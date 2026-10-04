package com._242aticlient;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import net.minecraft.client.Minecraft;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ConfigManager {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final Path CONFIG_PATH = Paths.get("config/242aticlient.json");

    public static void saveConfig() {
        try {
            JsonObject config = new JsonObject();
            JsonObject modules = new JsonObject();
            for (Module m : ModuleManager.modules) {
                modules.addProperty(m.name, m.toggled);
            }
            config.add("modules", modules);

            JsonObject gui = new JsonObject();
            if (Minecraft.getInstance().screen instanceof ClickGUI) {
                ClickGUI clickGUI = (ClickGUI) Minecraft.getInstance().screen;
                gui.addProperty("x", clickGUI.x);
                gui.addProperty("y", clickGUI.y);
            }
            config.add("gui", gui);

            String json = GSON.toJson(config);
            Files.write(CONFIG_PATH, json.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void loadConfig() {
        try {
            if (!Files.exists(CONFIG_PATH)) return;
            String json = new String(Files.readAllBytes(CONFIG_PATH));
            JsonObject config = GSON.fromJson(json, JsonObject.class);

            if (config.has("modules")) {
                JsonObject modules = config.getAsJsonObject("modules");
                for (Module m : ModuleManager.modules) {
                    if (modules.has(m.name)) {
                        boolean state = modules.get(m.name).getAsBoolean();
                        if (state && !m.toggled) m.toggle();
                        else if (!state && m.toggled) m.toggle();
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}