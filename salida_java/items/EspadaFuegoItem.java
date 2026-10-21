package com.NeoJS.generated.items;

import net.minecraft.world.item.SwordItem;
import net.minecraft.world.item.Tiers;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;

/**
 * Ítem autogenerado por NeoJS para NeoForge: EspadaFuego ("Hoja Ignea")
 */
public class EspadaFuegoItem extends SwordItem {
    public EspadaFuegoItem() {
        super(Tiers.DIAMOND, new Item.Properties()
                .durability(1200).fireResistant()
                .attributes(SwordItem.createAttributes(Tiers.DIAMOND, 45, -2.4f)));
    }

}
