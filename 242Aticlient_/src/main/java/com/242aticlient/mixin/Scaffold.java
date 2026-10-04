package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.world.phys.Vec3;

public class Scaffold extends Module {
    public Scaffold(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onTick(Minecraft client) {
        if (client.player == null || client.level == null) return;
        if (!client.options.keyUp.isDown()) return;

        BlockPos below = client.player.blockPosition().below();

        if (client.level.getBlockState(below).isAir()) {
            ItemStack mainHand = client.player.getMainHandItem();
            if (mainHand.getItem() instanceof BlockItem) {
                Vec3 hitVec = new Vec3(below.getX() + 0.5, below.getY() + 0.5, below.getZ() + 0.5);
                BlockHitResult hitResult = new BlockHitResult(hitVec, Direction.UP, below, false);
                client.player.useItem(InteractionHand.MAIN_HAND);
                client.player.swing(InteractionHand.MAIN_HAND);
            }
        }
    }
}