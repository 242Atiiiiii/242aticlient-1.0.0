package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.network.chat.Component;

public class Module {
    public String name;
    public String description;
    public Category category;
    public boolean toggled = false;
    public int key = -1;
    public int keyCode = -1;

    public Module(String name, String description, Category category) {
        this.name = name;
        this.description = description;
        this.category = category;
    }

    public void onEnable() {}
    public void onDisable() {}
    public void onTick(Minecraft client) {}
    public void onKeyPress(int keyCode) {}

    public void toggle() {
        this.toggled = !this.toggled;
        if (this.toggled) {
            onEnable();
            if (Minecraft.getInstance().player != null) {
                Minecraft.getInstance().player.displayClientMessage(Component.literal("§a[+] §f" + name + " §7açıldı"), false);
            }
        } else {
            onDisable();
            if (Minecraft.getInstance().player != null) {
                Minecraft.getInstance().player.displayClientMessage(Component.literal("§c[-] §f" + name + " §7kapatıldı"), false);
            }
        }
        ConfigManager.saveConfig();
    }

    public enum Category {
        COMBAT("Combat", 0xFF5555),
        MOVEMENT("Movement", 0x55FF55),
        RENDER("Render", 0x5555FF),
        PLAYER("Player", 0xFFFF55),
        MISC("Misc", 0xFF55FF);

        public String name;
        public int color;

        Category(String name, int color) {
            this.name = name;
            this.color = color;
        }
    }
}