package com._242aticlient;

import net.minecraft.client.Minecraft;

public class Fly extends Module {
    public Fly(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onEnable() {
        if (Minecraft.getInstance().player != null) {
            Minecraft.getInstance().player.getAbilities().flying = true;
        }
    }

    @Override
    public void onDisable() {
        if (Minecraft.getInstance().player != null) {
            Minecraft.getInstance().player.getAbilities().flying = false;
        }
    }

    @Override
    public void onTick(Minecraft client) {
        if (client.player == null) return;
        client.player.getAbilities().flying = true;
        client.player.getAbilities().setFlyingSpeed(0.1f);
    }
}