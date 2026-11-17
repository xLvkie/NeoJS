# main.py
import sys
from antlr4 import *
from gen.NeoJSLexer import NeoJSLexer
from gen.NeoJSParser import NeoJSParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.code_gen_visitor import CodeGenVisitor
from builder import DEFAULT_MDK_PATH, leer_propiedades_mdk, construir_mod


def compilar_archivo(ruta_archivo, mdk_path=DEFAULT_MDK_PATH):
    # Análisis Léxico y Sintáctico
    input_stream = FileStream(ruta_archivo, encoding='utf-8')
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

    # Generación de Código Java y Recursos JSON
    print("\n--- Iniciando Generación de Código Java (Minecraft NeoForge) ---")
    codegen = CodeGenVisitor(mod_id=props["mod_id"], base_package=props["mod_group_id"])
    codegen.visit(tree)
    codegen.finalizar()
    codigo_java = codegen.emitir("salida_neoforge")
    print(codigo_java)
    print("\n[ÉXITO] Código Java y recursos JSON para NeoForge generados en './salida_neoforge/'")

    # Construcción del .jar en el MDK de NeoForge
    construir_mod("salida_neoforge", mdk_path=mdk_path, dist_dir="dist", props=props)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ruta_script = sys.argv[1]
        ruta_mdk = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_MDK_PATH
        compilar_archivo(ruta_script, mdk_path=ruta_mdk)
    else:
        print("Uso: python main.py <ruta_del_archivo.txt> [ruta_mdk]")