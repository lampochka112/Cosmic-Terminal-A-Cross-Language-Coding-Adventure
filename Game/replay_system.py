class ReplaySystem:
    def __init__(self):
        self.recording_sessions = {}
        self.max_replays = 1000
    
    def start_recording(self, session_id):
        self.recording_sessions[session_id] = {
            'keystrokes': [],
            'timestamps': [],
            'code_versions': [],
            'start_time': time.time()
        }
    
    def record_keystroke(self, session_id, key, code_snapshot):
        if session_id in self.recording_sessions:
            self.recording_sessions[session_id]['keystrokes'].append(key)
            self.recording_sessions[session_id]['timestamps'].append(time.time())
            self.recording_sessions[session_id]['code_versions'].append(code_snapshot)
    
    def generate_learning_insights(self, session_id):
        replay_data = self.recording_sessions.get(session_id, {})
        insights = []
        
        # Анализ стиля coding
        typing_speed = self.calculate_typing_speed(replay_data)
        if typing_speed < 30:
            insights.append("Попробуй печатать быстрее!")
        
        # Анализ частых ошибок
        common_errors = self.find_common_errors(replay_data)
        if common_errors:
            insights.append(f"Частые ошибки: {', '.join(common_errors)}")
        
        # Анализ эффективности решения
        efficiency = self.calculate_efficiency(replay_data)
        insights.append(f"Эффективность решения: {efficiency}%")
        
        return insights