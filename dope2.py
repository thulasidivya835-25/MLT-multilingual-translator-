import fasttext
import os

# Load the pre-trained FastText model
model_path ='D:/fastx/lid.176.bin'
if not os.path.isfile(model_path):
    raise ValueError(f"Model file not found at {model_path}")

model = fasttext.load_model(model_path)

def detect_language_with_fasttext(word):
    predictions = model.predict(word, k=1)  # Top-1 prediction
    lang = predictions[0][0].replace('_label_', '')
    confidence = predictions[1][0]
    return lang, confidence

def detect_language_of_words(input_file, output_file, confidence_threshold=0.8):
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()
    
    words = text.split()
    detected_words = []

    for word in words:
        lang, confidence = detect_language_with_fasttext(word)
        if confidence < confidence_threshold:
            lang = 'und'  # 'und' for undefined language if below confidence threshold
        detected_words.append(f"{word} ({lang})")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(' '.join(detected_words))

# Replace 'input.txt' and 'output.txt' with your file paths
detect_language_of_words('input.txt','output2.txt')