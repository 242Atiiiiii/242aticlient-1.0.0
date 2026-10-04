package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Items;
import net.minecraft.world.InteractionHand;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.Vec3;

public class AutoCrystal extends Module {
    private int delay = 0;
    private static final int MAX_DELAY = 2;

    public AutoCrystal(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onTick(Minecraft client) {
        if (client.player == null || client.level == null) return;
        if (delay > 0) { delay--; return; }

        Player target = getNearestPlayer(client);
        if (target == null) return;

        double distance = client.player.distanceTo(target);
        if (distance > 6.0) return;

        if (client.player.getMainHandItem().getItem() == Items.END_CRYSTAL) {
            BlockPos targetPos = target.blockPosition();
            BlockPos placePos = findCrystalPlacePosition(client, targetPos);

            if (placePos != null) {
                Vec3 lookPos = new Vec3(placePos.getX() + 0.5, placePos.getY() + 0.5, placePos.getZ() + 0.5);
                client.player.lookAt(lookPos);
                client.player.useItem(InteractionHand.MAIN_HAND);
                client.player.swing(InteractionHand.MAIN_HAND);
                delay = MAX_DELAY;
            }
        }
    }

    private BlockPos findCrystalPlacePosition(Minecraft client, BlockPos targetPos) {
        for (int dx = -2; dx <= 2; dx++) {
            for (int dz = -2; dz <= 2; dz++) {
                BlockPos checkPos = targetPos.offset(dx, 0, dz);
                if (client.level.getBlockState(checkPos).isAir() &&
                    client.level.getBlockState(checkPos.below()).getBlock() == Blocks.OBSIDIAN) {
                    return checkPos;
                }
            }
        }
        return null;
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