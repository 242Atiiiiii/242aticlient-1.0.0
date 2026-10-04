package com._242aticlient;

import java.util.ArrayList;
import java.util.List;

public class ModuleManager {
    public static List<Module> modules = new ArrayList<>();

    public static void init() {
        // Combat
        modules.add(new KillAura("KillAura", "Otomatik saldırı", Module.Category.COMBAT));
        modules.add(new AutoCrystal("AutoCrystal", "Otomatik crystal", Module.Category.COMBAT));
        modules.add(new DoubleAnchor("DoubleAnchor", "Çift anchor", Module.Category.COMBAT));
        modules.add(new AnchorMacro("AnchorMacro", "Anchor makro", Module.Category.COMBAT));

        // Movement
        modules.add(new Fly("Fly", "Uçuş modu", Module.Category.MOVEMENT));
        modules.add(new Speed("Speed", "Hız artırma", Module.Category.MOVEMENT));

        // Render
        modules.add(new XRay("XRay", "X-Ray görüş", Module.Category.RENDER));

        // Player
        modules.add(new Scaffold("Scaffold", "Otomatik köprü", Module.Category.PLAYER));

        setKeybinds();
    }

    private static void setKeybinds() {
        if (modules.size() < 8) return;
        modules.get(0).key = 75;  // KillAura - K
        modules.get(1).key = 67;  // AutoCrystal - C
        modules.get(2).key = 71;  // DoubleAnchor - G
        modules.get(3).key = 78;  // AnchorMacro - N
        modules.get(4).key = 70;  // Fly - F
        modules.get(5).key = 86;  // Speed - V
        modules.get(6).key = 88;  // XRay - X
        modules.get(7).key = 66;  // Scaffold - B
    }

    public static Module getModule(String name) {
        for (Module m : modules) {
            if (m.name.equalsIgnoreCase(name)) return m;
        }
        return null;
    }

    public static List<Module> getModulesByCategory(Module.Category category) {
        List<Module> result = new ArrayList<>();
        for (Module m : modules) {
            if (m.category == category) result.add(m);
        }
        return result;
    }

    public static int getActiveCount() {
        int count = 0;
        for (Module m : modules) {
            if (m.toggled) count++;
        }
        return count;
    }
}