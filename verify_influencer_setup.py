"#!/usr/bin/env python3
\"\"\"
Verification script for the influencer feature setup
\"\"\"

import os
import json

def check_file_exists(filepath):
    \"\"\"Check if a file exists and print status\"\"\"
    if os.path.exists(filepath):
        print(f\"PASS: {filepath} - EXISTS\")
        return True
    else:
        print(f\"FAIL: {filepath} - MISSING\")
        return False

def check_json_file(filepath):
    \"\"\"Check if a JSON file is valid\"\"\"
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        print(f\"PASS: {filepath} - VALID JSON\")
        return True
    except json.JSONDecodeError as e:
        print(f\"FAIL: {filepath} - INVALID JSON: {e}\")
        return False
    except Exception as e:
        print(f\"FAIL: {filepath} - ERROR: {e}\")
        return False

def check_python_file(filepath):
    \"\"\"Check if a Python file has basic structure\"\"\"
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check for basic Python structure
        if 'def ' in content and 'import ' in content:
            print(f\"PASS: {filepath} - APPEARS VALID\")
            return True
        else:
            print(f\"WARN: {filepath} - FILE EXISTS BUT MAY BE INCOMPLETE\")
            return False
    except Exception as e:
        print(f\"FAIL: {filepath} - ERROR: {e}\")
        return False

def main():
    print(\"Verifying AI Influencer Generator Setup\")
    print(\"=\" * 50)
    
    # Check preset file
    preset_file = \"presets/influencer.json\"
    check_json_file(preset_file)
    
    # Check UI module
    ui_module = \"modules/influencer_ui.py\"
    check_python_file(ui_module)
    
    # Check documentation
    docs = [
        \"INTEGRATION_INSTRUCTIONS.md\",
        \"INFLUENCER_FEATURE_README.md\",
        \"INFLUENCER_FEATURE_SUMMARY.md\"
    ]
    
    for doc in docs:
        check_file_exists(doc)
    
    # Check test script
    test_script = \"test_influencer_ui.py\"
    check_file_exists(test_script)
    
    # Check existing extras files
    extras_files = [
        \"extras/influencer_generator.py\",
        \"extras/influencer_cli.py\",
        \"extras/download_influencer_models.py\"
    ]
    
    for extra in extras_files:
        check_file_exists(extra)
    
    print(\"\\nVerification complete!\")
    print(\"\\nNext steps:\")
    print(\"1. Follow INTEGRATION_INSTRUCTIONS.md to add the influencer tab to Fooocus UI\")
    print(\"2. Run 'python extras/download_influencer_models.py' to download required models\")
    print(\"3. Launch Fooocus with 'python launch.py --preset influencer'\")

if __name__ == \"__main__\":
    main()"
