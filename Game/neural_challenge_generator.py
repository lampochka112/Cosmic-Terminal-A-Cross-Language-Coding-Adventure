import torch
import transformers
from diffusers import StableDiffusionPipeline

class NeuralChallengeGenerator:
    def __init__(self):
        self.model = transformers.AutoModelForCausalLM.from_pretrained(
            "microsoft/CodeGPT-small-py"
        )
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(
            "microsoft/CodeGPT-small-py"
        )
        self.image_pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1"
        )
    
    def generate_ai_challenge(self, language, difficulty, player_style):
        prompt = f"""
        Создай уникальную задачу по программированию на {language} 
        сложности {difficulty}/10. Стиль игрока: {player_style}
        Задача должна быть креативной и обучающей.
        """
        
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_length=200,
            temperature=0.9,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        challenge = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return self.post_process_challenge(challenge)
    
    def generate_visual_representation(self, challenge_text):
        # Генерация изображения для визуализации задачи
        image = self.image_pipe(
            f"programming challenge visualization: {challenge_text}",
            height=512,
            width=512
        ).images[0]
        
        return image
    
    def adaptive_difficulty(self, player_performance):
        # Адаптивная сложность на основе ML
        performance_features = [
            player_performance['accuracy'],
            player_performance['speed'],
            player_performance['code_quality']
        ]
        
        # Простая нейросеть для предсказания оптимальной сложности
        optimal_difficulty = self.difficulty_model(torch.tensor(performance_features))
        return optimal_difficulty.item()