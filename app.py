import whisper

model = whisper.load_model("base")
result = model.transcribe("./Audio_Jeimmy.mp3")
print(result["text"])