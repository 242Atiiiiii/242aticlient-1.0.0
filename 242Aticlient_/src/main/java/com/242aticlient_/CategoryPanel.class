package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphics;
import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

public class CategoryPanel {
    public int x, y, width, height;
    public Module.Category category;
    public List<Module> modules = new ArrayList<>();
    public float scrollOffset = 0;
    private static final int HEADER_HEIGHT = 25;
    private static final int MODULE_HEIGHT = 28;
    private static final int MODULE_SPACING = 4;

    public CategoryPanel(Module.Category category, int x, int y, int width, int height) {
        this.category = category;
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    public void render(GuiGraphics context, int mouseX, int mouseY) {
        context.fill(x, y, x + width, y + height, new Color(25, 25, 35, 220).getRGB());
        context.fill(x, y, x + width, y + HEADER_HEIGHT, new Color(category.color, 200).getRGB());
        context.drawString(Minecraft.getInstance().font, category.name, x + 8, y + 8, 0xFFFFFF, false);

        int moduleY = y + HEADER_HEIGHT + 5 + (int)scrollOffset;
        context.enableScissor(x + 1, y + HEADER_HEIGHT + 1, x + width - 1, y + height - 1);

        for (Module mod : modules) {
            if (moduleY + MODULE_HEIGHT > y + HEADER_HEIGHT && moduleY < y + height) {
                renderModule(context, mod, mouseX, mouseY, moduleY);
            }
            moduleY += MODULE_HEIGHT + MODULE_SPACING;
        }

        context.disableScissor();

        int totalContentHeight = modules.size() * (MODULE_HEIGHT + MODULE_SPACING);
        if (totalContentHeight > height - HEADER_HEIGHT) {
            int scrollBarHeight = Math.max(20, (height - HEADER_HEIGHT) * (height - HEADER_HEIGHT) / totalContentHeight);
            int scrollBarY = y + HEADER_HEIGHT + (int)((-scrollOffset) * (height - HEADER_HEIGHT - scrollBarHeight) / (totalContentHeight - (height - HEADER_HEIGHT)));
            context.fill(x + width - 5, scrollBarY, x + width - 2, scrollBarY + scrollBarHeight, new Color(150, 150, 200, 100).getRGB());
        }
    }

    private void renderModule(GuiGraphics context, Module mod, int mouseX, int mouseY, int moduleY) {
        int moduleX = x + 5;
        int moduleWidth = width - 10;
        boolean hovered = mouseX >= moduleX && mouseX <= moduleX + moduleWidth &&
                         mouseY >= moduleY && mouseY <= moduleY + MODULE_HEIGHT;

        Color bgColor = mod.toggled ? new Color(category.color, 80) : new Color(45, 45, 55, 120);
        if (hovered) {
            bgColor = new Color(Math.min(255, bgColor.getRed() + 20), Math.min(255, bgColor.getGreen() + 20), Math.min(255, bgColor.getBlue() + 20), bgColor.getAlpha());
        }

        context.fill(moduleX, moduleY, moduleX + moduleWidth, moduleY + MODULE_HEIGHT, bgColor.getRGB());
        context.drawString(Minecraft.getInstance().font, mod.name, moduleX + 8, moduleY + 8, 0xFFFFFF, false);

        if (mod.toggled) {
            context.fill(moduleX, moduleY, moduleX + 3, moduleY + MODULE_HEIGHT, new Color(category.color).getRGB());
        }

        if (mod.key != -1) {
            String keyName = getKeyName(mod.key);
            context.drawString(Minecraft.getInstance().font, keyName, moduleX + moduleWidth - 40, moduleY + 8, 0x888888, false);
        }
    }

    public boolean mouseClicked(double mouseX, double mouseY, int button) {
        if (mouseX >= x && mouseX <= x + width && mouseY >= y && mouseY <= y + height) {
            int moduleY = y + HEADER_HEIGHT + 5 + (int)scrollOffset;
            for (Module mod : modules) {
                if (mouseX >= x + 5 && mouseX <= x + width - 5 && mouseY >= moduleY && mouseY <= moduleY + MODULE_HEIGHT) {
                    mod.toggle();
                    return true;
                }
                moduleY += MODULE_HEIGHT + MODULE_SPACING;
            }
        }
        return false;
    }

    private String getKeyName(int key) {
        switch (key) {
            case 75: return "K";
            case 67: return "C";
            case 71: return "G";
            case 78: return "N";
            case 70: return "F";
            case 86: return "V";
            case 88: return "X";
            case 66: return "B";
            default: return "";
        }
    }
}