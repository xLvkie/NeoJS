# Contexto del Proyecto: NeoJS (Compilador DSL para Minecraft NeoForge)

## 1. Descripción General del Proyecto
**NeoJS** es un Lenguaje de Dominio Específico (DSL) declarativo diseñado para abstraer la complejidad de la creación de mods en Minecraft (específicamente para la API **NeoForge 1.21.x**). 

En lugar de que un usuario escriba cientos de líneas de código Java repetitivo (boilerplate) interactuando con los registros de NeoForge, el usuario escribe un script sencillo en NeoJS. El compilador lee este script, valida sus reglas lógicas y semánticas, y actúa como un **transpilador (source-to-source compiler)**, generando automáticamente todo el código fuente en Java y los recursos JSON listos para ser empaquetados en un archivo `.jar`.

## 2. Objetivo Final (Pendiente de Implementar)
Actualmente, el compilador genera correctamente el código Java y los JSON en la carpeta `salida_neoforge/`. 
**El siguiente paso (Hito 3 / Final) es la automatización End-to-End con el MDK (Mod Development Kit) de NeoForge:**
1. Descargar/Tener una plantilla base del MDK de NeoForge (basada en Gradle).
2. Hacer que el compilador en Python inyecte automáticamente los archivos de `salida_neoforge/` dentro de las carpetas `src/main/java/` y `src/main/resources/` del MDK.
3. Ejecutar automáticamente (en segundo plano) el comando `./gradlew build`.
4. Extraer el archivo `.jar` resultante de la carpeta `build/libs/` y entregárselo al usuario listo para jugar.

## 3. Arquitectura del Compilador (Estado Actual)
El proyecto sigue una arquitectura clásica de tres fases utilizando **ANTLR4** (patrón Visitor):

### A. Frontend (Análisis Léxico y Sintáctico)
* **Archivo:** `NeoJS.g4`
* **Función:** Define las reglas léxicas (tokens como `NUMBER`, `ID` con soporte para namespaces como `minecraft:zombie`) y sintácticas (formato BNF).
* **Construcciones soportadas:**
  1. `item`: Declaración de materiales base.
  2. `weapon`: Declaración de armas (heredan de `SwordItem` y aplican efectos).
  3. `recipe`: Recetas para la mesa de crafteo.
  4. `mob`: Declaración de entidades pacíficas o agresivas (heredan de `Zombie` o `WanderingTrader`).
  5. `modify`: Alteración de atributos base de ítems o mobs de Minecraft vainilla.

### B. Middle-end (Análisis Semántico)
* **Archivo:** `semantic/semantic_visitor.py`
* **Función:** Recorre el AST (Árbol Sintáctico Abstracto) validando reglas de negocio del juego antes de generar código. Mantiene tablas de símbolos para evitar colisiones.
* **Reglas validadas (10 en total):**
  1. Identificadores duplicados (redeclaraciones).
  2. Incompatibilidad de tipos (ej. `STRING` en vez de `NUMBER`).
  3. Atributos fuera de contexto o desconocidos.
  4. Propiedades duplicadas en el mismo bloque.
  5. Valores de enumeración inválidos (ej. `rarity` solo acepta common/uncommon/rare/epic).
  6. Rangos numéricos inválidos (stack > 64, vida negativa, etc.).
  7. Atributos obligatorios faltantes.
  8. Referencias a entidades no declaradas (ej. en recetas de crafteo).
  9. Modificaciones a entidades sin el namespace obligatorio (`minecraft:`).
  10. Inconsistencia lógica (ej. un mob `passive` no puede tener `damage > 0`).

### C. Backend (Generación de Código)
* **Archivo:** `codegen/code_gen_visitor.py`
* **Función:** Genera la arquitectura Java de NeoForge 1.21.x.
* **Salida generada (`salida_neoforge/`):**
  * Clases individuales para ítems, armas y entidades.
  * `events/VanillaOverridesHandler.java`: Usa `@SubscribeEvent` en `EntityJoinLevelEvent` para modificar mobs nativos en tiempo real.
  * `NeoJSMod.java`: Clase `@Mod` principal con `DeferredRegister` para ítems, entidades, huevos generadores y una pestaña creativa (CreativeModeTab).
  * `resources/`: JSONs de recetas, modelos de ítems y archivos de traducción (lang).

### D. Orquestador y Pruebas
* **Archivo:** `main.py`
* **Función:** Punto de entrada. Ejecuta las fases en orden: Lexer -> Parser -> Semantic -> Codegen. Imprime un resumen de los errores semánticos o, si todo es válido, emite el código a `salida_neoforge/`.
* **Pruebas:** 
  * `tests/correct/correct1..10.txt` y `tests/correct/general_mod.txt`
  * `tests/errors/error1..10.txt`

## 4. Instrucciones para el Agente (Antigravity)
Al leer este proyecto, ten en cuenta que el código actual **ya es funcional a nivel de compilación**. Tu tarea a partir de ahora se centrará en el **"Objetivo Final"**:
1. No modifiques la gramática (`NeoJS.g4`) ni el analizador semántico a menos que se solicite agregar una nueva característica (ej. bloques, armaduras).
2. Ayuda a crear el puente (script de automatización o ajustes en `main.py`) que copie el contenido de `salida_neoforge/` hacia la estructura estándar de un proyecto Gradle (`src/main/java/com/neojs/mod/` y `src/main/resources/`).
3. Ayuda a orquestar subprocesos (subprocess) en Python para disparar la tarea de Gradle de NeoForge (`gradlew build`) y gestionar la compilación del mod `.jar`.