package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

public class ClickGUI extends Screen {
    public int x, y;
    private static final int WINDOW_WIDTH = 450;
    private static final int WINDOW_HEIGHT = 300;
    private boolean dragging = false;
    private int dragX, dragY;
    private List<CategoryPanel> panels = new ArrayList<>();
    private List<Module> allModules;
    private static final int HEADER_HEIGHT = 30;
    private static final int FOOTER_HEIGHT = 25;

    public ClickGUI() {
        super(Component.literal("242Aticlient_"));
        this.x = (Minecraft.getInstance().getWindow().getGuiScaledWidth() - WINDOW_WIDTH) / 2;
        this.y = (Minecraft.getInstance().getWindow().getGuiScaledHeight() - WINDOW_HEIGHT) / 2;
        this.allModules = ModuleManager.modules;
        initPanels();
    }

    private void initPanels() {
        int panelWidth = 130;
        int panelSpacing = 10;
        int startX = x + 10;

        Module.Category[] categories = Module.Category.values();
        for (int i = 0; i < categories.length; i++) {
            Module.Category cat = categories[i];
            List<Module> categoryModules = ModuleManager.getModulesByCategory(cat);
            if (!categoryModules.isEmpty()) {
                int panelX = startX + i * (panelWidth + panelSpacing);
                CategoryPanel panel = new CategoryPanel(cat, panelX, y + HEADER_HEIGHT, panelWidth, WINDOW_HEIGHT - HEADER_HEIGHT - FOOTER_HEIGHT);
                panel.modules = categoryModules;
                panels.add(panel);
            }
        }
    }

    @Override
    public void render(GuiGraphics context, int mouseX, int mouseY, float delta) {
        context.fill(0, 0, this.width, this.height, new Color(0, 0, 0, 150).getRGB());
        drawWindow(context);
        for (CategoryPanel panel : panels) {
            panel.render(context, mouseX, mouseY);
        }
        if (dragging) {
            x = mouseX - dragX;
            y = mouseY - dragY;
            for (CategoryPanel panel : panels) {
                panel.x = x + 10 + panels.indexOf(panel) * 140;
                panel.y = y + HEADER_HEIGHT;
            }
        }
        super.render(context, mouseX, mouseY, delta);
    }

    private void drawWindow(GuiGraphics context) {
        context.fill(x, y, x + WINDOW_WIDTH, y + WINDOW_HEIGHT, new Color(20, 20, 25, 240).getRGB());
        context.fill(x, y, x + WINDOW_WIDTH, y + HEADER_HEIGHT, new Color(30, 30, 40, 255).getRGB());
        context.drawString(this.font, "§l242Aticlient_", x + 10, y + 10, 0xFFFFFF, false);
        context.fill(x + WINDOW_WIDTH - 30, y + 5, x + WINDOW_WIDTH - 10, y + 25, new Color(200, 50, 50, 200).getRGB());
        context.drawString(this.font, "✕", x + WINDOW_WIDTH - 24, y + 8, 0xFFFFFF, false);
        context.fill(x, y + WINDOW_HEIGHT - FOOTER_HEIGHT, x + WINDOW_WIDTH, y + WINDOW_HEIGHT, new Color(25, 25, 35, 255).getRGB());
        context.drawString(this.font, "§7Right Shift ile kapat", x + 10, y + WINDOW_HEIGHT - 18, 0x888888, false);
        int activeCount = ModuleManager.getActiveCount();
        context.drawString(this.font, "§7Aktif: §a" + activeCount + "§7/" + allModules.size(),
            x + WINDOW_WIDTH - 100, y + WINDOW_HEIGHT - 18, 0x888888, false);
        context.fill(x, y + HEADER_HEIGHT, x + WINDOW_WIDTH, y + HEADER_HEIGHT + 1, new Color(50, 50, 60, 255).getRGB());
        context.fill(x, y + WINDOW_HEIGHT - FOOTER_HEIGHT - 1, x + WINDOW_WIDTH, y + WINDOW_HEIGHT - FOOTER_HEIGHT, new Color(50, 50, 60, 255).getRGB());
    }

    @Override
    public boolean mouseClicked(double mouseX, double mouseY, int button) {
        if (mouseX >= x + WINDOW_WIDTH - 30 && mouseX <= x + WINDOW_WIDTH - 10 &&
            mouseY >= y + 5 && mouseY <= y + 25) {
            this.onClose();
            return true;
        }
        if (mouseX >= x && mouseX <= x + WINDOW_WIDTH && mouseY >= y && mouseY <= y + HEADER_HEIGHT) {
            dragging = true;
            dragX = (int)(mouseX - x);
            dragY = (int)(mouseY - y);
            return true;
        }
        for (CategoryPanel panel : panels) {
            if (panel.mouseClicked(mouseX, mouseY, button)) return true;
        }
        return super.mouseClicked(mouseX, mouseY, button);
    }

    @Override
    public boolean mouseReleased(double mouseX, double mouseY, int button) {
        dragging = false;
        return super.mouseReleased(mouseX, mouseY, button);
    }

    @Override
    public boolean mouseScrolled(double mouseX, double mouseY, double horizontalAmount, double verticalAmount) {
        for (CategoryPanel panel : panels) {
            if (mouseX >= panel.x && mouseX <= panel.x + panel.width) {
                panel.scrollOffset += verticalAmount * 15;
                int maxScroll = Math.max(0, panel.modules.size() * 30 - (panel.height - 30));
                panel.scrollOffset = Math.max(-maxScroll, Math.min(0, panel.scrollOffset));
                break;
            }
        }
        return super.mouseScrolled(mouseX, mouseY, horizontalAmount, verticalAmount);
    }

    @Override
    public boolean isPauseScreen() {
        return false;
    }
}