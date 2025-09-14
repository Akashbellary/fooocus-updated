#!/bin/bash

echo "========================================"
echo "AI Influencer Generator Setup for Linux/Mac"
echo "========================================"
echo
echo "This script will set up everything needed to create hyper-realistic AI influencers."
echo
echo "Press Enter to continue..."
read

echo
echo "Step 1: Downloading required models..."
echo "----------------------------------------"
python extras/download_influencer_models.py
echo
echo "Step 2: Generating sample influencer prompts..."
echo "-----------------------------------------------"
python extras/influencer_generator.py
echo
echo "Step 3: Starting Fooocus with influencer preset..."
echo "--------------------------------------------------"
python launch.py --preset influencer
echo
echo "Setup complete! If you see any errors, please check the console output above."
