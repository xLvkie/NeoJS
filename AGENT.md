# Contexto del Proyecto: NeoJS (Compilador DSL para Minecraft NeoForge)

## 1. Descripción General del Proyecto
**NeoJS** es un Lenguaje de Dominio Específico (DSL) declarativo diseñado para abstraer la complejidad de la creación de mods en Minecraft (**API NeoForge 1.21.1 / Java 21**).

En lugar de escribir cientos de líneas de boilerplate interactuando con los registros y eventos de NeoForge, el usuario redacta un script declarativo en NeoJS (`.txt`). El compilador valida las reglas léxicas, sintácticas y semánticas, transpila el código fuente Java y recursos JSON hacia una carpeta aislada por script, y automatiza de extremo a extremo la inyección en la plantilla MDK de Gradle y la compilación del `.jar` final.

---

## 2. Estado Actual: Pipeline End-to-End Implementado
El puente automatizado entre **NeoJS**, la plantilla **MDK de NeoForge 1.21.1** y **Gradle** ya se encuentra implementado y funcional:

1. **Lectura Dinámica del MDK (`builder.leer_propiedades_mdk`):** Lee automáticamente `gradle.properties` del MDK destino para extraer `mod_id`, `mod_group_id` (paquete base Java) y `mod_version`. No existe ningún identificador hardcodeado en el compilador.
2. **Aislamiento de Salidas por Script:** Cada script compilado emite sus artefactos de manera aislada en `salida_neoforge/<nombre_script>/` (sin sobrescribir compilaciones de otros scripts).
3. **Desacoplamiento Despliegue vs. Compilación (`builder.py`):**
   * `desplegar_a_mdk(...)`: limpia `src/main/java/` (evitando clases `@Mod` duplicadas) y `src/main/resources/{assets,data}` preservando `META-INF/neoforge.mods.toml`, e inyecta los fuentes y JSON en el MDK.
   * `compilar_jar_mdk(...)`: ejecuta `./gradlew build` mediante `subprocess` y extrae el `.jar` resultante de `build/libs/` hacia `dist/`.
   * `construir_mod(...)`: fachada retrocompatible que ejecuta ambos pasos secuencialmente.
4. **CLI con Subcomandos y Asistente Interactivo (`main.py`):**
   * `python main.py <ruta_script.txt> [--mdk RUTA] [--yes | -y] [--no-deploy]` (modo `compile` por defecto).
   * `python main.py compile <ruta_script.txt> [--mdk RUTA] [--yes | -y] [--no-deploy]`: compila a `salida_neoforge/<nombre_script>/` y lanza un asistente interactivo de 2 pasos (1. mover lógica al MDK de IntelliJ; 2. compilar `.jar` con Gradle en `dist/`), salvo que se indique `-y/--yes` o `--no-deploy`.
   * `python main.py deploy <ruta_carpeta> [--mdk RUTA] [--build] [--yes | -y]`: despliega una carpeta ya compilada (ej. `salida_neoforge/general_mod`) hacia el MDK y opcionalmente ejecuta `./gradlew build`.
   * `python main.py list`: lista todas las compilaciones guardadas en `salida_neoforge/` listas para desplegarse.

---

## 3. Arquitectura del Compilador

### A. Frontend (Análisis Léxico y Sintáctico)
* **Archivos:** `NeoJS.g4` y código generado en `gen/`.
* **Construcciones soportadas:**
  1. `item`: Declaración de ítems base.
  2. `weapon`: Declaración de armas (`SwordItem`, `SimpleTier` y efectos en `hurtEnemy`).
  3. `recipe`: Recetas de crafteo (`minecraft:crafting_shaped` para 1.21).
  4. `mob`: Entidades personalizadas agresivas (`Zombie`) o pasivas/neutrales (`WanderingTrader` con `Mob.createMobAttributes()`).
  5. `modify`: Alteración de atributos base de ítems o mobs vanilla.

### B. Middle-end (Análisis Semántico)
* **Archivo:** `semantic/semantic_visitor.py`.
* **Reglas validadas (10 en total):**
  1. Identificadores duplicados.
  2. Incompatibilidad de tipos (`reglas_tipos`).
  3. Atributos no reconocidos o fuera de contexto (`atributos_por_contexto`).
  4. Propiedades duplicadas en el mismo bloque.
  5. Valores de enumeración inválidos (`rarity`, `behavior`).
  6. Rangos numéricos y porcentajes inválidos.
  7. Atributos obligatorios faltantes (`damage` en `weapon`; `result` e `ingredients` en `recipe`).
  8. Referencias a ítems/armas no declarados en recetas.
  9. Namespace obligatorio (`:`) en `modify`, `base_item` y `base_model`.
  10. Inconsistencia lógica (`passive` con `damage > 0`).

### C. Backend (Generación de Código)
* **Archivo:** `codegen/code_gen_visitor.py`.
* **Clase principal `NeoJSMod.java`:** Registra `ITEMS`, `ENTITY_TYPES`, `CREATIVE_TABS` y expone:
  * `ModBusEvents` (`@EventBusSubscriber(..., bus = EventBusSubscriber.Bus.MOD)`): `EntityAttributeCreationEvent` para todos los mobs.
  * `ClientModEvents` (`@EventBusSubscriber(..., bus = EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)`): `EntityRenderersEvent.RegisterRenderers` vinculando `ZombieRenderer::new` (agresivos) y `WanderingTraderRenderer::new` (pasivos/neutrales).
* **Eventos vanilla:** `events/VanillaOverridesHandler.java` con `EntityJoinLevelEvent`.
* **Recursos:** `resources/assets/<mod_id>/{models/item,lang}` y `resources/data/<mod_id>/recipe/`.
* **Salida:** `salida_neoforge/<nombre_script>/`.

### D. Puente MDK, Orquestador y Pruebas
* **Archivos:** `builder.py` y `main.py`.
* **Entrega final:** `dist/<mod_id>-<mod_version>.jar`.
* **Pruebas:**
  * `tests/correct/correct1..10.txt` y `tests/correct/general_mod.txt`.
  * `tests/errors/error1..10.txt`.

---

## 4. Reglas Permanentes para Futuros Agentes (Antigravity)
1. **Sincronización Documental Obligatoria:** En **toda iteración futura** sobre este repositorio debes mantener `AGENT.md` y `ARCHITECTURE.md` actualizados y coherentes con el código real antes de finalizar la tarea.
2. **Cero Hardcodeo:** `mod_id`, `base_package` (`mod_group_id`) y `mod_version` deben leerse siempre dinámicamente desde `<mdk_path>/gradle.properties` mediante `builder.leer_propiedades_mdk()` y pasarse por constructor a `CodeGenVisitor(mod_id, base_package)`.
3. **Inmutabilidad Selectiva del Núcleo:** No modifiques `NeoJS.g4`, `gen/*` ni las 10 reglas de `semantic/semantic_visitor.py` salvo cuando la tarea solicite explícitamente añadir nuevas construcciones o atributos al DSL (consulta la guía paso a paso en `ARCHITECTURE.md`).
4. **Integridad de Recursos en el MDK:** Al limpiar el MDK (`limpiar_mdk`), elimina `src/main/java/` y `src/main/resources/{assets,data}` pero conserva siempre intacto `src/main/resources/META-INF/neoforge.mods.toml`.

---

## 5. Hoja de Ruta Oficial (Fases Futuras)
1. **Fase 1 (Próxima):** Texturas personalizadas (`.png`) y escalado visual (`scale` + `PoseStack`) sobre modelos base de entidades en el cliente (`ClientModEvents`).
2. **Fase 2:** Sonidos personalizados (`sounds.json`) y generación natural de mobs en biomas (`neoforge/biome_modifier` con `add_spawns`).
3. **Fase 3:** Integración de **GeckoLib** como dependencia en `build.gradle` del MDK para soportar geometrías 3D personalizadas (`.geo.json`) y animaciones (`.animation.json`) de criaturas complejas.
4. **Fase 4:** Generación de mundo y minerales (`ore` / `worldgen`: `configured_feature`, `placed_feature` y `biome_modifier` de `add_features`).
5. **Fase 5:** Tablas de botín (`loot` / `loot_table` en JSON) y efectos de estado avanzados.
