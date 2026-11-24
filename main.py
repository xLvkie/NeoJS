# main.py
import argparse
import os
import sys
from pathlib import Path
from antlr4 import *
from gen.NeoJSLexer import NeoJSLexer
from gen.NeoJSParser import NeoJSParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.code_gen_visitor import CodeGenVisitor
from builder import (
    DEFAULT_MDK_PATH,
    leer_propiedades_mdk,
    desplegar_a_mdk,
    compilar_jar_mdk,
)

RESPUESTAS_AFIRMATIVAS = {"s", "si", "sí", "y", "yes"}


def preguntar_si_no(mensaje: str) -> bool | None:
    """Solicita confirmación [s/N] al usuario manejando interrupciones sin traceback."""
    try:
        respuesta = input(mensaje).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\n[CANCELADO] Operación cancelada por el usuario.")
        return None
    return respuesta in RESPUESTAS_AFIRMATIVAS


def _solicitar_y_compilar_jar(mdk_path: str, props: dict):
    """Paso 2 interactivo: pregunta si se debe ejecutar ./gradlew build y extraer el .jar."""
    resp_build = preguntar_si_no(
        "\n¿Deseas compilar el mod con Gradle ('./gradlew build') y extraer el .jar en 'dist/'? [s/N]: "
    )
    if resp_build is None:
        return
    if resp_build:
        compilar_jar_mdk(mdk_path=mdk_path, dist_dir="dist", props=props)
    else:
        print(
            "\n[INFO] Las fuentes ya fueron actualizadas en IntelliJ; "
            "puedes ejecutar la tarea 'runClient' directamente desde el IDE."
        )


def compilar_archivo(
    ruta_archivo: str,
    mdk_path: str = DEFAULT_MDK_PATH,
    auto_yes: bool = False,
    no_deploy: bool = False,
):
    """Compila un script NeoJS a Java/JSON en salida_neoforge/<nombre_script>/ y ejecuta el asistente."""
    if not os.path.isfile(ruta_archivo):
        print(f"[FALLO] No se encontró el archivo fuente: '{ruta_archivo}'.")
        return

    # Análisis Léxico y Sintáctico
    input_stream = FileStream(ruta_archivo, encoding="utf-8")
    lexer = NeoJSLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NeoJSParser(stream)

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\n[FALLO] Se encontraron errores sintácticos en '{ruta_archivo}'.")
        return

    print("[OK] Análisis Léxico y Sintáctico completado sin errores.")

    # Análisis Semántico
    semantico = SemanticVisitor()
    semantico.visit(tree)

    if len(semantico.errores) > 0:
        print(f"\n[FALLO] Se detectaron {len(semantico.errores)} errores semánticos:")
        for idx, err in enumerate(semantico.errores, 1):
            print(f"  {idx}. {err}")
        return

    print("[OK] Análisis Semántico completado exitosamente.")
    print(f"  - Ítems registrados ({len(semantico.items_declarados)}): {list(semantico.items_declarados.keys())}")
    print(f"  - Armas registradas ({len(semantico.weapons_declaradas)}): {list(semantico.weapons_declaradas.keys())}")
    print(f"  - Recetas registradas ({len(semantico.recipes_declaradas)}): {list(semantico.recipes_declaradas.keys())}")
    print(f"  - Mobs registrados ({len(semantico.mobs_declarados)}): {list(semantico.mobs_declarados.keys())}")
    print(f"  - Modificaciones vanilla ({len(semantico.modificaciones)}): {[m['target'] for m in semantico.modificaciones]}")

    # Lectura dinámica de propiedades del MDK
    props = leer_propiedades_mdk(mdk_path)

    # Aislamiento de salida por nombre de script
    script_name = Path(ruta_archivo).stem
    salida_dir = os.path.join("salida_neoforge", script_name)

    # Generación de Código Java y Recursos JSON
    print("\n--- Iniciando Generación de Código Java (Minecraft NeoForge) ---")
    codegen = CodeGenVisitor(mod_id=props["mod_id"], base_package=props["mod_group_id"])
    codegen.visit(tree)
    codegen.finalizar()
    codigo_java = codegen.emitir(salida_dir)
    print(codigo_java)
    print(f"\n[ÉXITO] Código Java y recursos JSON para NeoForge generados en './{salida_dir}/'")

    if no_deploy:
        print(
            f"\n[INFO] Modo '--no-deploy' activo. La salida quedó guardada en '{salida_dir}/'.\n"
            f"Para desplegarla al MDK más adelante ejecuta:\n"
            f"  python main.py deploy {salida_dir}"
        )
        return

    if auto_yes:
        desplegar_a_mdk(salida_dir, mdk_path=mdk_path, props=props)
        compilar_jar_mdk(mdk_path=mdk_path, dist_dir="dist", props=props)
        return

    # Asistente interactivo Paso 1: Desplegar al MDK (IntelliJ)
    resp_deploy = preguntar_si_no(
        f"\n¿Deseas mover y reemplazar esta lógica en el proyecto MDK de IntelliJ ({mdk_path})? [s/N]: "
    )
    if resp_deploy is None:
        return
    if not resp_deploy:
        print(
            f"\n[INFO] El proyecto MDK no fue modificado. Código disponible en '{salida_dir}/'.\n"
            f"Para desplegarlo al MDK más adelante ejecuta:\n"
            f"  python main.py deploy {salida_dir}"
        )
        return

    desplegar_a_mdk(salida_dir, mdk_path=mdk_path, props=props)
    print("[INFO] El código fuente y recursos ya están listos en IntelliJ.")

    # Asistente interactivo Paso 2: Compilar el .jar con Gradle
    _solicitar_y_compilar_jar(mdk_path, props)


def desplegar_carpeta(
    ruta_carpeta: str,
    mdk_path: str = DEFAULT_MDK_PATH,
    build: bool = False,
    auto_yes: bool = False,
):
    """Despliega una compilación previa desde salida_neoforge/<nombre>/ hacia el MDK."""
    if not os.path.isdir(ruta_carpeta):
        print(f"[FALLO] No existe la carpeta de salida '{ruta_carpeta}'.")
        return
    if not os.path.isfile(os.path.join(ruta_carpeta, "NeoJSMod.java")):
        print(
            f"[FALLO] La carpeta '{ruta_carpeta}' no contiene una compilación NeoJS válida "
            "(falta 'NeoJSMod.java')."
        )
        return

    props = desplegar_a_mdk(ruta_carpeta, mdk_path=mdk_path)
    print("[INFO] El código fuente y recursos ya están listos en IntelliJ.")

    if build or auto_yes:
        compilar_jar_mdk(mdk_path=mdk_path, dist_dir="dist", props=props)
    else:
        _solicitar_y_compilar_jar(mdk_path, props)


def listar_compilaciones(base_dir: str = "salida_neoforge"):
    """Muestra todas las subcarpetas disponibles en salida_neoforge/ listas para desplegarse."""
    if not os.path.isdir(base_dir):
        print(f"[INFO] No existe el directorio '{base_dir}/'. Compila un script primero.")
        return

    disponibles = sorted(
        nombre
        for nombre in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, nombre))
        and os.path.isfile(os.path.join(base_dir, nombre, "NeoJSMod.java"))
    )

    if not disponibles:
        print(f"[INFO] No hay compilaciones guardadas en '{base_dir}/'.")
        return

    print(f"Compilaciones disponibles en '{base_dir}/' ({len(disponibles)}):")
    for nombre in disponibles:
        ruta = os.path.join(base_dir, nombre)
        print(f"  - {nombre:<20} -> python main.py deploy {ruta}")


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Compilador DSL NeoJS para Minecraft NeoForge 1.21.1",
    )
    subparsers = parser.add_subparsers(dest="comando", help="Subcomandos disponibles")

    # Subcomando compile (por defecto al pasar directamente <ruta_script.txt>)
    p_compile = subparsers.add_parser(
        "compile",
        help="Compila un script NeoJS (.txt) hacia salida_neoforge/<nombre_script>/",
    )
    p_compile.add_argument("ruta_script", help="Ruta al archivo fuente NeoJS (.txt)")
    p_compile.add_argument(
        "--mdk",
        default=DEFAULT_MDK_PATH,
        help=f"Ruta al proyecto plantilla MDK de NeoForge (por defecto: {DEFAULT_MDK_PATH})",
    )
    grupo_modo = p_compile.add_mutually_exclusive_group()
    grupo_modo.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Omite preguntas interactivas: despliega al MDK y compila el .jar automáticamente",
    )
    grupo_modo.add_argument(
        "--no-deploy",
        action="store_true",
        help="Genera salida_neoforge/<nombre_script>/ y termina sin preguntar ni tocar el MDK",
    )

    # Subcomando deploy
    p_deploy = subparsers.add_parser(
        "deploy",
        help="Despliega una compilación previa (salida_neoforge/<nombre>/) al MDK",
    )
    p_deploy.add_argument("ruta_carpeta", help="Carpeta compilada (ej. salida_neoforge/general_mod)")
    p_deploy.add_argument(
        "--mdk",
        default=DEFAULT_MDK_PATH,
        help=f"Ruta al proyecto plantilla MDK de NeoForge (por defecto: {DEFAULT_MDK_PATH})",
    )
    p_deploy.add_argument(
        "--build",
        action="store_true",
        help="Ejecuta './gradlew build' automáticamente tras desplegar al MDK",
    )
    p_deploy.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Omite confirmación interactiva y compila el .jar automáticamente",
    )

    # Subcomando list
    subparsers.add_parser(
        "list",
        help="Lista las compilaciones disponibles en salida_neoforge/",
    )

    return parser


def main(argv: list[str] | None = None):
    if argv is None:
        argv = sys.argv[1:]

    parser = construir_parser()
    if not argv:
        parser.print_help()
        return

    if argv[0] not in {"compile", "deploy", "list", "-h", "--help"}:
        argv = ["compile", *argv]

    args = parser.parse_args(argv)

    if args.comando == "compile":
        compilar_archivo(
            args.ruta_script,
            mdk_path=args.mdk,
            auto_yes=args.yes,
            no_deploy=args.no_deploy,
        )
    elif args.comando == "deploy":
        desplegar_carpeta(
            args.ruta_carpeta,
            mdk_path=args.mdk,
            build=args.build,
            auto_yes=args.yes,
        )
    elif args.comando == "list":
        listar_compilaciones()


if __name__ == "__main__":
    main()
