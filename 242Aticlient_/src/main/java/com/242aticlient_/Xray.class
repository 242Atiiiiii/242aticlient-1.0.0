package com._242aticlient;

import net.minecraft.client.Minecraft;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class XRay extends Module {
    private static final Set<Block> ORE_BLOCKS = new HashSet<>(Arrays.asList(
        Blocks.DIAMOND_ORE,
        Blocks.DEEPSLATE_DIAMOND_ORE,
        Blocks.IRON_ORE,
        Blocks.DEEPSLATE_IRON_ORE,
        Blocks.GOLD_ORE,
        Blocks.DEEPSLATE_GOLD_ORE,
        Blocks.EMERALD_ORE,
        Blocks.DEEPSLATE_EMERALD_ORE,
        Blocks.REDSTONE_ORE,
        Blocks.DEEPSLATE_REDSTONE_ORE,
        Blocks.LAPIS_ORE,
        Blocks.DEEPSLATE_LAPIS_ORE,
        Blocks.COAL_ORE,
        Blocks.DEEPSLATE_COAL_ORE,
        Blocks.NETHER_QUARTZ_ORE,
        Blocks.NETHER_GOLD_ORE,
        Blocks.ANCIENT_DEBRIS,
        Blocks.COPPER_ORE,
        Blocks.DEEPSLATE_COPPER_ORE
    ));

    public XRay(String name, String description, Category category) {
        super(name, description, category);
    }

    @Override
    public void onEnable() {
        if (Minecraft.getInstance().levelRenderer != null) {
            Minecraft.getInstance().levelRenderer.reload();
        }
    }

    @Override
    public void onDisable() {
        if (Minecraft.getInstance().levelRenderer != null) {
            Minecraft.getInstance().levelRenderer.reload();
        }
    }

    public static boolean shouldRender(Block block) {
        return ORE_BLOCKS.contains(block);
    }

    public static boolean isActive() {
        Module xray = ModuleManager.getModule("XRay");
        return xray != null && xray.toggled;
    }
}