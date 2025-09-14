#!/usr/bin/env python3
"""
Test script for the influencer UI module
"""

import sys
import os

# Add the root directory to the path so we can import modules
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir)

try:
    import modules.influencer_ui as influencer_ui
    print("SUCCESS: influencer_ui module imported correctly")
    
    # Test that the main data structures exist
    if hasattr(influencer_ui, 'INFLUENCER_TYPES'):
        print(f"SUCCESS: Found {len(influencer_ui.INFLUENCER_TYPES)} influencer types")
        for key, value in influencer_ui.INFLUENCER_TYPES.items():
            print(f"  - {value['name']}: {value['description']}")
    else:
        print("ERROR: INFLUENCER_TYPES not found")
    
    # Test function calls
    try:
        prompt = influencer_ui.generate_influencer_prompt()
        print(f"SUCCESS: Generated sample prompt: {prompt[:50]}...")
    except Exception as e:
        print(f"ERROR: Failed to generate prompt: {e}")
        
    try:
        negative_prompt = influencer_ui.generate_influencer_negative_prompt()
        print(f"SUCCESS: Generated negative prompt length: {len(negative_prompt)} characters")
    except Exception as e:
        print(f"ERROR: Failed to generate negative prompt: {e}")
        
    try:
        settings = influencer_ui.get_influencer_settings()
        print(f"SUCCESS: Generated settings with {len(settings)} parameters")
        print(f"  - Base model: {settings.get('base_model', 'Not found')}")
        print(f"  - Steps: {settings.get('steps', 'Not found')}")
    except Exception as e:
        print(f"ERROR: Failed to generate settings: {e}")
        
    print("\nAll tests completed!")
    
except ImportError as e:
    print(f"ERROR: Failed to import influencer_ui module: {e}")
except Exception as e:
    print(f"ERROR: Unexpected error: {e}")