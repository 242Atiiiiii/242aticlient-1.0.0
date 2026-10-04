package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.world.phys.Vec3;

public class Speed extends Module {
    private int jumpDelay = 0;

    public Speed(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onTick(Minecraft client) {
        if (client.player == null) return;

        boolean moving = client.options.keyUp.isDown() ||
                        client.options.keyDown.isDown() ||
                        client.options.keyLeft.isDown() ||
                        client.options.keyRight.isDown();

        if (!moving) {
            jumpDelay = 0;
            return;
        }

        if (jumpDelay > 0) {
            jumpDelay--;
        }

        if (client.player.onGround()) {
            client.player.jump();
            Vec3 vel = client.player.getDeltaMovement();
            client.player.setDeltaMovement(vel.x * 1.2, 0.42, vel.z * 1.2);
            jumpDelay = 3;
        } else if (jumpDelay == 0) {
            Vec3 vel = client.player.getDeltaMovement();
            client.player.setDeltaMovement(vel.x * 1.05, vel.y, vel.z * 1.05);
        }
    }
}