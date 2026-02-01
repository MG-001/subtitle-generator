##### Libraries
from moviepy import VideoFileClip
from faster_whisper import WhisperModel
from pathlib import Path

# Get the path of the current script (repo folder)
REPO_PATH = Path(__file__).parent.resolve()

# Example usage
input_mp4 = REPO_PATH / "sample video.mp4"
output_wav = REPO_PATH / "sample audio.wav"
VideoFileClip(input_mp4).audio.write_audiofile(output_wav) # wav is good for transcription
##### Transcription
#### Load Model
model = WhisperModel("small", device="cpu")
print("Model loaded successfully")
#### Detect language
segments, info = model.transcribe(output_wav)
print("Detected language:", info.language)

### Content
for seg in segments:
    start = f"{seg.start:.2f}s"
    end = f"{seg.end:.2f}s"
    text = seg.text.strip()
    print(f"[{start} → {end}] {text}")
    print("\n")