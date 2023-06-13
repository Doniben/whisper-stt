import whisper

model = whisper.load_model("large")
result = model.transcribe("Ashley12-06.mp4") # Agregar audio
print(result["text"])