package com._242aticlient.mixin;

import com._242aticlient.XRay;
import net.minecraft.client.renderer.block.BlockRenderDispatcher;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.BlockGetter;
import com.mojang.blaze3d.vertex.PoseStack;
import net.minecraft.client.renderer.MultiBufferSource;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(BlockRenderDispatcher.class)
public class XRayMixin {
    @Inject(method = "renderBatched", at = @At("HEAD"), cancellable = true)
    private void onRenderBlock(BlockState state, BlockPos pos, BlockGetter world, PoseStack poseStack,
                               MultiBufferSource buffer, int packedLight, int overlay, CallbackInfo ci) {
        if (XRay.isActive() && !XRay.shouldRender(state.getBlock())) {
            ci.cancel();
        }
    }
}