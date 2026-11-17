# builder.py
import os
import shutil
import subprocess

DEFAULT_MDK_PATH = "/home/bookie/Proyectos/Neoforge-myMod-1.21.1"


def leer_propiedades_mdk(mdk_path=DEFAULT_MDK_PATH) -> dict:
    """Lee gradle.properties del MDK y extrae mod_id, mod_group_id y mod_version."""
    props_path = os.path.join(mdk_path, "gradle.properties")
    if not os.path.isfile(props_path):
        raise FileNotFoundError(f"No se encontró gradle.properties en: {props_path}")

    propiedades = {}
    with open(props_path, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#") or "=" not in linea:
                continue
            clave, valor = linea.split("=", 1)
            propiedades[clave.strip()] = valor.strip()

    requeridas = ("mod_id", "mod_group_id", "mod_version")
    faltantes = [k for k in requeridas if not propiedades.get(k)]
    if faltantes:
        raise ValueError(
            f"Faltan propiedades requeridas en {props_path}: {', '.join(faltantes)}"
        )

    return {
        "mod_id": propiedades["mod_id"],
        "mod_group_id": propiedades["mod_group_id"],
        "mod_version": propiedades["mod_version"],
    }


def limpiar_mdk(mdk_path: str, base_package: str):
    """Limpia src/main/java/ y las carpetas generables de resources/ en el MDK."""
    java_dir = os.path.join(mdk_path, "src", "main", "java")
    if os.path.exists(java_dir):
        shutil.rmtree(java_dir)

    package_subpath = os.path.join(*base_package.split("."))
    package_dir = os.path.join(java_dir, package_subpath)
    os.makedirs(package_dir, exist_ok=True)

    resources_dir = os.path.join(mdk_path, "src", "main", "resources")
    os.makedirs(resources_dir, exist_ok=True)
    for subdir in ("assets", "data"):
        target = os.path.join(resources_dir, subdir)
        if os.path.exists(target):
            shutil.rmtree(target)


def copiar_fuentes_a_mdk(carpeta_salida: str, mdk_path: str, base_package: str):
    """Copia el código Java y los recursos JSON desde carpeta_salida hacia el MDK."""
    if not os.path.isdir(carpeta_salida):
        raise FileNotFoundError(f"No existe la carpeta de salida: {carpeta_salida}")

    package_subpath = os.path.join(*base_package.split("."))
    package_dir = os.path.join(mdk_path, "src", "main", "java", package_subpath)
    resources_dir = os.path.join(mdk_path, "src", "main", "resources")
    os.makedirs(package_dir, exist_ok=True)
    os.makedirs(resources_dir, exist_ok=True)

    for entrada in os.listdir(carpeta_salida):
        origen = os.path.join(carpeta_salida, entrada)
        if entrada == "resources" and os.path.isdir(origen):
            shutil.copytree(origen, resources_dir, dirs_exist_ok=True)
        elif os.path.isdir(origen):
            shutil.copytree(origen, os.path.join(package_dir, entrada), dirs_exist_ok=True)
        else:
            shutil.copy2(origen, os.path.join(package_dir, entrada))


def ejecutar_gradle_y_extraer_jar(
    mdk_path: str, mod_id: str, mod_version: str, dist_dir: str = "dist"
) -> str:
    """Ejecuta ./gradlew build en el MDK y copia el .jar final a dist_dir."""
    gradlew_path = os.path.join(mdk_path, "gradlew")
    if not os.path.isfile(gradlew_path):
        raise FileNotFoundError(f"No se encontró el script gradlew en: {gradlew_path}")

    os.chmod(gradlew_path, 0o755)
    subprocess.run(["./gradlew", "build"], cwd=mdk_path, check=True)

    libs_dir = os.path.join(mdk_path, "build", "libs")
    if not os.path.isdir(libs_dir):
        raise FileNotFoundError(f"No se encontró el directorio de salida Gradle: {libs_dir}")

    jar_esperado = os.path.join(libs_dir, f"{mod_id}-{mod_version}.jar")
    jar_origen = None
    if os.path.isfile(jar_esperado):
        jar_origen = jar_esperado
    else:
        candidatos = [
            os.path.join(libs_dir, f)
            for f in sorted(os.listdir(libs_dir))
            if f.endswith(".jar") and not f.endswith(("-sources.jar", "-dev.jar"))
        ]
        if candidatos:
            jar_origen = candidatos[0]

    if not jar_origen:
        raise FileNotFoundError(f"No se encontró ningún archivo .jar compilado en: {libs_dir}")

    os.makedirs(dist_dir, exist_ok=True)
    jar_destino = os.path.join(dist_dir, os.path.basename(jar_origen))
    shutil.copy2(jar_origen, jar_destino)
    return jar_destino


def construir_mod(
    carpeta_salida="salida_neoforge",
    mdk_path=DEFAULT_MDK_PATH,
    dist_dir="dist",
    props=None,
) -> str:
    """Orquesta la limpieza del MDK, inyección de código, build con Gradle y entrega del .jar."""
    if props is None:
        props = leer_propiedades_mdk(mdk_path)

    mod_id = props["mod_id"]
    base_package = props["mod_group_id"]
    mod_version = props["mod_version"]

    print(f"\n--- Preparando plantilla NeoForge MDK ({mod_id} v{mod_version} | {base_package}) ---")
    print(f"[1/3] Limpiando clases previas y recursos generados en '{mdk_path}'...")
    limpiar_mdk(mdk_path, base_package)

    print(f"[2/3] Copiando fuentes y recursos desde '{carpeta_salida}/' hacia el MDK...")
    copiar_fuentes_a_mdk(carpeta_salida, mdk_path, base_package)

    print("[3/3] Ejecutando './gradlew build' (esto puede tardar unos segundos)...")
    jar_final = ejecutar_gradle_y_extraer_jar(mdk_path, mod_id, mod_version, dist_dir=dist_dir)
    print(f"[ÉXITO] Mod compilado listo para Minecraft en: '{jar_final}'")
    return jar_final
