# Complete Guide to AI Influencer Generation

This guide walks you through the entire process of creating hyper-realistic AI influencers using the tools we've provided.

## Prerequisites

1. Fooocus installed and running
2. Python 3.10 or higher
3. At least 12GB VRAM (recommended) or 16GB RAM for CPU inference

## Quick Start

### Windows

Double-click on `extras/setup_influencer_windows.bat` to automatically:
1. Download all required models
2. Generate sample influencer prompts
3. Launch Fooocus with optimal settings

### Linux/Mac

Run in terminal:
```bash
chmod +x extras/setup_influencer.sh
./extras/setup_influencer.sh
```

## Manual Setup

### 1. Download Required Models

```bash
python extras/download_influencer_models.py
```

This downloads:
- realisticStockPhoto_v20.safetensors (base model)
- SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors (LoRA)
- Supporting enhancement models

### 2. Generate Influencer Prompts

```bash
python extras/influencer_generator.py
```

This creates sample prompts and saves them to `sample_influencers.json`.

### 3. Launch with Influencer Preset

```bash
python launch.py --preset influencer
```

## Understanding the Components

### Preset Configuration

We've created a specialized preset at `presets/influencer.json` with:
- Optimized model and LoRA settings
- Recommended CFG scale and sharpness
- Quality performance mode
- Pre-selected styles for maximum realism

### Influencer Generator Script

The `influencer_generator.py` script provides:
- Multiple influencer archetypes
- Advanced prompt engineering
- Optimal parameter recommendations
- Batch generation capabilities

## Creating Your Own Influencers

### 1. Choose an Influencer Type

Available types:
- `instagram_model`: Fashion/lifestyle content
- `tiktok_star`: Social media personality
- `business_executive`: Corporate/professional
- `fitness_guru`: Health/athletic niche

### 2. Generate Custom Prompts

```python
from extras.influencer_generator import generate_influencer_batch

# Generate 5 unique fitness influencers
influencers = generate_influencer_batch(count=5, influencer_type="fitness_guru")

for i, inf in enumerate(influencers):
    print(f"Influencer {i+1}: {inf['prompt']}")
```

### 3. Fine-tune Parameters

Key parameters to adjust for maximum realism:

| Parameter | Recommended Value | Purpose |
|-----------|-------------------|---------|
| Performance | Quality | Maximum detail |
| Steps | 60+ | Fine detail rendering |
| CFG Scale | 3.0-4.5 | Balance creativity/accuracy |
| Sharpness | 2.0-3.5 | Image clarity |
| Styles | Multiple | Layered enhancements |

## Advanced Techniques

### 1. Aspect Ratio Optimization

Different platforms benefit from specific ratios:
- Instagram posts: 1024×1024
- Instagram stories: 768×1344
- TikTok videos: 768×1344
- LinkedIn posts: 1152×896

### 2. Multi-Stage Generation

For ultimate quality:
1. Generate base image (1152×1152)
2. Use "Upscale (2x)" feature
3. Apply "Improve Detail" to enhance faces
4. Use "Vary (Subtle)" for fine adjustments

### 3. Style Mixing

Combine multiple styles for unique results:
- `Fooocus Photograph` + `sai-photographic` (realistic)
- `Fooocus Cinematic` + `sai-cinematic` (dramatic)
- `Fooocus Masterpiece` + `sai-enhance` (polished)

## Troubleshooting

### Common Issues

1. **Out of Memory Errors**
   - Reduce image size
   - Use Speed performance mode
   - Close other applications

2. **Unrealistic Results**
   - Increase steps to 60+
   - Adjust CFG scale (3.0-4.5 range)
   - Use Quality performance mode
   - Ensure proper negative prompts

3. **Slow Generation**
   - Use Extreme Speed or Lightning modes
   - Reduce steps (20-40)
   - Lower resolution

### Quality Optimization Checklist

- [ ] Using realisticStockPhoto_v20.safetensors base model
- [ ] Applying SDXL_FILM_PHOTOGRAPHY_STYLE_V1 LoRA
- [ ] Setting performance to Quality
- [ ] Using 60+ steps
- [ ] Including detailed positive prompts
- [ ] Using comprehensive negative prompts
- [ ] Applying multiple complementary styles

## Ethical Considerations

When creating AI influencers, consider:
1. Transparency about AI generation
2. Respecting likeness rights
3. Avoiding deceptive representation
4. Complying with platform policies
5. Considering societal impact

## Next Steps

1. Experiment with different influencer types
2. Create branded content variations
3. Develop consistent visual identities
4. Explore animation possibilities
5. Build diverse character portfolios

For support, refer to the main Fooocus documentation or community forums.