from birdnetlib.analyzer import Analyzer
from birdnetlib import Recording
from datetime import datetime

MIN_CONFIDENCE = 0.01
# Set your sample audio path (we will change this later)
AUDIO_FILE = "../samples/example.wav"

def run_inference():
    print("[INFO] Loading model...")
    analyzer = Analyzer()

    print(f"[INFO] Loading audio file: {AUDIO_FILE}")
    recording = Recording(
        analyzer,
        AUDIO_FILE,
        lat=43.6532,   # Toronto lat
        lon=-79.3832,  # Toronto lon
        date=datetime.now()
    )

    
    recording.analyze()

    print("\n✅ Results:")
    detections = recording.detections

    if not detections:
        print("No birds detected.")
        return

    for result in detections:
        species = result["common_name"]
        conf = result["confidence"]

        if conf >= MIN_CONFIDENCE:
            print(f"{species} ({conf:.2f})")

if __name__ == "__main__":
    run_inference()
