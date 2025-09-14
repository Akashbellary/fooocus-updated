# AI Influencer Generator Extension

Fooocus now includes powerful AI influencer generation capabilities that allow you to create hyper-realistic digital personas indistinguishable from real people.

## Key Features

### 4 Influencer Types
- **Instagram Model** - Fashion and lifestyle content
- **TikTok Star** - Viral social media personality
- **Business Executive** - Corporate/professional persona
- **Fitness Guru** - Health and athletic niche

### Ultra-Realistic Generation
- Automatically generated prompts with technical photography terminology
- Pre-optimized settings for maximum photorealism
- 200-step generation for ultimate detail
- Comprehensive negative prompts to prevent artifacts

### Dual Usage Modes
1. **Web UI Integration** - New "Influencers" tab for seamless usage
2. **Command-Line Tools** - Generate influencers without the UI

## Quick Start

```bash
# Download optimized models
python extras/download_influencer_models.py

# Generate influencer prompts
python extras/influencer_cli.py --count 5 --type instagram_model

# Launch Fooocus with influencer preset
python launch.py --preset influencer
```

## Web UI Integration

After following the integration instructions in `INTEGRATION_INSTRUCTIONS.md`:

1. Open the new "Influencers" tab in the right sidebar
2. Select an influencer type
3. Click "Generate Influencer Prompt"
4. Adjust advanced settings if needed
5. Click "Apply to Main Prompts"
6. Generate images as usual

## Technical Highlights

### Optimized Model Stack
- **Base Model**: realisticStockPhoto_v20.safetensors
- **LoRA**: SDXL_FILM_PHOTOGRAPHY_STYLE_V1 at 0.5 strength
- **Styles**: Fooocus Photograph + Sharp + sai-photographic
- **Performance**: Quality mode with 200 steps

### Advanced Controls
- Maximum Realism toggle (200 steps)
- Diverse Ethnicities option
- Age Group selection
- Configuration saving

## Documentation Files

- `INTEGRATION_INSTRUCTIONS.md` - Web UI integration guide
- `INFLUENCER_FEATURE_README.md` - Complete feature documentation
- `INFLUENCER_FEATURE_SUMMARY.md` - Implementation overview
- `QUICK_START.md` - Immediate usage instructions

## Expected Results

Images generated with these settings will be:
- Photorealistic in quality
- Indistinguishable from professional photography
- Suitable for commercial use
- Diverse in ethnicity and age
- Consistent in style and quality

The AI Influencer Generator extension is ready to use!