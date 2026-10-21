# code_gen_visitor.py
import os  # [Fuera de los temas del curso]: Uso del módulo 'os' para gestión de carpetas y archivos
from gen.NeoJSVisitor import NeoJSVisitor
from gen.NeoJSParser import NeoJSParser

class CodeGenVisitor(NeoJSVisitor):

    def __init__(self, package_name="com.NeoJS.generated", mod_id="examplemod"):
        self.package_name = package_name
        self.mod_id = mod_id
        # Guardamos rutas relativas con su subcarpeta: {"items/EspadaItem.java": "codigo..."}
        self.archivos_java = {}
        self.items_registrados = []
        self.eventos_modificacion = []

    # 1. Generación de Clase Java para Ítem (NeoForge API)
    def visitItemDecl(self, ctx: NeoJSParser.ItemDeclContext):
        nombre_item = ctx.ID().getText()
        nombre_clase = f"{nombre_item}Item"
        self.items_registrados.append((nombre_item.lower(), nombre_clase))
        attrs = self.visit(ctx.attrList())

        damage = int(attrs.get("damage", ("NUMBER", 5))[1])
        durability = int(attrs.get("durability", ("NUMBER", 250))[1])
        attack_speed = float(attrs.get("attack_speed", ("NUMBER", -2.4))[1])
        fire_immune = attrs.get("fire_immune", ("BOOLEAN", False))[1]
        glowing = attrs.get("glowing", ("BOOLEAN", False))[1]
        display_name = attrs.get("name", ("STRING", nombre_item))[1]

        prop_extra = ".fireResistant()" if fire_immune else ""

        metodo_glow = ""
        if glowing:
            metodo_glow = """
    @Override
    public boolean isFoil(ItemStack stack) {
        return true;
    }"""

        codigo_java = f"""package {self.package_name}.items;

import net.minecraft.world.item.SwordItem;
import net.minecraft.world.item.Tiers;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;

/**
 * Ítem autogenerado por NeoJS para NeoForge: {nombre_item} ("{display_name}")
 */
public class {nombre_clase} extends SwordItem {{
    public {nombre_clase}() {{
        super(Tiers.DIAMOND, new Item.Properties()
                .durability({durability}){prop_extra}
                .attributes(SwordItem.createAttributes(Tiers.DIAMOND, {damage}, {attack_speed}f)));
    }}
{metodo_glow}
}}
"""
        self.archivos_java[f"items/{nombre_clase}.java"] = codigo_java

    # 2. Generación de Clase Java para Jefe (Boss / Phase)
    def visitBossDecl(self, ctx: NeoJSParser.BossDeclContext):
        nombre_boss = ctx.ID().getText()
        nombre_clase = f"{nombre_boss}BossEntity"
        attrs = self.visit(ctx.attrList())

        hp = float(attrs.get("hp", ("NUMBER", 200.0))[1])
        damage = float(attrs.get("damage", ("NUMBER", 15.0))[1])
        armor = float(attrs.get("armor", ("NUMBER", 10.0))[1])
        ability = attrs.get("ability", ("STRING", "none"))[1]
        condicion = attrs.get("condition", ("CONDITION", "hp < 50.0"))[1]

        codigo_java = f"""package {self.package_name}.entities;

import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.AttributeSupplier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.level.Level;

/**
 * Entidad de Jefe autogenerada por NeoJS para NeoForge: {nombre_boss}
 */
public class {nombre_clase} extends Monster {{

    public {nombre_clase}(EntityType<? extends Monster> type, Level level) {{
        super(type, level);
    }}

    public static AttributeSupplier.Builder createAttributes() {{
        return Monster.createMonsterAttributes()
                .add(Attributes.MAX_HEALTH, {hp}D)
                .add(Attributes.ATTACK_DAMAGE, {damage}D)
                .add(Attributes.ARMOR, {armor}D);
    }}

    @Override
    public void tick() {{
        super.tick();
        // Condición de fase configurada en NeoJS: {condicion}
        if (this.getHealth() < (this.getMaxHealth() * 0.5f)) {{
            triggerSpecialAbility("{ability}");
        }}
    }}

    private void triggerSpecialAbility(String abilityName) {{
        // Lógica de ejecución para la habilidad: {ability}
    }}
}}
"""
        self.archivos_java[f"entities/{nombre_clase}.java"] = codigo_java

    # 3. Generación de Clase Java para Tabla de Botín (Loot)
    def visitLootDecl(self, ctx: NeoJSParser.LootDeclContext):
        nombre_loot = ctx.ID().getText()
        nombre_clase = f"{nombre_loot}LootHandler"
        drops = self.visit(ctx.dropList())

        bloques_drop = []
        for d in drops:
            item_id = d["item"]
            attrs = d["attrs"]
            chance = float(attrs.get("chance", ("PERCENTAGE", 100.0))[1]) / 100.0
            cant_min = int(attrs.get("min", ("NUMBER", 1))[1])
            cant_max = int(attrs.get("max", ("NUMBER", 1))[1])

            bloques_drop.append(f"""        // Drop: {item_id} ({chance * 100:.1f}%)
        if (Math.random() <= {chance}) {{
            int amount = {cant_min} + (int)(Math.random() * ({cant_max} - {cant_min} + 1));
            spawnDrop("{item_id}", amount);
        }}""")

        cuerpo_drops = "\n\n".join(bloques_drop)

        codigo_java = f"""package {self.package_name}.loot;

/**
 * Tabla de botín autogenerada por NeoJS: {nombre_loot}
 */
public class {nombre_clase} {{

    public static void rollLoot() {{
{cuerpo_drops}
    }}

    private static void spawnDrop(String itemId, int count) {{
        System.out.println("Spawning drop: " + count + "x " + itemId);
    }}
}}
"""
        self.archivos_java[f"loot/{nombre_clase}.java"] = codigo_java

    def visitDropList(self, ctx: NeoJSParser.DropListContext):
        return [self.visit(d) for d in ctx.dropDecl()]

    def visitDropDecl(self, ctx: NeoJSParser.DropDeclContext):
        return {"item": ctx.ID().getText(), "attrs": self.visit(ctx.attrList())}

    # 4. Recolección de Modificaciones
    def visitModifyDecl(self, ctx: NeoJSParser.ModifyDeclContext):
        self.eventos_modificacion.append({
            "target": ctx.ID().getText(),
            "attrs": self.visit(ctx.attrList())
        })

    def visitAttrList(self, ctx: NeoJSParser.AttrListContext):
        atributos = {}
        for attr_ctx in ctx.attr():
            clave, val_info = self.visit(attr_ctx)
            atributos[clave] = val_info
        return atributos

    def visitAttr(self, ctx: NeoJSParser.AttrContext):
        if ctx.TK_CONDITION():
            return "condition", ("CONDITION", self.visit(ctx.condition()))
        return ctx.ID().getText(), self.visit(ctx.value())

    def visitCondition(self, ctx: NeoJSParser.ConditionContext):
        var_name = ctx.ID().getText()
        op = ctx.OP_REL().getText()
        _, val = self.visit(ctx.value())
        return f"{var_name} {op} {val}"

    def visitValue(self, ctx: NeoJSParser.ValueContext):
        if ctx.NUMBER():
            return ("NUMBER", float(ctx.NUMBER().getText()))
        elif ctx.STRING():
            return ("STRING", ctx.STRING().getText()[1:-1])
        elif ctx.PERCENTAGE():
            return ("PERCENTAGE", float(ctx.PERCENTAGE().getText().replace("%", "")))
        elif ctx.TIME_LITERAL():
            return ("TIME_LITERAL", ctx.TIME_LITERAL().getText())
        elif ctx.TRUE() or ctx.FALSE():
            return ("BOOLEAN", ctx.getText() == "true")
        return ("ID", ctx.getText())

    def finalizar(self):
        # A. Generar el Registro Automático de Ítems para NeoForge (DeferredRegister.Items)
        if self.items_registrados:
            lineas_registro = []
            for reg_id, clase in self.items_registrados:
                lineas_registro.append(
                    f'    public static final DeferredItem<Item> {reg_id.upper()} = ITEMS.register("{reg_id}", () -> new {clase}());'
                )
            registros_str = "\n".join(lineas_registro)

            self.archivos_java["NeoJSRegistry.java"] = f"""package {self.package_name};

import {self.package_name}.items.*;
import net.minecraft.world.item.Item;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.neoforge.registries.DeferredItem;
import net.neoforged.neoforge.registries.DeferredRegister;

/**
 * Registro central autogenerado por NeoJS Compiler para Minecraft NeoForge
 */
public class NeoJSRegistry {{
    public static final DeferredRegister.Items ITEMS = DeferredRegister.createItems("{self.mod_id}");

{registros_str}

    public static void register(IEventBus eventBus) {{
        ITEMS.register(eventBus);
    }}
}}
"""

        # B. Generar el Interceptor de Eventos para 'modify item' en NeoForge
        if self.eventos_modificacion:
            bloques_if = []
            for mod in self.eventos_modificacion:
                target = mod["target"]
                attrs = mod["attrs"]
                lineas = []

                if "damage" in attrs:
                    lineas.append(f"                event.setAmount({float(attrs['damage'][1])}f);")
                if "crit_chance" in attrs:
                    prob = float(attrs["crit_chance"][1]) / 100.0
                    lineas.append(f"                if (Math.random() < {prob}) event.setAmount(event.getAmount() * 1.5f);")

                acciones_str = "\n".join(lineas)
                bloques_if.append(f"""            if (itemId.equals("{target}")) {{
{acciones_str}
            }}""")

            cuerpo_eventos = "\n\n".join(bloques_if)
            self.archivos_java["events/NeoJSEventHandler.java"] = f"""package {self.package_name}.events;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.entity.living.LivingIncomingDamageEvent;

/**
 * Interceptor de eventos autogenerado por NeoJS Compiler para NeoForge
 */
@EventBusSubscriber(modid = "{self.mod_id}")
public class NeoJSEventHandler {{

    @SubscribeEvent
    public static void onLivingDamage(LivingIncomingDamageEvent event) {{
        if (event.getSource().getEntity() instanceof Player player) {{
            ItemStack heldItem = player.getMainHandItem();
            if (heldItem.isEmpty()) return;

            String itemId = BuiltInRegistries.ITEM.getKey(heldItem.getItem()).toString();
{cuerpo_eventos}
        }}
    }}
}}
"""

    def emitir(self, carpeta_salida="salida_java"):
        resumen_consola = []
        for ruta_relativa, contenido in self.archivos_java.items():
            ruta_completa = os.path.join(carpeta_salida, ruta_relativa)
            os.makedirs(os.path.dirname(ruta_completa), exist_ok=True)
            with open(ruta_completa, "w", encoding="utf-8") as f:
                f.write(contenido)
            resumen_consola.append(f"// ==========================================\n// ARCHIVO GENERADO: {ruta_completa}\n// ==========================================\n{contenido}")
        return "\n".join(resumen_consola)