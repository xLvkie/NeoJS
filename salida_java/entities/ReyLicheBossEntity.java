package com.NeoJS.generated.entities;

import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.AttributeSupplier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.level.Level;

/**
 * Entidad de Jefe autogenerada por NeoJS para NeoForge: ReyLiche
 */
public class ReyLicheBossEntity extends Monster {

    public ReyLicheBossEntity(EntityType<? extends Monster> type, Level level) {
        super(type, level);
    }

    public static AttributeSupplier.Builder createAttributes() {
        return Monster.createMonsterAttributes()
                .add(Attributes.MAX_HEALTH, 1500.0D)
                .add(Attributes.ATTACK_DAMAGE, 30.0D)
                .add(Attributes.ARMOR, 20.0D);
    }

    @Override
    public void tick() {
        super.tick();
        // Condición de fase configurada en NeoJS: hp < 50.0
        if (this.getHealth() < (this.getMaxHealth() * 0.5f)) {
            triggerSpecialAbility("invocar_esqueletos");
        }
    }

    private void triggerSpecialAbility(String abilityName) {
        // Lógica de ejecución para la habilidad: invocar_esqueletos
    }
}
