# AI Influencer Generator - Quick Start Guide

## Immediate Usage (Command Line)

You can start generating influencer prompts right away using the command line:

```bash
# Generate 5 Instagram models
python extras/influencer_cli.py --count 5 --type instagram_model

# Generate with maximum realism
python extras/influencer_cli.py --count 3 --max-realism --verbose

# Generate diverse influencers
python extras/influencer_cli.py --count 10 --diverse
```

This will create JSON files with ultra-realistic prompts you can use in Fooocus.

## Download Required Models

Before generating images, download the optimized models:

```bash
python extras/download_influencer_models.py
```

This downloads:
- realisticStockPhoto_v20.safetensors (base model)
- SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors (LoRA)
- Supporting enhancement models

## Launch with Optimized Settings

Start Fooocus with the influencer preset for best results:

```bash
python launch.py --preset influencer
```

## Web UI Integration (Optional)

To add the influencer tab to the Fooocus web UI:

1. Follow integration instructions in `INTEGRATION_INSTRUCTIONS.md`
2. Restart Fooocus
3. Use the new "Influencers" tab in the right sidebar

## Influencer Types Available

1. **Instagram Model** - Fashion and lifestyle content
2. **TikTok Star** - Viral social media personality
3. **Business Executive** - Corporate/professional persona
4. **Fitness Guru** - Health and athletic niche

## For Maximum Realism

When generating images:
- Use Quality performance mode
- Set steps to 200
- Enable maximum realism in advanced settings
- Apply multiple photographic styles
- Use recommended aspect ratios

## Sample Workflow

1. Run: `python extras/influencer_cli.py --count 3 --max-realism`
2. Open the generated JSON file
3. Copy prompts to Fooocus
4. Launch: `python launch.py --preset influencer`
5. Generate images with 200 steps

Your hyper-realistic AI influencers are ready!