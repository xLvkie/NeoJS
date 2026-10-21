package com.NeoJS.generated.loot;

/**
 * Tabla de botín autogenerada por NeoJS: CofreReyLiche
 */
public class CofreReyLicheLootHandler {

    public static void rollLoot() {
        // Drop: EspadaFuego (25.0%)
        if (Math.random() <= 0.25) {
            int amount = 1 + (int)(Math.random() * (1 - 1 + 1));
            spawnDrop("EspadaFuego", amount);
        }

        // Drop: LingoteOro (75.0%)
        if (Math.random() <= 0.75) {
            int amount = 3 + (int)(Math.random() * (10 - 3 + 1));
            spawnDrop("LingoteOro", amount);
        }
    }

    private static void spawnDrop(String itemId, int count) {
        System.out.println("Spawning drop: " + count + "x " + itemId);
    }
}
