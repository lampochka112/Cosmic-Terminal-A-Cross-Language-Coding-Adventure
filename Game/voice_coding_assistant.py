import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import openai

class VoiceCodingAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_engine = pyttsx3.init()
        self.voice_commands = self.load_voice_commands()
    
    def load_voice_commands(self):
        return {
            "напиши функцию": self.handle_write_function,
            "исправь ошибку": self.handle_fix_error,
            "оптимизируй код": self.handle_optimize_code,
            "сгенерируй тесты": self.handle_generate_tests,
            "объясни код": self.handle_explain_code
        }
    
    def listen_for_commands(self):
        with self.microphone as source:
            print("Слушаю команды...")
            audio = self.recognizer.listen(source)
        
        try:
            command = self.recognizer.recognize_google(audio, language="ru-RU")
            print(f"Распознано: {command}")
            return self.process_command(command.lower())
        except sr.UnknownValueError:
            return "Не понял команду"
        except sr.RequestError:
            return "Ошибка сервиса распознавания"
    
    def process_command(self, command):
        for voice_cmd, handler in self.voice_commands.items():
            if voice_cmd in command:
                return handler(command)
        return "Команда не распознана"
    
    def handle_write_function(self, command):
        # Анализ команды и генерация кода через AI
        function_description = command.replace("напиши функцию", "").strip()
        ai_generated_code = self.generate_code_with_ai(function_description)
        return f"Сгенерирован код: {ai_generated_code}"
    
    def speak_response(self, text):
        # Озвучивание ответа
        tts = gTTS(text=text, lang='ru')
        tts.save("response.mp3")
        os.system("afplay response.mp3")  # For macOS