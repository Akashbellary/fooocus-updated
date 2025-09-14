# Getting Started with AI Influencer Creation

Welcome to the world of hyper-realistic AI influencer generation! This guide will help you create digital personas that are virtually indistinguishable from real people.

## What You'll Create

AI influencers are digital personas designed to look like real people but don't actually exist. They can be used for:
- Social media marketing
- Brand representation
- Content creation
- Entertainment
- Research purposes

## Quick Start Guide

### 1. Install Requirements

Make sure you have Fooocus installed with all dependencies. If not, follow the installation guide in the main repository.

### 2. Download Essential Models

Run this command to automatically download all required models:
```bash
python extras/download_influencer_models.py
```

This will download:
- realisticStockPhoto_v20.safetensors (base model)
- SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors (LoRA)
- Supporting enhancement models

### 3. Generate Your First Influencer

Run the influencer generator:
```bash
python extras/influencer_generator.py
```

This creates sample prompts and saves them to `sample_influencers.json`.

### 4. Launch with Optimal Settings

Start Fooocus with our custom preset:
```bash
python launch.py --preset influencer
```

## How It Works

Our system uses advanced techniques to maximize realism:

### Prompt Engineering

We automatically generate comprehensive prompts that include:
- Physical characteristics
- Expressions and poses
- Attire and styling
- Photography equipment
- Lighting conditions
- Quality enhancement keywords

### Optimal Parameters

We've identified the best settings for maximum realism:
- Base Model: realisticStockPhoto_v20.safetensors
- LoRA: SDXL_FILM_PHOTOGRAPHY_STYLE_V1 (0.4 strength)
- Styles: Fooocus Photograph + Fooocus Sharp + sai-photographic
- Performance: Quality mode
- Steps: 60+ (automatically set)
- CFG Scale: 3.5 (balanced creativity and accuracy)

### Negative Prompts

Comprehensive negative prompts prevent unrealistic features:
- Cartoon/anime characteristics
- 3D rendering artifacts
- Low quality issues
- Anatomical abnormalities
- Artificial appearance markers

## Available Influencer Types

1. **Instagram Model** - Fashion and lifestyle content
2. **TikTok Star** - Viral social media personality
3. **Business Executive** - Corporate/professional persona
4. **Fitness Guru** - Health and athletic niche

Each type has optimized prompts and settings for its specific use case.

## For Maximum Realism

Follow these tips for the most convincing results:

1. **Use Quality Mode**: Always generate with Quality performance setting
2. **Increase Steps**: Use 60+ steps for fine detail rendering
3. **Apply Multiple Styles**: Combine complementary styles for layered enhancement
4. **Optimize Resolution**: Use recommended aspect ratios for each platform
5. **Enhance Details**: Use the "Improve Detail" feature on faces
6. **Iterate**: Generate multiple versions and select the best

## Ethical Guidelines

When creating AI influencers, please:
1. Be transparent about their AI-generated nature when required
2. Respect likeness rights and intellectual property
3. Avoid deceptive representation
4. Follow platform policies and terms of service
5. Consider the societal impact of synthetic personas

## Next Steps

1. Read `extras/INFLUENCER_GENERATION_GUIDE.md` for advanced techniques
2. Experiment with different influencer types
3. Customize prompts for your specific needs
4. Create consistent character portfolios
5. Explore batch generation for multiple personas

## Support

If you encounter issues:
1. Check the main Fooocus documentation
2. Review the detailed guides in the `extras/` folder
3. Search community forums for similar questions
4. Report bugs to the main repository

Happy influencer creating!