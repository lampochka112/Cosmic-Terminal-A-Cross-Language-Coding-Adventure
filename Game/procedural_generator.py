class ProceduralGenerator:
    def __init__(self):
        self.templates = {
            'python': [
                "Напиши функцию для {operation} {data_structure}",
                "Создай класс для работы с {concept}",
                "Реализуй алгоритм {algorithm} на Python"
            ],
            'cpp': [
                "Оптимизируй код для работы с {hardware}",
                "Напиши шаблонную функцию для {operation}",
                "Реализуй паттерн {design_pattern} на C++"
            ]
        }
        
        self.concepts = {
            'operation': ['сортировки', 'поиска', 'фильтрации', 'трансформации'],
            'data_structure': ['массивов', 'списков', 'деревьев', 'графов'],
            'algorithm': ['быстрой сортировки', 'поиска в ширину', 'диффи-хеллмана'],
            'hardware': ['GPU', 'многопроцессорных систем', 'embedded устройств']
        }
    
    def generate_challenge(self, language, difficulty):
        template = random.choice(self.templates[language])
        challenge = template
        
        for key in self.concepts:
            if f'{{{key}}}' in template:
                replacement = random.choice(self.concepts[key])
                challenge = challenge.replace(f'{{{key}}}', replacement)
        
        # Добавляем сложность
        if difficulty > 1:
            challenge += f" с сложностью O({self.generate_complexity(difficulty)})"
        
        return challenge
    
    def generate_complexity(self, difficulty):
        complexities = ['n', 'n log n', 'n²', '2^n', 'n!']
        return complexities[min(difficulty - 1, len(complexities) - 1)]