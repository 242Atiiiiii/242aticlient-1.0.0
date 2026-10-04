package com._242aticlient;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.client.event.lifecycle.v1.ClientTickEvents;
import net.fabricmc.fabric.api.client.keybinding.v1.KeyMappingHelper;
import net.minecraft.client.KeyMapping;
import net.minecraft.client.Minecraft;
import net.minecraft.network.chat.Component;
import org.lwjgl.glfw.GLFW;

public class Main implements ModInitializer {
    public static final String PREFIX = "§b[242Aticlient_] §f";
    public static KeyMapping guiKey;

    @Override
    public void onInitialize() {
        System.out.println("[242Aticlient_] Başlatıldı!");
        ModuleManager.init();
        EventManager.register();
        ConfigManager.loadConfig();
        registerGuiKey();
        registerCommands();
    }

    private void registerGuiKey() {
        guiKey = KeyMappingHelper.registerKeyBinding(new KeyMapping(
            "key.242aticlient.gui",
            InputUtil.Type.KEYSYM,
            GLFW.GLFW_KEY_RIGHT_SHIFT,
            "category.242aticlient"
        ));
    }

    private void registerCommands() {
        ClientTickEvents.END_CLIENT_TICK.register(client -> {
            while (guiKey.consumeClick()) {
                if (client.screen instanceof ClickGUI) {
                    client.setScreen(null);
                } else {
                    client.setScreen(new ClickGUI());
                }
            }
        });
    }
}