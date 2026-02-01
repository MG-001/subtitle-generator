import warnings
import soundcard as sc
import soundfile as sf
import numpy as np

warnings.filterwarnings("ignore", category=sc.SoundcardRuntimeWarning)

SAMPLE_RATE = 48000
CHUNK_SEC = 2
OUTPUT_FILE = r"C:\Users\prave\Work\subtitle-generator\Trail\t_audio_from_pc\system_audio.wav"

speaker = sc.default_speaker()
print("Capturing from speaker:", speaker.name)

mic = sc.get_microphone(speaker.name, include_loopback=True)

# Open the WAV file once in write mode
with mic.recorder(samplerate=SAMPLE_RATE) as recorder, \
     sf.SoundFile(OUTPUT_FILE, mode='w', samplerate=SAMPLE_RATE, channels=2) as file:

    print("Recording system audio... Press Ctrl+C to stop\n")

    try:
        while True:
            chunk = recorder.record(numframes=SAMPLE_RATE * CHUNK_SEC)
            if chunk.size == 0:
                continue

            # Write chunk to WAV
            file.write(chunk)

            # Feedback
            print("Captured chunk:", chunk.shape)

    except KeyboardInterrupt:
        print("\nStopped recording. Saved to:", OUTPUT_FILE)
