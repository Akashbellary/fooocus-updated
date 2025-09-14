import os
import json

def check_files():
    files_to_check = [
        "presets/influencer.json",
        "modules/influencer_ui.py",
        "INTEGRATION_INSTRUCTIONS.md",
        "INFLUENCER_FEATURE_README.md",
        "INFLUENCER_FEATURE_SUMMARY.md",
        "test_influencer_ui.py",
        "extras/influencer_generator.py",
        "extras/influencer_cli.py",
        "extras/download_influencer_models.py"
    ]
    
    print("Checking influencer feature files:")
    print("-" * 40)
    
    all_good = True
    for file in files_to_check:
        if os.path.exists(file):
            print(f"FOUND: {file}")
        else:
            print(f"MISSING: {file}")
            all_good = False
    
    # Check JSON validity
    if os.path.exists("presets/influencer.json"):
        try:
            with open("presets/influencer.json", "r") as f:
                json.load(f)
            print("JSON: presets/influencer.json is valid")
        except Exception as e:
            print(f"JSON ERROR: {e}")
            all_good = False
    
    print("-" * 40)
    if all_good:
        print("All files are present and valid!")
        print("\nTo integrate the influencer tab:")
        print("1. Follow instructions in INTEGRATION_INSTRUCTIONS.md")
        print("2. Run: python extras/download_influencer_models.py")
        print("3. Launch: python launch.py --preset influencer")
    else:
        print("Some files are missing or invalid.")

if __name__ == "__main__":
    check_files()