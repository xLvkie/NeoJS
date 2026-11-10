# codegen/code_gen_visitor.py
import os
import json
from gen.NeoJSVisitor import NeoJSVisitor
from gen.NeoJSParser import NeoJSParser


class CodeGenVisitor(NeoJSVisitor):

    def __init__(self, mod_id="neojsmod", base_package="com.neojs.mod"):
        self.mod_id = mod_id
        self.base_package = base_package
        self.archivos_salida = {}
        self.items_generados = []
        self.weapons_generadas = []
        self.recipes_generadas = []
        self.mobs_generados = []
        self.mod_items = []
        self.mod_mobs = []
        self.traducciones = {
            f"itemGroup.{self.mod_id}.neojs_tab": "NeoJS Mod"
        }

    def _generar_modelo_item_json(self, short_id: str, base_item: str, is_handheld=False):
        tex_name = base_item.split(":")[-1]
        parent = "minecraft:item/handheld" if is_handheld else "minecraft:item/generated"
        model_json = {
            "parent": parent,
            "textures": {
                "layer0": f"minecraft:item/{tex_name}"
            }
        }
        self.archivos_salida[f"resources/assets/{self.mod_id}/models/item/{short_id}.json"] = json.dumps(model_json, indent=2)

    # ==========================================
    # CREACIÓN DE ÍTEMS (NEOFORGE)
    # ==========================================
    def visitItemDecl(self, ctx: NeoJSParser.ItemDeclContext):
        nombre = ctx.ID().getText()
        short_id = nombre.lower()
        const_name = nombre.upper()
        attrs = self.visit(ctx.attrList())

        display_name = attrs.get("name", ("STRING", nombre))[1]
        base_item = attrs.get("base_item", ("ID", "minecraft:diamond"))[1]
        asset_path = attrs.get("asset_path", ("STRING", "minecraft:textures/item/diamond.png"))[1]
        rarity_str = attrs.get("rarity", ("STRING", "epic"))[1].upper()
        if rarity_str not in ("COMMON", "UNCOMMON", "RARE", "EPIC"):
            rarity_str = "COMMON"
        stack_size = int(attrs.get("stack_size", ("NUMBER", 64))[1])
        fire_immune = attrs.get("fire_immune", ("BOOLEAN", False))[1]

        fire_chain = ".fireResistant()" if fire_immune else ""

        codigo_java = f"""package {self.base_package}.items;

import net.minecraft.world.item.Item;
import net.minecraft.world.item.Rarity;

/**
 * Ítem de NeoForge autogenerado por NeoJS: {nombre} ("{display_name}")
 * Diseño base (Fallback): {base_item}
 * Ruta de Asset personalizable: {asset_path}
 */
public class {nombre}Item extends Item {{
    public static final String REGISTRY_ID = "{short_id}";
    public static final String BASE_DESIGN = "{base_item}";
    public static final String CUSTOM_ASSET_PATH = "{asset_path}";

    public {nombre}Item() {{
        super(new Item.Properties()
            .stacksTo({stack_size})
            .rarity(Rarity.{rarity_str}){fire_chain}
        );
    }}
}}
"""
        self.archivos_salida[f"items/{nombre}Item.java"] = codigo_java
        self._generar_modelo_item_json(short_id, base_item, is_handheld=False)
        self.traducciones[f"item.{self.mod_id}.{short_id}"] = display_name
        self.items_generados.append({
            "class_name": f"{nombre}Item",
            "const_name": const_name,
            "short_id": short_id,
            "display_name": display_name
        })

    # ==========================================
    # CREACIÓN DE ARMAS (NEOFORGE)
    # ==========================================
    def visitWeaponDecl(self, ctx: NeoJSParser.WeaponDeclContext):
        nombre = ctx.ID().getText()
        short_id = nombre.lower()
        const_name = nombre.upper()
        attrs = self.visit(ctx.attrList())

        display_name = attrs.get("name", ("STRING", nombre))[1]
        base_item = attrs.get("base_item", ("ID", "minecraft:diamond_sword"))[1]
        asset_path = attrs.get("asset_path", ("STRING", "minecraft:textures/item/diamond_sword.png"))[1]
        damage = float(attrs.get("damage", ("NUMBER", 15.0))[1])
        durability = int(attrs.get("durability", ("NUMBER", 1500))[1])
        attack_speed = float(attrs.get("attack_speed", ("NUMBER", -2.0))[1])
        effect = attrs.get("effect", ("STRING", "none"))[1].lower()
        fire_immune = attrs.get("fire_immune", ("BOOLEAN", False))[1]

        fire_chain = ".fireResistant()" if fire_immune else ""

        mob_effect_code = ""
        if "wither" in effect:
            mob_effect_code = "target.addEffect(new MobEffectInstance(MobEffects.WITHER, 100, 1), attacker);"
        elif "slow" in effect:
            mob_effect_code = "target.addEffect(new MobEffectInstance(MobEffects.MOVEMENT_SLOWDOWN, 100, 1), attacker);"
        elif "poison" in effect:
            mob_effect_code = "target.addEffect(new MobEffectInstance(MobEffects.POISON, 100, 1), attacker);"
        elif "weakness" in effect:
            mob_effect_code = "target.addEffect(new MobEffectInstance(MobEffects.WEAKNESS, 100, 1), attacker);"

        codigo_java = f"""package {self.base_package}.weapons;

import net.minecraft.tags.BlockTags;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Rarity;
import net.minecraft.world.item.SwordItem;
import net.minecraft.world.item.Tier;
import net.minecraft.world.item.crafting.Ingredient;
import net.neoforged.neoforge.common.SimpleTier;

/**
 * Arma de NeoForge autogenerada por NeoJS: {nombre} ("{display_name}")
 * Daño configurado: {damage} | Durabilidad: {durability} | Velocidad: {attack_speed}
 */
public class {nombre}Weapon extends SwordItem {{
    public static final String REGISTRY_ID = "{short_id}";
    public static final String BASE_DESIGN = "{base_item}";
    public static final String CUSTOM_ASSET_PATH = "{asset_path}";

    public static final Tier WEAPON_TIER = new SimpleTier(
        BlockTags.INCORRECT_FOR_DIAMOND_TOOL,
        {durability},
        9.0F,
        {max(0.0, damage - 4.0):.1f}F,
        15,
        () -> Ingredient.EMPTY
    );

    public {nombre}Weapon() {{
        super(
            WEAPON_TIER,
            new Item.Properties()
                .rarity(Rarity.EPIC){fire_chain}
                .attributes(SwordItem.createAttributes(WEAPON_TIER, 3, {attack_speed:.1f}F))
        );
    }}

    @Override
    public boolean hurtEnemy(ItemStack stack, LivingEntity target, LivingEntity attacker) {{
        {mob_effect_code}
        return super.hurtEnemy(stack, target, attacker);
    }}
}}
"""
        self.archivos_salida[f"weapons/{nombre}Weapon.java"] = codigo_java
        self._generar_modelo_item_json(short_id, base_item, is_handheld=True)
        self.traducciones[f"item.{self.mod_id}.{short_id}"] = display_name
        self.weapons_generadas.append({
            "class_name": f"{nombre}Weapon",
            "const_name": const_name,
            "short_id": short_id,
            "display_name": display_name
        })

    # ======================================================
    # CREACIÓN DE RECETAS DE CRAFTEO (NEOFORGE 1.21 JSON)
    # ======================================================
    def visitRecipeDecl(self, ctx: NeoJSParser.RecipeDeclContext):
        nombre = ctx.ID().getText()
        short_id = nombre.lower()
        attrs = self.visit(ctx.attrList())

        result_raw = attrs.get("result", ("ID", nombre))[1]
        result_id = result_raw if ":" in result_raw else f"{self.mod_id}:{result_raw.lower()}"
        amount = int(attrs.get("amount", ("NUMBER", 1))[1])
        ingredients_str = attrs.get("ingredients", ("STRING", "2x LingoteTitanio + 1x minecraft:stick"))[1]

        partes = [p.strip() for p in ingredients_str.split("+")]
        mat_principal = f"{self.mod_id}:lingotetitanio"
        mat_mango = "minecraft:stick"
        if len(partes) >= 1:
            tok = partes[0].split()[-1]
            mat_principal = tok if ":" in tok else f"{self.mod_id}:{tok.lower()}"
        if len(partes) >= 2:
            tok2 = partes[1].split()[-1]
            mat_mango = tok2 if ":" in tok2 else f"{self.mod_id}:{tok2.lower()}"

        recipe_json = {
            "type": "minecraft:crafting_shaped",
            "category": "equipment",
            "pattern": [
                "M",
                "M",
                "S"
            ],
            "key": {
                "M": {"item": mat_principal},
                "S": {"item": mat_mango}
            },
            "result": {
                "id": result_id,
                "count": amount
            }
        }
        self.archivos_salida[f"resources/data/{self.mod_id}/recipe/{short_id}.json"] = json.dumps(recipe_json, indent=2)
        self.recipes_generadas.append({
            "name": nombre,
            "short_id": short_id,
            "result_id": result_id,
            "ingredients": ingredients_str
        })

    # ==========================================
    # CREACIÓN DE MOBS (NEOFORGE ENTITIES)
    # ==========================================
    def visitMobDecl(self, ctx: NeoJSParser.MobDeclContext):
        nombre = ctx.ID().getText()
        short_id = nombre.lower()
        const_name = nombre.upper()
        egg_short_id = f"{short_id}_spawn_egg"
        attrs = self.visit(ctx.attrList())

        display_name = attrs.get("name", ("STRING", nombre))[1]
        behavior = attrs.get("behavior", ("STRING", "aggressive"))[1].lower()
        base_model = attrs.get("base_model", ("ID", "minecraft:zombie" if behavior == "aggressive" else "minecraft:wandering_trader"))[1]
        asset_path = attrs.get("asset_path", ("STRING", "minecraft:textures/entity/zombie/zombie.png"))[1]
        hitbox_w = float(attrs.get("hitbox_w", ("NUMBER", 0.6))[1])
        hitbox_h = float(attrs.get("hitbox_h", ("NUMBER", 1.95))[1])
        scale = float(attrs.get("scale", ("NUMBER", 1.0))[1])
        hp = float(attrs.get("hp", ("NUMBER", 40.0))[1])
        damage = float(attrs.get("damage", ("NUMBER", 8.0))[1])
        defense = float(attrs.get("defense", ("NUMBER", attrs.get("armor", ("NUMBER", 4.0))[1]))[1])

        is_aggressive = (behavior == "aggressive")
        parent_class = "Zombie" if is_aggressive else "WanderingTrader"
        parent_import = "net.minecraft.world.entity.monster.Zombie" if is_aggressive else "net.minecraft.world.entity.npc.WanderingTrader"
        mob_category = "MobCategory.MONSTER" if is_aggressive else "MobCategory.CREATURE"
        egg_bg_color = "0x2B3A4A" if is_aggressive else "0x3E6B89"
        egg_spot_color = "0x00E5FF" if is_aggressive else "0xFFD700"
        default_vanilla_tex = "minecraft:textures/entity/zombie/zombie.png" if is_aggressive else "minecraft:textures/entity/wandering_trader.png"

        codigo_java = f"""package {self.base_package}.mobs;

import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.AttributeSupplier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import {parent_import};
import net.minecraft.world.level.Level;

/**
 * Entidad Mob de NeoForge autogenerada por NeoJS: {nombre} ("{display_name}")
 * Comportamiento: {behavior} | Modelo Base: {base_model}
 * Dimensiones Hitbox: {hitbox_w}F x {hitbox_h}F (Escala: {scale}F)
 */
public class {nombre}Entity extends {parent_class} {{
    public static final String REGISTRY_ID = "{short_id}";
    public static final String EGG_REGISTRY_ID = "{egg_short_id}";
    public static final float HITBOX_WIDTH = {hitbox_w:.2f}F;
    public static final float HITBOX_HEIGHT = {hitbox_h:.2f}F;
    public static final float VISUAL_SCALE = {scale:.2f}F;

    public static final ResourceLocation DEFAULT_VANILLA_SKIN = ResourceLocation.parse("{default_vanilla_tex}");
    public static final ResourceLocation CUSTOM_SKIN_TEXTURE = ResourceLocation.parse("{asset_path}");

    public {nombre}Entity(EntityType<? extends {parent_class}> type, Level level) {{
        super(type, level);
    }}

    public static AttributeSupplier.Builder createAttributes() {{
        return {parent_class}.createAttributes()
            .add(Attributes.MAX_HEALTH, {hp:.1f}D)
            .add(Attributes.ATTACK_DAMAGE, {damage:.1f}D)
            .add(Attributes.ARMOR, {defense:.1f}D);
    }}
}}
"""
        self.archivos_salida[f"mobs/{nombre}Entity.java"] = codigo_java

        egg_model = {"parent": "minecraft:item/template_spawn_egg"}
        self.archivos_salida[f"resources/assets/{self.mod_id}/models/item/{egg_short_id}.json"] = json.dumps(egg_model, indent=2)
        self.traducciones[f"entity.{self.mod_id}.{short_id}"] = display_name
        self.traducciones[f"item.{self.mod_id}.{egg_short_id}"] = f"Huevo de {display_name}"

        self.mobs_generados.append({
            "class_name": f"{nombre}Entity",
            "const_name": const_name,
            "short_id": short_id,
            "egg_short_id": egg_short_id,
            "display_name": display_name,
            "hitbox_w": hitbox_w,
            "hitbox_h": hitbox_h,
            "mob_category": mob_category,
            "egg_bg": egg_bg_color,
            "egg_fg": egg_spot_color
        })

    # ==========================================
    # MODIFICACIÓN DE ESTADÍSTICAS VANILLA
    # ==========================================
    def visitModifyDecl(self, ctx: NeoJSParser.ModifyDeclContext):
        kind = "mob" if ctx.TK_MOB() else "item"
        target = ctx.ID().getText()
        attrs = self.visit(ctx.attrList())
        if kind == "item":
            self.mod_items.append({"target": target, "attrs": attrs})
        else:
            self.mod_mobs.append({"target": target, "attrs": attrs})

    def visitAttrList(self, ctx: NeoJSParser.AttrListContext):
        atributos = {}
        for attr_ctx in ctx.attr():
            k, v = self.visit(attr_ctx)
            atributos[k] = v
        return atributos

    def visitAttr(self, ctx: NeoJSParser.AttrContext):
        return ctx.ID().getText(), self.visit(ctx.value())

    def visitValue(self, ctx: NeoJSParser.ValueContext):
        if ctx.NUMBER():
            return ("NUMBER", float(ctx.NUMBER().getText()))
        elif ctx.STRING():
            return ("STRING", ctx.STRING().getText()[1:-1])
        elif ctx.PERCENTAGE():
            return ("PERCENTAGE", float(ctx.PERCENTAGE().getText().replace("%", "")))
        elif ctx.TRUE() or ctx.FALSE():
            return ("BOOLEAN", ctx.getText() == "true")
        return ("ID", ctx.getText())

    # ================================
    # ENSAMBLAJE DE NEOFORGE 
    # ================================
    def finalizar(self):
        lang_json = json.dumps(self.traducciones, indent=2, ensure_ascii=False)
        self.archivos_salida[f"resources/assets/{self.mod_id}/lang/en_us.json"] = lang_json
        self.archivos_salida[f"resources/assets/{self.mod_id}/lang/es_es.json"] = lang_json

        bloques_if_mobs = []
        for m in self.mod_mobs:
            target = m["target"]
            a = m["attrs"]
            hp = float(a.get("hp", ("NUMBER", 20.0))[1])
            dmg = float(a.get("damage", ("NUMBER", 3.0))[1])
            armor = float(a.get("armor", ("NUMBER", a.get("defense", ("NUMBER", 2.0))[1]))[1])
            bloques_if_mobs.append(f"""        if (entityId.equals("{target}")) {{
            if (living.getAttribute(Attributes.MAX_HEALTH) != null) {{
                living.getAttribute(Attributes.MAX_HEALTH).setBaseValue({hp:.1f}D);
                living.setHealth({hp:.1f}F);
            }}
            if (living.getAttribute(Attributes.ATTACK_DAMAGE) != null) {{
                living.getAttribute(Attributes.ATTACK_DAMAGE).setBaseValue({dmg:.1f}D);
            }}
            if (living.getAttribute(Attributes.ARMOR) != null) {{
                living.getAttribute(Attributes.ARMOR).setBaseValue({armor:.1f}D);
            }}
        }}""")

        cuerpo_if_mobs = "\n".join(bloques_if_mobs) if bloques_if_mobs else "        // Sin modificaciones de mobs vanilla"

        codigo_eventos = f"""package {self.base_package}.events;

import {self.base_package}.NeoJSMod;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.entity.EntityJoinLevelEvent;

/**
 * Manejador de eventos de NeoForge autogenerado por NeoJS.
 * Aplica los bloques 'modify mob' sobre entidades base de Minecraft cuando entran al mundo.
 */
@EventBusSubscriber(modid = NeoJSMod.MOD_ID)
public class VanillaOverridesHandler {{

    @SubscribeEvent
    public static void onEntityJoinLevel(EntityJoinLevelEvent event) {{
        if (event.getLevel().isClientSide() || !(event.getEntity() instanceof LivingEntity living)) {{
            return;
        }}
        ResourceLocation key = BuiltInRegistries.ENTITY_TYPE.getKey(living.getType());
        String entityId = key.toString();

{cuerpo_if_mobs}
    }}
}}
"""
        self.archivos_salida["events/VanillaOverridesHandler.java"] = codigo_eventos

        imports_extra = []
        reg_items_lines = []
        reg_entities_lines = []
        reg_eggs_lines = []
        tab_accept_lines = []
        attr_event_lines = []

        for it in self.items_generados:
            imports_extra.append(f"import {self.base_package}.items.{it['class_name']};")
            reg_items_lines.append(
                f'    public static final DeferredItem<Item> {it["const_name"]} = ITEMS.registerItem("{it["short_id"]}", props -> new {it["class_name"]}());'
            )
            tab_accept_lines.append(f"                output.accept({it['const_name']}.get());")

        for wp in self.weapons_generadas:
            imports_extra.append(f"import {self.base_package}.weapons.{wp['class_name']};")
            reg_items_lines.append(
                f'    public static final DeferredItem<Item> {wp["const_name"]} = ITEMS.registerItem("{wp["short_id"]}", props -> new {wp["class_name"]}());'
            )
            tab_accept_lines.append(f"                output.accept({wp['const_name']}.get());")

        for mb in self.mobs_generados:
            imports_extra.append(f"import {self.base_package}.mobs.{mb['class_name']};")
            reg_entities_lines.append(f"""    public static final DeferredHolder<EntityType<?>, EntityType<{mb['class_name']}>> {mb['const_name']} =
        ENTITY_TYPES.register("{mb['short_id']}", () -> EntityType.Builder.of({mb['class_name']}::new, {mb['mob_category']})
            .sized({mb['hitbox_w']:.2f}F, {mb['hitbox_h']:.2f}F)
            .build("{mb['short_id']}"));""")
            reg_eggs_lines.append(f"""    public static final DeferredItem<Item> {mb['const_name']}_SPAWN_EGG =
        ITEMS.register("{mb['egg_short_id']}", () -> new DeferredSpawnEggItem({mb['const_name']}, {mb['egg_bg']}, {mb['egg_fg']}, new Item.Properties()));""")
            tab_accept_lines.append(f"                output.accept({mb['const_name']}_SPAWN_EGG.get());")
            attr_event_lines.append(f"        event.put({mb['const_name']}.get(), {mb['class_name']}.createAttributes().build());")

        icono_tab_const = (
            self.items_generados[0]["const_name"] if self.items_generados
            else (self.weapons_generadas[0]["const_name"] if self.weapons_generadas else None)
        )
        icono_expr = f"new ItemStack({icono_tab_const}.get())" if icono_tab_const else "new ItemStack(net.minecraft.world.item.Items.DIAMOND)"

        codigo_mod_principal = f"""package {self.base_package};

{chr(10).join(imports_extra)}
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MobCategory;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import net.neoforged.neoforge.common.DeferredSpawnEggItem;
import net.neoforged.neoforge.event.entity.EntityAttributeCreationEvent;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredItem;
import net.neoforged.neoforge.registries.DeferredRegister;

/**
 * Clase Principal de Minecraft NeoForge autogenerada por el compilador NeoJS.
 */
@Mod(NeoJSMod.MOD_ID)
public class NeoJSMod {{
    public static final String MOD_ID = "{self.mod_id}";

    public static final DeferredRegister.Items ITEMS = DeferredRegister.createItems(MOD_ID);
    public static final DeferredRegister<EntityType<?>> ENTITY_TYPES = DeferredRegister.create(Registries.ENTITY_TYPE, MOD_ID);
    public static final DeferredRegister<CreativeModeTab> CREATIVE_TABS = DeferredRegister.create(Registries.CREATIVE_MODE_TAB, MOD_ID);

    // --- REGISTRO DE ÍTEMS Y ARMAS ---
{chr(10).join(reg_items_lines)}

    // --- REGISTRO DE MOBS Y HUEVOS GENERADORES ---
{chr(10).join(reg_entities_lines)}

{chr(10).join(reg_eggs_lines)}

    // --- PESTAÑA PROPIA EN EL INVENTARIO CREATIVO ---
    public static final DeferredHolder<CreativeModeTab, CreativeModeTab> NEOJS_TAB = CREATIVE_TABS.register("neojs_tab",
        () -> CreativeModeTab.builder()
            .title(Component.translatable("itemGroup." + MOD_ID + ".neojs_tab"))
            .icon(() -> {icono_expr})
            .displayItems((params, output) -> {{
{chr(10).join(tab_accept_lines)}
            }})
            .build()
    );

    public NeoJSMod(IEventBus modEventBus) {{
        ITEMS.register(modEventBus);
        ENTITY_TYPES.register(modEventBus);
        CREATIVE_TABS.register(modEventBus);
        modEventBus.addListener(this::registerEntityAttributes);
    }}

    private void registerEntityAttributes(EntityAttributeCreationEvent event) {{
{chr(10).join(attr_event_lines)}
    }}
}}
"""
        self.archivos_salida["NeoJSMod.java"] = codigo_mod_principal

    def emitir(self, carpeta_salida="salida_neoforge"):
        resumen_consola = []
        for ruta_relativa, contenido in self.archivos_salida.items():
            ruta_completa = os.path.join(carpeta_salida, ruta_relativa)
            os.makedirs(os.path.dirname(ruta_completa), exist_ok=True)
            with open(ruta_completa, "w", encoding="utf-8") as f:
                f.write(contenido)
            if ruta_relativa.endswith(".java") or "/recipe/" in ruta_relativa:
                resumen_consola.append(
                    f"// ==========================================\n// ARCHIVO GENERADO: {ruta_completa}\n// ==========================================\n{contenido}"
                )
        return "\n".join(resumen_consola)