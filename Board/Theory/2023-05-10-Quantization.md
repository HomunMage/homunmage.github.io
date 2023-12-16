---
layout: post
title:  "Quantization"
date:   2023-05-10 10:00:00 +0800
categories: [Theory]
---

就如同我之前提的[人人使用老師-學生模型](../Physics/2023-04-10-H100.md)⁠ 類似alphago出paper之後 會有開源的source code和社群訓練的網路參數  
最近也越來越多local host的語言模型  也有人公開一定程度訓練的參數  
比如minigpt4(Vicuna) 就是用老師-學生模型學出來的  

當然參數越多效果越好 隨之而來的就是家用也會往快速擴增gpu ram的方向發展

另外同時還有另一個問題可以談  目前的AI都是先管效果不管大小

但是AI其實有壓縮的手段 (quantization) 想要了解的人可以看[AI模型壓縮技術-量化(Quantization)](https://chih-sheng-huang821.medium.com/ai模型壓縮技術-量化-quantization-966505128365)


經過多種quantization壓縮後 一般來說可以剩1/10大小  
也就是如果需要10張顯卡的網路  quantization後一張顯卡就可以跑了