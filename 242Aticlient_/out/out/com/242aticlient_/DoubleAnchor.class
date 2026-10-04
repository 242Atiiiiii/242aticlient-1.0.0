package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.InteractionHand;
import net.minecraft.core.BlockPos;
import net.minecraft.world.phys.Vec3;

public class DoubleAnchor extends Module {
    private int tickCounter = 0;
    private int phase = 0;
    private Player target;
    private BlockPos firstAnchorPos;
    private BlockPos secondAnchorPos;

    public DoubleAnchor(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onTick(Minecraft client) {
        if (client.player == null || client.level == null) return;

        target = getNearestPlayer(client);
        if (target == null) {
            phase = 0;
            return;
        }

        double distance = client.player.distanceTo(target);

        if (distance >= 2.0 && distance <= 5.0) {
            tickCounter++;
            switch (phase) {
                case 0:
                    prepareAnchors(client);
                    phase = 1;
                    break;
                case 1:
                    if (tickCounter % 3 == 0) {
                        triggerFirstAnchor(client);
                        phase = 2;
                    }
                    break;
                case 2:
                    if (tickCounter % 3 == 0) {
                        triggerSecondAnchor(client);
                        phase = 0;
                    }
                    break;
            }
        } else {
            tickCounter = 0;
            phase = 0;
        }
    }

    private void prepareAnchors(Minecraft client) {
        BlockPos targetBlock = target.blockPosition();
        firstAnchorPos = new BlockPos(targetBlock.getX() + 2, targetBlock.getY(), targetBlock.getZ());
        secondAnchorPos = new BlockPos(targetBlock.getX() - 2, targetBlock.getY(), targetBlock.getZ());
        placeAnchor(client, firstAnchorPos);
        placeAnchor(client, secondAnchorPos);
    }

    private void triggerFirstAnchor(Minecraft client) {
        if (firstAnchorPos != null) {
            Vec3 lookPos = new Vec3(firstAnchorPos.getX() + 0.5, firstAnchorPos.getY() + 1, firstAnchorPos.getZ() + 0.5);
            client.player.lookAt(lookPos);
            client.player.useItem(InteractionHand.MAIN_HAND);
            client.player.swing(InteractionHand.MAIN_HAND);

            Vec3 towardTarget = target.getPosition().subtract(client.player.getPosition()).normalize().multiply(0.3);
            client.player.setDeltaMovement(towardTarget.x, 0.2, towardTarget.z);
            client.player.lookAt(target.getPosition());
        }
    }

    private void triggerSecondAnchor(Minecraft client) {
        if (secondAnchorPos != null) {
            Vec3 lookPos = new Vec3(secondAnchorPos.getX() + 0.5, secondAnchorPos.getY() + 1, secondAnchorPos.getZ() + 0.5);
            client.player.lookAt(lookPos);
            client.player.useItem(InteractionHand.MAIN_HAND);
            client.player.swing(InteractionHand.MAIN_HAND);

            Vec3 away = client.player.getPosition().subtract(target.getPosition()).normalize().multiply(0.5);
            client.player.setDeltaMovement(away.x, 0.3, away.z);
            prepareAnchors(client);
        }
    }

    private void placeAnchor(Minecraft client, BlockPos pos) {
        BlockPos obsidianPos = pos.below();
        if (client.level.getBlockState(obsidianPos).getBlock().toString().contains("obsidian")) {
            Vec3 lookPos = new Vec3(pos.getX() + 0.5, pos.getY(), pos.getZ() + 0.5);
            client.player.lookAt(lookPos);
            client.player.useItem(InteractionHand.MAIN_HAND);
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