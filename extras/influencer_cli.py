"""
Command-Line Interface for AI Influencer Generation
==================================================

A simple CLI for generating AI influencers with customizable options.
"""

import argparse
import json
import os
import sys

# Add the root directory to the path so we can import modules
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from extras.influencer_generator import (
    generate_influencer_batch, 
    save_influencer_configs,
    INFLUENCER_PRESETS
)


def main():
    parser = argparse.ArgumentParser(
        description="Generate AI influencers with customizable options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python extras/influencer_cli.py --count 5 --type instagram_model
  python extras/influencer_cli.py --count 3 --type tiktok_star --output tiktok_influencers.json
  python extras/influencer_cli.py --help
        """
    )
    
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Number of influencers to generate (default: 1)"
    )
    
    parser.add_argument(
        "-t", "--type",
        choices=list(INFLUENCER_PRESETS.keys()),
        default="instagram_model",
        help="Type of influencer to generate (default: instagram_model)"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output JSON file name (default: auto-generated)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed output for each influencer"
    )
    
    parser.add_argument(
        "--list-types",
        action="store_true",
        help="List available influencer types and exit"
    )
    
    parser.add_argument(
        "--max-realism",
        action="store_true",
        help="Enable maximum realism settings (200 steps, enhanced prompts)"
    )
    
    parser.add_argument(
        "--diverse",
        action="store_true",
        help="Generate diverse ethnicities and ages"
    )
    
    args = parser.parse_args()
    
    # Handle --list-types
    if args.list_types:
        print("Available influencer types:")
        for key, value in INFLUENCER_PRESETS.items():
            print(f"  {key}: {value['description']}")
        return
    
    # Validate count
    if args.count < 1:
        print("Error: Count must be at least 1")
        sys.exit(1)
    
    if args.count > 100:
        print("Warning: Generating more than 100 influencers at once may consume significant resources")
        response = input("Continue? (y/N): ")
        if response.lower() != 'y':
            print("Generation cancelled.")
            return
    
    # Generate influencers
    print(f"Generating {args.count} {args.type} influencer(s)...")
    influencers = generate_influencer_batch(count=args.count, influencer_type=args.type)
    
    # Apply max realism settings if requested
    if args.max_realism:
        print("Applying maximum realism settings...")
        for influencer in influencers:
            # Increase steps to maximum
            influencer["settings"]["steps"] = 200
            # Increase LoRA strength
            influencer["settings"]["loras"][0][1] = 0.5
            
    # Show verbose output if requested
    if args.verbose:
        for i, influencer in enumerate(influencers):
            print(f"\n--- Influencer {i+1} ---")
            print(f"ID: {influencer['id']}")
            print(f"Prompt: {influencer['prompt']}")
            print(f"Negative Prompt: {influencer['negative_prompt']}")
            print(f"Steps: {influencer['settings']['steps']}")
    
    # Save to file
    save_influencer_configs(influencers, args.output)
    
    print(f"\nSuccess! Generated {len(influencers)} influencer(s).")
    print("\nTo use these in Fooocus:")
    print("1. Copy the prompt and negative prompt to the respective fields")
    print("2. Apply the recommended settings in the advanced options")
    print("3. Generate with Quality performance and 200 steps for maximum realism")
    print("4. Use the 'influencer' preset for optimal results: python launch.py --preset influencer")

if __name__ == "__main__":
    main()