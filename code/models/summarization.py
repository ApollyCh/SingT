import os
from dotenv import load_dotenv
from songUnit import Song
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
model_name = "meta-llama/Llama-3.2-1B"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class Summarization:
    def __init__(self, song: Song):
        self.song = song
        self.model = AutoModelForCausalLM.from_pretrained(model_name, token=HF_TOKEN).to(device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_summary(self, text) -> str:
        torch.cuda.empty_cache()

        question = "Summarize the meaning and emotional theme of the song lyrics."

        input_text = f"Song lyrics:\n{text}\n\nQuestion: {question}\nAnswer:"
        inputs = self.tokenizer(input_text, return_tensors="pt").to(device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=100,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.3,
            no_repeat_ngram_size=2
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
