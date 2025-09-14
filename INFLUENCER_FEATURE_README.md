# AI Influencer Generator for Fooocus

## Overview

This feature adds powerful AI influencer generation capabilities directly to the Fooocus web UI. Users can create hyper-realistic AI influencers that are virtually indistinguishable from real people, with just a few clicks.

## Features

- **Multiple Influencer Types**: Instagram models, TikTok stars, business executives, and fitness gurus
- **Ultra-Realistic Prompts**: Automatically generated prompts with technical photography terminology
- **One-Click Integration**: Apply generated prompts directly to the main Fooocus interface
- **Advanced Settings**: Control realism level, diversity, and age groups
- **Pre-Optimized Presets**: Settings automatically configured for maximum photorealism

## Installation

All necessary files have been created during setup:

1. `modules/influencer_ui.py` - UI components for the influencer tab
2. `presets/influencer.json` - Optimized settings for influencer generation
3. `extras/influencer_generator.py` - Core generation logic
4. `extras/influencer_cli.py` - Command-line interface
5. `extras/download_influencer_models.py` - Model downloader

## Integration Instructions

Follow the detailed steps in `INTEGRATION_INSTRUCTIONS.md` to add the influencer tab to the Fooocus web UI.

## Usage

### Web UI Method (Recommended)

1. Start Fooocus with the influencer preset:
   ```bash
   python launch.py --preset influencer
   ```

2. Navigate to the new "Influencers" tab in the right sidebar

3. Select an influencer type from the dropdown menu

4. Click "Generate Influencer Prompt" to create a detailed prompt

5. Adjust advanced settings if desired:
   - Enable "Maximum Realism" for 200-step generation
   - Enable "Diverse Ethnicities" for varied demographics
   - Select a specific age group

6. Click "Apply to Main Prompts" to transfer the generated prompts to the main interface

7. Generate images using the standard Fooocus workflow

### Command Line Method

Generate influencer prompts via command line:

```bash
# Generate 5 Instagram models
python extras/influencer_cli.py --count 5 --type instagram_model

# Generate with maximum realism settings
python extras/influencer_cli.py --count 3 --max-realism

# Generate diverse influencers with verbose output
python extras/influencer_cli.py --count 10 --diverse --verbose
```

## Influencer Types

1. **Instagram Model**
   - Perfect for fashion and lifestyle influencers
   - Optimized for portrait photography
   - Default aspect ratio: 896×1152

2. **TikTok Star**
   - Ideal for viral social media content creators
   - Vertical video format optimized
   - Default aspect ratio: 768×1344

3. **Business Executive**
   - Professional corporate persona
   - Suitable for LinkedIn and professional use
   - Default aspect ratio: 1152×896

4. **Fitness Guru**
   - Athletic and health-focused influencer
   - Great for workout and wellness content
   - Default aspect ratio: 1024×1024

## Technical Details

### Optimized Settings

The influencer preset uses these optimized settings for maximum realism:

- **Base Model**: `realisticStockPhoto_v20.safetensors`
- **LoRA**: `SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors` at 0.5 strength
- **Styles**: Fooocus Photograph + Fooocus Sharp + sai-photographic
- **Performance**: Quality mode
- **Steps**: 200 (maximum detail)
- **CFG Scale**: 3.5 (balanced creativity and accuracy)
- **Sharpness**: 3.0 (enhanced detail)

### Prompt Engineering

Generated prompts include:

- Detailed physical characteristics
- Professional photography equipment
- Studio-quality lighting conditions
- High-fashion attire descriptions
- Technical quality enhancement keywords
- Context-appropriate backgrounds

### Negative Prompts

Comprehensive negative prompts prevent:

- Cartoon or anime characteristics
- 3D rendering artifacts
- Low-quality issues
- Anatomical abnormalities
- Artificial appearance markers
- Over-processing effects

## Best Practices

### For Maximum Realism

1. Use the "Quality" performance setting
2. Enable "Maximum Realism" in advanced settings
3. Generate with 200 steps
4. Use the influencer preset: `python launch.py --preset influencer`
5. Apply multiple complementary styles
6. Use recommended aspect ratios for each influencer type

### Post-Processing Tips

1. Use the "Enhance" feature for additional detail
2. Apply subtle variations with "Vary (Subtle)"
3. Use inpainting for fine-tuning specific features
4. Experiment with different seeds for variety

## Ethical Guidelines

When creating AI influencers, please:

1. Be transparent about their AI-generated nature when required
2. Respect likeness rights and intellectual property
3. Avoid deceptive representation
4. Follow platform policies and terms of service
5. Consider the societal impact of synthetic personas

## Troubleshooting

### Common Issues

1. **Influencer tab not appearing**
   - Verify integration steps in `INTEGRATION_INSTRUCTIONS.md`
   - Check for syntax errors in `webui.py`
   - Restart Fooocus after making changes

2. **Generated images not realistic enough**
   - Ensure you're using the influencer preset
   - Enable maximum realism settings
   - Use 200 steps for generation
   - Check that required models are downloaded

3. **Apply to Main Prompts not working**
   - Verify the button connections in `webui.py`
   - Check browser console for JavaScript errors

### Model Requirements

Ensure these models are downloaded:

- `realisticStockPhoto_v20.safetensors` (base model)
- `SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors` (LoRA)

Download them automatically with:
```bash
python extras/download_influencer_models.py
```

## Support

For issues with the influencer feature:

1. Check this documentation
2. Review the integration instructions
3. Verify all required files are present
4. Ensure models are properly downloaded
5. Check the Fooocus community forums

## Future Enhancements

Planned improvements:

- Additional influencer types
- Custom influencer templates
- Batch generation with consistent characteristics
- Export/import of influencer configurations
- Integration with face enhancement features
- Automated background replacement

## Credits

This feature builds upon the excellent work of the Fooocus team and the broader AI art community.