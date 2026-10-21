package com.NeoJS.generated;

import com.NeoJS.generated.items.*;
import net.minecraft.world.item.Item;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.neoforge.registries.DeferredItem;
import net.neoforged.neoforge.registries.DeferredRegister;

/**
 * Registro central autogenerado por NeoJS Compiler para Minecraft NeoForge
 */
public class NeoJSRegistry {
    public static final DeferredRegister.Items ITEMS = DeferredRegister.createItems("examplemod");

    public static final DeferredItem<Item> ESPADAFUEGO = ITEMS.register("espadafuego", () -> new EspadaFuegoItem());

    public static void register(IEventBus eventBus) {
        ITEMS.register(eventBus);
    }
}
