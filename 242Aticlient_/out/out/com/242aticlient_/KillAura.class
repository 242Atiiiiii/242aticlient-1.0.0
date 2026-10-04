package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.InteractionHand;

public class KillAura extends Module {
    public KillAura(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onTick(Minecraft client) {
        if (client.player == null || client.level == null) return;

        Player target = getNearestPlayer(client);
        if (target == null) return;

        double distance = client.player.distanceTo(target);
        if (distance <= 4.5) {
            client.player.lookAt(target.getPosition());
            client.player.attack(target);
            client.player.swing(InteractionHand.MAIN_HAND);
        }
    }

    private Player getNearestPlayer(Minecraft client) {
        Player nearest = null;
        double nearestDist = Double.MAX_VALUE;

        for (Entity entity : client.level.entitiesForRendering()) {
            if (entity instanceof Player player) {
                if (player == client.player) continue;
                if (player.isDead()) continue;

                double dist = client.player.distanceTo(player);
                if (dist < nearestDist) {
                    nearestDist = dist;
                    nearest = player;
                }
            }
        }
        return nearest;
    }
}