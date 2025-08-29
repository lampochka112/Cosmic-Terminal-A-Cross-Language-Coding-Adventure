class QuestSystem:
    def __init__(self):
        self.quests = {
            'first_code': {
                'title': 'Первый контакт',
                'description': 'Напиши свою первую программу на любом языке',
                'reward': 100,
                'completed': False
            },
            'polyglot': {
                'title': 'Полиглот',
                'description': 'Реши задачи на 3 разных языках программирования',
                'reward': 300,
                'completed': False
            },
            'speedrunner': {
                'title': 'Спидраннер',
                'description': 'Пройди 5 уровней менее чем за 10 минут',
                'reward': 500,
                'completed': False
            }
        }
        
        self.current_story_chapter = 1
        self.story_chapters = {
            1: "Вы - новый стажер на космической станции 'Кодекс'. Система ИИ вышла из-под контроля...",
            2: "Вы обнаружили, что саботаж устроил бывший lead developer...",
            3: "Путешествие к ядру системы для финального противостояния..."
        }
    
    def check_quest_completion(self, player_stats):
        completed_quests = []
        
        if not self.quests['first_code']['completed'] and player_stats['total_solutions'] > 0:
            self.quests['first_code']['completed'] = True
            completed_quests.append('first_code')
        
        if not self.quests['polyglot']['completed'] and len(player_stats['languages_used']) >= 3:
            self.quests['polyglot']['completed'] = True
            completed_quests.append('polyglot')
        
        return completed_quests
    
    def get_story_dialog(self, chapter, character):
        dialogs = {
            'ai_core': [
                "Приветствую, программист. Система нестабильна...",
                "Мне нужна твоя помощь чтобы восстановить контроль...",
                "Будь осторожен - кто-то намеренно сломал меня..."
            ],
            'villain': [
                "Так-так, кто это у нас здесь? Еще один герой?",
                "Ты никогда не починишь систему! Я все предусмотрел!",
                "Посмотрим, справишься ли ты с моими последними головоломками..."
            ]
        }
        
        return dialogs.get(character, [])[chapter - 1]