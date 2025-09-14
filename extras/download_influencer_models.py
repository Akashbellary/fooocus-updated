"""
Download Models for AI Influencer Generation
===========================================

This script automatically downloads the recommended models for 
creating hyper-realistic AI influencers.
"""

import os
import sys

# Add the root directory to the path so we can import modules
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from modules.model_loader import load_file_from_url
from modules.config import paths_checkpoints, paths_loras

def download_influencer_models():
    """Download all recommended models for influencer generation."""
    
    print("Downloading models for AI Influencer Generation...")
    print("=" * 50)
    
    # Create directories if they don't exist
    os.makedirs(paths_checkpoints[0], exist_ok=True)
    os.makedirs(paths_loras[0], exist_ok=True)
    
    # Download base model
    print("1. Downloading realisticStockPhoto_v20.safetensors (base model)...")
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/realisticStockPhoto_v20.safetensors',
        model_dir=paths_checkpoints[0],
        file_name='realisticStockPhoto_v20.safetensors'
    )
    print("   ✓ Download complete")
    
    # Download LoRA model
    print("2. Downloading SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors (LoRA)...")
    load_file_from_url(
        url='https://huggingface.co/mashb1t/fav_models/resolve/main/fav/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors',
        model_dir=paths_loras[0],
        file_name='SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors'
    )
    print("   ✓ Download complete")
    
    # Download additional quality enhancement models
    print("3. Downloading fooocus_expansion.bin (prompt expansion)...")
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_expansion.bin',
        model_dir=os.path.join(root_dir, 'models', 'prompt_expansion', 'fooocus_expansion'),
        file_name='pytorch_model.bin'
    )
    print("   ✓ Download complete")
    
    # Download VAE approximation model for better quality
    print("4. Downloading xlvaeapp.pth (VAE approximation)...")
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/xlvaeapp.pth',
        model_dir=os.path.join(root_dir, 'models', 'vae_approx'),
        file_name='xlvaeapp.pth'
    )
    print("   ✓ Download complete")
    
    print("\n" + "=" * 50)
    print("All models downloaded successfully!")
    print("\nRecommended next steps:")
    print("1. Run: python extras/influencer_generator.py")
    print("2. Start Fooocus: python launch.py --preset influencer")
    print("3. Use the generated prompts in the UI")

if __name__ == "__main__":
    download_influencer_models()