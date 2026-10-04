package com._242aticlient;

import net.fabricmc.fabric.api.client.event.lifecycle.v1.ClientTickEvents;
import net.minecraft.client.Minecraft;
import net.minecraft.client.KeyMapping;
import org.lwjgl.glfw.GLFW;

public class EventManager {
    public static void register() {
        ClientTickEvents.END_CLIENT_TICK.register(client -> {
            if (client.player == null) return;

            for (Module m : ModuleManager.modules) {
                if (m.toggled) m.onTick(client);
            }

            for (Module m : ModuleManager.modules) {
                if (m.key != -1) {
                    boolean pressed = KeyMapping.isDown(m.key);
                    if (pressed && m.keyCode != m.key) {
                        m.toggle();
                        m.keyCode = m.key;
                    } else if (!pressed) {
                        m.keyCode = -1;
                    }
                }
            }
        });
    }
}