import gradio as gr
import random
import json
from datetime import datetime
import modules.config as config
from modules.flags import Performance, Steps

# Influencer-specific configurations
INFLUENCER_TYPES = {
    "instagram_model": {
        "name": "Instagram Model",
        "description": "Perfect for fashion and lifestyle influencers",
        "styles": ["Fooocus Photograph", "Fooocus Sharp", "sai-photographic"],
        "aspect_ratio": "896*1152",
        "cfg_scale": 3.5,
        "sharpness": 3.0
    },
    "tiktok_star": {
        "name": "TikTok Star",
        "description": "Ideal for viral social media content creators",
        "styles": ["Fooocus Cinematic", "sai-cinematic", "Fooocus V2"],
        "aspect_ratio": "768*1344",  # Vertical video format
        "cfg_scale": 4.0,
        "sharpness": 2.5
    },
    "business_executive": {
        "name": "Business Executive",
        "description": "Professional corporate persona",
        "styles": ["Fooocus Photograph", "sai-photographic", "Fooocus Masterpiece"],
        "aspect_ratio": "1152*896",
        "cfg_scale": 3.0,
        "sharpness": 2.0
    },
    "fitness_guru": {
        "name": "Fitness Guru",
        "description": "Athletic and health-focused influencer",
        "styles": ["Fooocus Photograph", "sai-analog film", "Fooocus Sharp"],
        "aspect_ratio": "1024*1024",
        "cfg_scale": 4.5,
        "sharpness": 3.5
    }
}

# Comprehensive list of influencer characteristics
INFLUENCER_CHARACTERISTICS = {
    "facial_features": [
        "symmetrical face", "high cheekbones", "sharp jawline", "defined jawline",
        "oval face shape", "heart-shaped face", "almond-shaped eyes", "full lips",
        "straight nose", "small nose", "button nose", "dimples", "high forehead",
        "perfect bone structure", "chiseled features", "flawless complexion"
    ],
    "hair_styles": [
        "flowing hair", "styled hair", "glossy hair", "shiny hair", "luxurious hair",
        "voluminous hair", "silky hair", "lustrous hair", "glistening hair",
        "perfectly styled hair", "flawless hair", "radiant hair", "glossy locks",
        "shimmering hair", "luminous hair", "vibrant hair"
    ],
    "lighting_conditions": [
        "studio lighting", "soft lighting", "natural lighting", "golden hour lighting",
        "dramatic lighting", "cinematic lighting", "professional lighting",
        "perfect lighting", "flattering light", "even lighting", "Rembrandt lighting",
        "butterfly lighting", "loop lighting", "split lighting"
    ],
    "camera_equipment": [
        "Canon EOS R5", "Nikon Z8", "Sony A7R V", "Hasselblad X2D 100C",
        "Leica SL2-S", "Fujifilm GFX 100S", "Panasonic S1R", "Olympus OM-1",
        "Phase One XF IQ4", "Bronica SQ-A", "Mamiya RZ67", "Pentax 645Z"
    ],
    "photography_styles": [
        "professional portrait", "fashion photography", "editorial shoot",
        "commercial photography", "glamour photography", "beauty photography",
        "headshot photography", "profile picture", "corporate headshot",
        "high fashion editorial", "couture photography", "luxury brand campaign"
    ],
    "expressions": [
        "confident smile", "warm smile", "professional smile", "genuine smile",
        "charming smile", "captivating smile", "radiant smile", "bright smile",
        "serious expression", "thoughtful expression", "focused expression",
        "mysterious gaze", "intense stare", "seductive look", "approachable grin"
    ],
    "attire": [
        "designer clothing", "fashionable outfit", "stylish attire",
        "trendy clothes", "elegant outfit", "sophisticated attire",
        "professional wear", "business attire", "casual chic outfit",
        "haute couture", "luxury fashion", "runway ready", "red carpet worthy"
    ],
    "backgrounds": [
        "urban cityscape", "luxury interior", "minimalist background",
        "studio backdrop", "outdoor location", "modern architecture",
        "natural scenery", "elegant setting", "professional environment",
        "penthouse view", "boutique hotel lobby", "art gallery", "yacht deck"
    ]
}

# Quality enhancement keywords for maximum realism
QUALITY_ENHANCEMENT_KEYWORDS = [
    "8k resolution", "ultra detailed", "highly detailed", "professional photo",
    "sharp focus", "perfect composition", "award winning", "magazine quality",
    "commercial photography", "editorial quality", "studio quality",
    "photorealistic", "hyper realistic", "uncanny valley", "film grain",
    "cinematic", "vignette", "depth of field", "bokeh", "detailed skin texture",
    "pores visible", "realistic hair strands", "perfect lighting",
    "professional retouching", "flawless skin", "crystal clear", "HDR",
    "masterpiece", "best quality", "intricate details", "epic detailed",
    "sharp focus", "dramatic lighting", "volumetric lighting", 
    "ray tracing", "physically based rendering", "subsurface scattering",
    "specular reflection", "diffraction grading", "chromatic aberration",
    "motion blur", "focus peaking", "noise reduction", "dynamic range",
    "color graded", "anamorphic lens flare", "optical vignetting"
]

# Ethnicity and diversity descriptors for realistic variation
ETHNICITY_DESCRIPTORS = [
    "Caucasian", "African", "Asian", "Latino", "Middle Eastern", 
    "Mediterranean", "Scandinavian", "East Asian", "South Asian",
    "Southeast Asian", "Pacific Islander", "Indigenous", "Mixed heritage"
]

# Age range descriptors
AGE_DESCRIPTORS = [
    "young adult", "mid-twenties", "early thirties", "thirty-something",
    "mid-age", "mature", "middle-aged", "prime of life"
]

def generate_influencer_prompt(influencer_type="instagram_model", custom_attributes=None):
    """
    Generate a comprehensive prompt for creating hyper-realistic AI influencers.
    
    Args:
        influencer_type (str): Type of influencer to generate
        custom_attributes (dict): Custom attributes to override defaults
        
    Returns:
        str: Generated prompt for influencer creation
    """
    if custom_attributes is None:
        custom_attributes = {}
    
    preset = INFLUENCER_TYPES.get(influencer_type, INFLUENCER_TYPES["instagram_model"])
    
    # Select random characteristics
    facial_feature = random.choice(INFLUENCER_CHARACTERISTICS["facial_features"])
    hair_style = random.choice(INFLUENCER_CHARACTERISTICS["hair_styles"])
    lighting = random.choice(INFLUENCER_CHARACTERISTICS["lighting_conditions"])
    camera = random.choice(INFLUENCER_CHARACTERISTICS["camera_equipment"])
    photo_style = random.choice(INFLUENCER_CHARACTERISTICS["photography_styles"])
    expression = random.choice(INFLUENCER_CHARACTERISTICS["expressions"])
    attire = random.choice(INFLUENCER_CHARACTERISTICS["attire"])
    background = random.choice(INFLUENCER_CHARACTERISTICS["backgrounds"])
    ethnicity = random.choice(ETHNICITY_DESCRIPTORS)
    age = random.choice(AGE_DESCRIPTORS)
    
    # Select quality enhancement keywords (5-8 random ones for maximum detail)
    quality_keywords = random.sample(QUALITY_ENHANCEMENT_KEYWORDS, random.randint(5, 8))
    
    # Build the prompt with enhanced realism descriptors
    prompt_parts = [
        f"portrait of a {age} {ethnicity}",
        facial_feature,
        hair_style,
        expression,
        attire,
        photo_style,
        lighting,
        f"shot on {camera}",
        background,
        "RAW photo",  # Ensures photorealism
        "professional model",  # Adds authenticity
        "perfect skin texture",  # Enhances realism
        "natural freckles visible",  # Adds human imperfections for believability
        "individual eyelashes visible",  # Extreme detail
        "realistic hair follicles"  # Ultimate detail level
    ]
    
    # Add quality enhancement keywords
    prompt_parts.extend(quality_keywords)
    
    # Join all parts with commas
    prompt = ", ".join(prompt_parts)
    
    return prompt

def generate_influencer_negative_prompt():
    """
    Generate a comprehensive negative prompt to avoid unrealistic features.
    
    Returns:
        str: Negative prompt for influencer generation
    """
    negative_prompt = (
        "cartoon, anime, 3d render, computer graphics, painting, drawing, sketch, "
        "low quality, blurry, out of focus, low resolution, pixelated, compressed, "
        "watermark, text, logo, signature, distorted face, asymmetric face, "
        "disproportionate features, unrealistic proportions, plastic look, "
        "artificial appearance, doll-like, mannequin, mask, costume, fake, "
        "oversaturated, underexposed, overexposed, poor lighting, harsh shadows, "
        "grainy, noisy, smudged, deformed, mutated, extra limbs, missing features, "
        "cropped face, cut off features, bad anatomy, wrong anatomy, "
        "disconnected limbs, malformed hands, extra fingers, missing fingers, "
        "floating head, detached body parts, unrealistic eyes, empty eyes, "
        "expressionless face, frozen expression, unnatural pose, stiff pose, "
        "bad composition, cluttered scene, busy background, distracting elements, "
        "low detail, lack of detail, smooth skin without pores, artificial skin, "
        "plastic skin, glowing skin, shiny face, oily face, sweaty face, "
        "over-retouched, airbrushed effect, filter effect, snapchat filter, "
        "instagram filter, unrealistic beauty standards, impossible perfection, "
        "cgi, digital art, concept art, stylized, rendered, vector art, "
        "illustration, painting, drawing, sketch, unrealistic lighting, "
        "unnatural colors, oversharpened, halos, chromatic aberration errors, "
        "compression artifacts, jpeg artifacts, noise, grain, film damage, "
        "motion blur, camera shake, lens distortion, chromatic fringing, "
        "moire patterns, banding, posterization, color bleeding, "
        "unrealistic shadows, hard shadows, double exposure, multiple exposures, "
        "ghosting, flare artifacts, lens flare, bokeh artifacts, "
        "unrealistic depth of field, shallow focus errors, perspective errors, "
        "geometric distortion, barrel distortion, pincushion distortion, "
        "vignetting errors, color cast, white balance errors, exposure errors, "
        "highlight clipping, shadow clipping, lossy compression, "
        "blocky artifacts, ringing artifacts, aliasing, jaggies, "
        "pixelation, interpolation artifacts, upscaling artifacts, "
        "generative artifacts, neural network artifacts, deepfake artifacts, "
        "synthetic appearance, artificial lighting, studio lighting errors, "
        "unnatural skin tones, plastic skin, wax figure, mannequin, "
        "doll, puppet, marionette, action figure, toy, figurine, "
        "3d model, render, cgi, computer generated, digitally created, "
        "algorithmic, procedural, formulaic, generic, template, "
        "stock photo, clipart, emoji, caricature, parody, satire, "
        "exaggerated features, distorted proportions, surreal, fantastical, "
        "impossible physics, physically impossible, physically inaccurate"
    )
    
    return negative_prompt

def get_influencer_settings(influencer_type="instagram_model"):
    """
    Get optimal settings for influencer generation.
    
    Args:
        influencer_type (str): Type of influencer to generate
        
    Returns:
        dict: Settings dictionary for influencer generation
    """
    preset = INFLUENCER_TYPES.get(influencer_type, INFLUENCER_TYPES["instagram_model"])
    
    settings = {
        "base_model": "realisticStockPhoto_v20.safetensors",
        "refiner_model": "None",
        "refiner_switch": 0.5,
        "loras": [
            ["SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors", 0.5],  # Increased strength for more realism
            ["None", 1.0],
            ["None", 1.0],
            ["None", 1.0],
            ["None", 1.0]
        ],
        "cfg_scale": preset["cfg_scale"],
        "sharpness": preset["sharpness"],
        "sampler": "dpmpp_2m_sde_gpu",
        "scheduler": "karras",
        "performance": Performance.QUALITY.value,
        "steps": 200,  # Maximum steps for ultimate detail
        "styles": preset["styles"],
        "aspect_ratio": preset["aspect_ratio"],
        "image_number": 1
    }
    
    return settings

def create_influencer_tab():
    """Create the Influencer tab for the Fooocus UI."""
    
    with gr.Tab(label="Influencers", elem_id="influencer_tab"):
        gr.Markdown("## AI Influencer Generator")
        gr.Markdown("Create hyper-realistic AI influencers that are virtually indistinguishable from real people.")
        
        with gr.Row():
            with gr.Column(scale=1):
                influencer_type = gr.Dropdown(
                    choices=[(v["name"], k) for k, v in INFLUENCER_TYPES.items()],
                    value="instagram_model",
                    label="Influencer Type"
                )
                
                gr.Markdown("**Influencer Type Descriptions:**")
                for key, value in INFLUENCER_TYPES.items():
                    gr.Markdown(f"- **{value['name']}**: {value['description']}")
                
                generate_btn = gr.Button("Generate Influencer Prompt", variant="primary")
                
                with gr.Accordion("Advanced Settings", open=False):
                    max_realism = gr.Checkbox(label="Maximum Realism (200 steps)", value=True)
                    diverse_ethnicity = gr.Checkbox(label="Diverse Ethnicities", value=True)
                    custom_age = gr.Dropdown(
                        choices=["Any"] + AGE_DESCRIPTORS,
                        value="Any",
                        label="Age Group"
                    )
            
            with gr.Column(scale=2):
                influencer_prompt = gr.Textbox(
                    label="Positive Prompt",
                    placeholder="Generated influencer prompt will appear here...",
                    lines=6,
                    max_lines=10
                )
                
                influencer_negative_prompt = gr.Textbox(
                    label="Negative Prompt",
                    value=generate_influencer_negative_prompt(),
                    lines=6,
                    max_lines=10
                )
                
                with gr.Row():
                    apply_to_main = gr.Button("Apply to Main Prompts")
                    save_config = gr.Button("Save Configuration")
                
                influencer_config_display = gr.JSON(label="Influencer Configuration")
        
        # Functions
        def generate_influencer(influencer_type, max_realism, diverse_ethnicity, custom_age):
            # Generate custom attributes
            custom_attributes = {}
            if custom_age != "Any":
                custom_attributes["age"] = custom_age
                
            # Generate prompt
            prompt = generate_influencer_prompt(influencer_type, custom_attributes)
            
            # Get settings
            settings = get_influencer_settings(influencer_type)
            
            # Apply max realism if requested
            if max_realism:
                settings["steps"] = 200
                settings["loras"][0][1] = 0.5
            
            # Create configuration
            influencer_config = {
                "id": f"influencer_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "type": influencer_type,
                "prompt": prompt,
                "negative_prompt": generate_influencer_negative_prompt(),
                "settings": settings
            }
            
            return prompt, influencer_config
        
        # Event handlers
        generate_btn.click(
            fn=generate_influencer,
            inputs=[influencer_type, max_realism, diverse_ethnicity, custom_age],
            outputs=[influencer_prompt, influencer_config_display]
        )
        
        save_config.click(
            fn=lambda config: json.dumps(config, indent=2),
            inputs=[influencer_config_display],
            outputs=[]
        )
    
    # Return the components that need to be connected externally
    # Note: We don't return apply_to_main button to avoid Gradio conflicts
    return influencer_prompt, influencer_negative_prompt
