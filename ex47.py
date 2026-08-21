import warnings
import os

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import sounddevice as sd
from scipy.io.wavfile import write
from transformers import pipeline
import torch


# ==========================================================
# SPEECH-TO-TEXT ENGINEERING QUERY APPLICATION
# ==========================================================

print("=" * 60)
print("       ENGINEERING SPEECH-TO-TEXT APPLICATION")
print("=" * 60)

# ----------------------------------------------------------
# SELECT CPU OR GPU
# ----------------------------------------------------------

device = 0 if torch.cuda.is_available() else -1

if device == 0:
    print("Device: GPU")
else:
    print("Device: CPU")


# ----------------------------------------------------------
# LOAD PRE-TRAINED WHISPER MODEL
# ----------------------------------------------------------

print("\nLoading pre-trained Whisper model...")
print("Please wait...")

speech_to_text = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny",
    device=device
)

print("Model loaded successfully!")


# ----------------------------------------------------------
# RECORD AUDIO
# ----------------------------------------------------------

sample_rate = 16000
duration = 8

print("\n==============================================")
print("Speak your engineering-related query.")
print("Example: What is artificial intelligence?")
print("Recording will continue for 8 seconds.")
print("==============================================")

input("\nPress ENTER to start recording...")

print("\nRecording... Speak now!")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32"
)

sd.wait()

print("Recording completed.")


# ----------------------------------------------------------
# SAVE AUDIO
# ----------------------------------------------------------

audio_file = "engineering_query.wav"

write(
    audio_file,
    sample_rate,
    audio
)

print("Audio saved as:", audio_file)


# ----------------------------------------------------------
# CONVERT SPEECH TO TEXT
# ----------------------------------------------------------

print("\nConverting speech into text...")

result = speech_to_text(
    audio_file
)

text = result["text"].strip()


# ----------------------------------------------------------
# DISPLAY RESULT
# ----------------------------------------------------------

print("\n==============================================")
print("           SPEECH-TO-TEXT RESULT")
print("==============================================")

print("Engineering Query:")
print(text)

print("==============================================")
