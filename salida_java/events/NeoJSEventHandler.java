package com.NeoJS.generated.events;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.entity.living.LivingIncomingDamageEvent;

/**
 * Interceptor de eventos autogenerado por NeoJS Compiler para NeoForge
 */
@EventBusSubscriber(modid = "examplemod")
public class NeoJSEventHandler {

    @SubscribeEvent
    public static void onLivingDamage(LivingIncomingDamageEvent event) {
        if (event.getSource().getEntity() instanceof Player player) {
            ItemStack heldItem = player.getMainHandItem();
            if (heldItem.isEmpty()) return;

            String itemId = BuiltInRegistries.ITEM.getKey(heldItem.getItem()).toString();
            if (itemId.equals("minecraft:diamond_sword")) {
                event.setAmount(18.0f);
                if (Math.random() < 0.25) event.setAmount(event.getAmount() * 1.5f);
            }
        }
    }
}
