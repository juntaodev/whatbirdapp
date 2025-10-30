from birdnetlib.analyzer import Analyzer

print("[INFO] Triggering BirdNET model download...")
analyzer = Analyzer()
print("[INFO] Model downloaded.")
print("[INFO] Model location:", analyzer.model_path)
