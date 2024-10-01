import torch
from demucs import pretrained
from demucs.apply import apply_model
import torchaudio
import os
import whisper

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class LyricExtraction:

    def __init__(self, file):
        self.file = file
        self.output_folder = "vocals"
        self.lyric_file = f"{os.path.basename(self.file).replace('.mp3', '_vocals.wav')}"

    def convert_to_stereo(self, target_samplerate):
        wav, sr = torchaudio.load(self.file, normalize=True)

        if sr != target_samplerate:
            wav = torchaudio.transforms.Resample(orig_freq=sr, new_freq=target_samplerate)(wav)

        if wav.shape[0] == 1:
            wav = torch.cat([wav, wav], dim=0)
        return wav

    def extract_vocals(self):
        model = pretrained.get_model('mdx_extra')
        model.cuda()

        wav = self.convert_to_stereo(model.samplerate)

        sources = apply_model(model, wav[None], device=device)
        vocals = sources[0, 3].cpu().numpy()  # Index 3 corresponds to vocals in 'mdx_extra'

        output_path = os.path.join(
            self.output_folder,
            self.lyric_file,
        )

        torchaudio.save(output_path, torch.tensor(vocals), sample_rate=model.samplerate)
        print(f"Vocal part saved: {output_path}")

    def extract_lyrics(self):
        model = whisper.load_model("medium")

        lyric = model.transcribe(self.lyric_file)

        return lyric
