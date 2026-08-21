import torch
from diffusers import StableDiffusionPipeline

# -------------------------------------------------
# PRE-TRAINED TEXT-TO-IMAGE MODEL
# -------------------------------------------------

model_id = "runwayml/stable-diffusion-v1-5"

print("Loading pre-trained text-to-image model...")
print("Please wait. The first run may take some time.")

# Select CPU or GPU automatically
device = "cuda" if torch.cuda.is_available() else "cpu"

print("Using device:", device)

# Load model
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

pipe = pipe.to(device)

# -------------------------------------------------
# TEXT PROMPT
# -------------------------------------------------

prompt = """
A highly detailed engineering visualization of a modern
cable-stayed bridge crossing a wide river, strong concrete
pillars, steel suspension cables, modern road infrastructure,
engineers inspecting the bridge, realistic engineering design,
professional architectural visualization, realistic materials,
high detail, realistic lighting, 4K quality
"""

# -------------------------------------------------
# NEGATIVE PROMPT
# -------------------------------------------------

negative_prompt = """
blurry, low quality, distorted structure, broken bridge,
deformed objects, unrealistic architecture, text, watermark
"""

# -------------------------------------------------
# GENERATE IMAGE
# -------------------------------------------------

print("Generating engineering image...")

image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]

# -------------------------------------------------
# SAVE IMAGE
# -------------------------------------------------

image.save("engineering_bridge.png")

print()
print("==============================================")
print("IMAGE GENERATED SUCCESSFULLY!")
print("==============================================")
print("Saved as: engineering_bridge.png")
