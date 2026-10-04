package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.phys.Vec3;

public class AnchorMacro extends Module {
    private int tickCounter = 0;

    public AnchorMacro(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onTick(Minecraft client) {
        if (client.player == null || client.level == null) return;

        Player target = getNearestPlayer(client);
        if (target == null) return;

        double distance = client.player.distanceTo(target);

        if (distance >= 3.0 && distance <= 6.0) {
            tickCounter++;
            if (tickCounter % 5 == 0) {
                client.player.lookAt(target.getPosition());
                client.player.useItem(InteractionHand.MAIN_HAND);
                client.player.swing(InteractionHand.MAIN_HAND);

                if (distance < 4.0) {
                    Vec3 away = client.player.getPosition().subtract(target.getPosition()).normalize().multiply(0.5);
                    client.player.setDeltaMovement(away.x, 0.3, away.z);
                }
            }
        } else {
            tickCounter = 0;
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