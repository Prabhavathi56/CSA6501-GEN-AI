import torch
from diffusers import StableDiffusionPipeline

# =========================================================
# LOAD PRE-TRAINED TEXT-TO-IMAGE MODEL
# =========================================================

model_id = "runwayml/stable-diffusion-v1-5"

print("Loading pre-trained model...")
print("Please wait...")

device = "cuda" if torch.cuda.is_available() else "cpu"

if device == "cuda":
    dtype = torch.float16
else:
    dtype = torch.float32

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=dtype
)

pipe = pipe.to(device)

# =========================================================
# THREE DIFFERENT TEXT PROMPTS
# =========================================================

prompts = [

    # Prompt 1 - Simple
    """
    A modern engineering bridge over a river,
    realistic bridge, daytime, engineering structure
    """,

    # Prompt 2 - Detailed
    """
    A large modern cable-stayed engineering bridge
    crossing a wide river, tall concrete towers,
    steel suspension cables, multiple road lanes,
    engineers inspecting the structure, realistic
    engineering environment, detailed architecture,
    bright daylight
    """,

    # Prompt 3 - Futuristic
    """
    A futuristic smart engineering bridge over a river,
    advanced cable system, intelligent LED lighting,
    autonomous vehicles, robotic inspection drones,
    modern city skyline, advanced materials,
    high-tech engineering design, cinematic lighting,
    ultra detailed
    """
]

# =========================================================
# GENERATE THREE IMAGES
# =========================================================

for i, prompt in enumerate(prompts):

    print()
    print("Generating image", i + 1)

    image = pipe(
        prompt=prompt,
        num_inference_steps=30,
        guidance_scale=7.5
    ).images[0]

    filename = "engineering_image_" + str(i + 1) + ".png"

    image.save(filename)

    print("Saved:", filename)

# =========================================================
# COMPLETION MESSAGE
# =========================================================

print()
print("==========================================")
print("ALL IMAGES GENERATED SUCCESSFULLY")
print("==========================================")

print()
print("Image 1: engineering_image_1.png")
print("Image 2: engineering_image_2.png")
print("Image 3: engineering_image_3.png")

print()
print("Prompt comparison:")
print("1. Simple prompt -> basic bridge design")
print("2. Detailed prompt -> more specific engineering features")
print("3. Futuristic prompt -> advanced and futuristic features")
