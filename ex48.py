import warnings
import os

warnings.filterwarnings("ignore")

os.environ["TOKENIZERS_PARALLELISM"] = "false"

import torch
import soundfile as sf

from transformers import (
    SpeechT5Processor,
    SpeechT5ForTextToSpeech,
    SpeechT5HifiGan
)

from datasets import load_dataset


# ==========================================================
# ENGINEERING TEXT-TO-SPEECH APPLICATION
# ==========================================================

print("=" * 60)
print("       ENGINEERING TEXT-TO-SPEECH APPLICATION")
print("=" * 60)


# ==========================================================
# SELECT DEVICE
# ==========================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Device:", device)


# ==========================================================
# LOAD PRE-TRAINED SPEECHT5 MODEL
# ==========================================================

print("\nLoading pre-trained SpeechT5 model...")
print("Please wait...")

processor = SpeechT5Processor.from_pretrained(
    "microsoft/speecht5_tts"
)

model = SpeechT5ForTextToSpeech.from_pretrained(
    "microsoft/speecht5_tts"
).to(device)

vocoder = SpeechT5HifiGan.from_pretrained(
    "microsoft/speecht5_hifigan"
).to(device)

print("SpeechT5 model loaded successfully!")


# ==========================================================
# LOAD SPEAKER EMBEDDING
# ==========================================================

print("\nLoading speaker information...")

dataset = load_dataset(
    "Matthijs/cmu-arctic-xvectors",
    split="validation"
)

speaker_embedding = torch.tensor(
    dataset[7306]["xvector"]
).unsqueeze(0).to(device)

print("Speaker information loaded!")


# ==========================================================
# ENGINEERING TEXT
# ==========================================================

text = """
Artificial intelligence is an important field of engineering.
Machine learning allows computers to learn patterns from data.
Engineers use artificial intelligence to develop intelligent
systems, robotics, automation, computer vision, and smart
applications.
"""


# ==========================================================
# DISPLAY TEXT
# ==========================================================

print("\n==============================================")
print("Engineering Text:")
print("==============================================")

print(text)


# ==========================================================
# CONVERT TEXT INTO SPEECH
# ==========================================================

print("\nGenerating natural-sounding speech...")
print("Please wait...")

inputs = processor(
    text=text,
    return_tensors="pt"
)

input_ids = inputs["input_ids"].to(device)

with torch.no_grad():

    speech = model.generate_speech(
        input_ids,
        speaker_embeddings=speaker_embedding,
        vocoder=vocoder
    )


# ==========================================================
# SAVE AUDIO
# ==========================================================

output_file = "engineering_speech.wav"

sf.write(
    output_file,
    speech.cpu().numpy(),
    16000
)


# ==========================================================
# RESULT
# ==========================================================

print("\n==============================================")
print("       TEXT-TO-SPEECH COMPLETED")
print("==============================================")

print("Input text converted successfully.")
print("Audio file saved as:")
print(output_file)

print("\nYou can open engineering_speech.wav")
print("to listen to the generated speech.")
