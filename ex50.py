import os
import PyPDF2
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ============================================================
# MACHINE TRANSLATION APPLICATION
# English Engineering Document -> Indian Language
# ============================================================

# Models for different Indian languages
MODELS = {
    "Hindi": "ai4bharat/indictrans2-en-indic-1B",
    "Tamil": "ai4bharat/indictrans2-en-indic-1B",
    "Telugu": "ai4bharat/indictrans2-en-indic-1B",
    "Kannada": "ai4bharat/indictrans2-en-indic-1B",
    "Malayalam": "ai4bharat/indictrans2-en-indic-1B",
    "Bengali": "ai4bharat/indictrans2-en-indic-1B",
    "Marathi": "ai4bharat/indictrans2-en-indic-1B",
    "Gujarati": "ai4bharat/indictrans2-en-indic-1B",
    "Punjabi": "ai4bharat/indictrans2-en-indic-1B",
}

# IndicTrans2 language codes
LANGUAGE_CODES = {
    "Hindi": "hin_Deva",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Bengali": "ben_Beng",
    "Marathi": "mar_Deva",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
}

# Model cache
model_cache = {}


# ============================================================
# LOAD MODEL
# ============================================================

def load_model(language):

    if language in model_cache:
        return model_cache[language]

    print("Loading translation model...")

    model_name = MODELS[language]

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    model_cache[language] = (tokenizer, model)

    print("Model loaded successfully.")

    return tokenizer, model


# ============================================================
# EXTRACT TEXT FROM PDF
# ============================================================

def extract_text_from_pdf(pdf_file):

    if pdf_file is None:
        return ""

    try:
        reader = PyPDF2.PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        return "ERROR: " + str(e)


# ============================================================
# SPLIT LONG TEXT
# ============================================================

def split_text(text, max_chars=1000):

    paragraphs = text.split("\n")

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if len(current_chunk) + len(paragraph) <= max_chars:

            current_chunk += paragraph + "\n"

        else:

            if current_chunk:
                chunks.append(current_chunk)

            current_chunk = paragraph + "\n"

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


# ============================================================
# TRANSLATE TEXT
# ============================================================

def translate_text(text, language):

    if not text.strip():
        return "No text found."

    try:

        tokenizer, model = load_model(language)

        target_language = LANGUAGE_CODES[language]

        chunks = split_text(text)

        translated_chunks = []

        for chunk in chunks:

            # Add target language token
            input_text = f"{chunk}"

            inputs = tokenizer(
                input_text,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512
            )

            # Generate translation
            outputs = model.generate(
                **inputs,
                max_length=512,
                num_beams=5,
                early_stopping=True
            )

            translated = tokenizer.batch_decode(
                outputs,
                skip_special_tokens=True
            )[0]

            translated_chunks.append(translated)

        return "\n\n".join(translated_chunks)

    except Exception as e:

        return "Translation Error:\n" + str(e)


# ============================================================
# PROCESS PDF
# ============================================================

def translate_pdf(pdf_file, language):

    if pdf_file is None:
        return "Please upload an engineering PDF document."

    print("Reading PDF...")

    text = extract_text_from_pdf(pdf_file)

    if text.startswith("ERROR"):
        return text

    if not text.strip():
        return "No readable text was found in the PDF."

    print("Text extracted successfully.")

    print("Starting translation...")

    translated_text = translate_text(
        text,
        language
    )

    return translated_text


# ============================================================
# SAVE TRANSLATED TEXT
# ============================================================

def save_translation(text):

    if not text.strip():
        return None

    output_file = "translated_engineering_document.txt"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    return output_file


# ============================================================
# GRADIO APPLICATION
# ============================================================

with gr.Blocks(
    title="Engineering Document Machine Translation"
) as app:

    gr.Markdown(
        """
        # 🌐 Engineering Document Machine Translation

        Upload an **English engineering PDF** and translate it
        into an Indian language using a **pre-trained IndicTrans2
        translation model**.
        """
    )

    with gr.Row():

        pdf_input = gr.File(
            label="Upload English Engineering PDF",
            file_types=[".pdf"],
            type="filepath"
        )

        language_input = gr.Dropdown(
            choices=list(LANGUAGE_CODES.keys()),
            value="Tamil",
            label="Select Indian Language"
        )

    translate_button = gr.Button(
        "🚀 Translate Document"
    )

    output_text = gr.Textbox(
        label="Translated Engineering Document",
        lines=25
    )

    download_button = gr.Button(
        "💾 Save Translation"
    )

    download_file = gr.File(
        label="Download Translated Text"
    )

    translate_button.click(
        fn=translate_pdf,
        inputs=[
            pdf_input,
            language_input
        ],
        outputs=output_text
    )

    download_button.click(
        fn=save_translation,
        inputs=output_text,
        outputs=download_file
    )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("ENGINEERING DOCUMENT MACHINE TRANSLATION")
    print("=" * 60)

    print("Starting application...")

    app.launch()
