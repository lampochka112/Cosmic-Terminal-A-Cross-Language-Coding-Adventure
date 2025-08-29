class ModSystem:
    def __init__(self):
        self.loaded_mods = []
        self.mod_directory = "mods/"
    
    def load_mods(self):
        for mod_file in os.listdir(self.mod_directory):
            if mod_file.endswith('.json'):
                with open(os.path.join(self.mod_directory, mod_file)) as f:
                    mod_data = json.load(f)
                    self.loaded_mods.append(mod_data)
    
    def apply_mods(self, game_state):
        for mod in self.loaded_mods:
            if 'challenges' in mod:
                game_state['challenges'].extend(mod['challenges'])
            
            if 'languages' in mod:
                game_state['available_languages'].extend(mod['languages'])
            
            if 'skills' in mod:
                game_state['skills'].update(mod['skills'])
    
    def create_mod_template(self):
        return {
            "name": "Новый мод",
            "version": "1.0.0",
            "author": "Ваше имя",
            "challenges": [],
            "languages": [],
            "skills": {},
            "dependencies": []
        }