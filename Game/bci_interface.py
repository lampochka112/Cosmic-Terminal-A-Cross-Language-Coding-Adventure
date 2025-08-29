import brainflow
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class BrainComputerInterface:
    def __init__(self):
        self.board_id = brainflow.BoardIds.CYTON_BOARD
        self.board = brainflow.BoardShim(
            self.board_id,
            brainflow.BoardShim.get_board_descr(self.board_id)
        )
        self.classifier = RandomForestClassifier()
        self.is_trained = False
    
    def start_bci_session(self):
        self.board.prepare_session()
        self.board.start_stream()
    
    def train_mental_commands(self):
        # Обучение мысленным командам
        training_data = []
        labels = []
        
        print("Думай о движении влево...")
        left_data = self.record_mental_activity(5)
        training_data.extend(left_data)
        labels.extend([0] * len(left_data))
        
        print("Думай о движении вправо...")
        right_data = self.record_mental_activity(5)
        training_data.extend(right_data)
        labels.extend([1] * len(right_data))
        
        # Обучение классификатора
        self.classifier.fit(training_data, labels)
        self.is_trained = True
    
    def mental_code_navigation(self):
        # Навигация по коду силой мысли
        while True:
            eeg_data = self.get_recent_eeg_data()
            prediction = self.classifier.predict([eeg_data])
            
            if prediction == 0:  # Мысль "влево"
                self.navigate_code_left()
            elif prediction == 1:  # Мысль "вправо"
                self.navigate_code_right()
    
    def focus_based_difficulty(self):
        # Адаптивная сложность на основе focus игрока
        focus_level = self.measure_player_focus()
        
        if focus_level > 0.8:
            return "hard"
        elif focus_level > 0.5:
            return "medium"
        else:
            return "easy"