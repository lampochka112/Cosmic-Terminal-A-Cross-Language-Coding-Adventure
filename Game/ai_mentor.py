import openai
import os

class AIMentor:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.history = []
    
    def get_hint(self, challenge_description, user_code, language):
        prompt = f"""
        Ты - AI ментор в программистской игре. Дай небольшую подсказку для решения задачи.
        Язык: {language}
        Задача: {challenge_description}
        Код пользователя: {user_code}
        
        Дай небольшую подсказку, не раскрывая полное решение.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            return response.choices[0].message.content
        except:
            return "Подсказка: Попробуй использовать основные конструкции языка..."
    
    def code_review(self, user_code, language):
        prompt = f"""
        Сделай краткий code review на 2-3 предложения для кода на {language}:
        {user_code}
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            return response.choices[0].message.content
        except:
            return "Code review: Код выглядит неплохо, продолжай в том же духе!"