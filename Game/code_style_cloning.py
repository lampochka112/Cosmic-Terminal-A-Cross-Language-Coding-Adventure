class CodeStyleCloner:
    def __init__(self):
        self.style_profiles = {}
        self.vectorizer = TfidfVectorizer()
        self.style_model = NearestNeighbors(n_neighbors=3)
    
    def analyze_player_style(self, player_id, code_samples):
        # Анализ стиля coding игрока
        features = self.extract_style_features(code_samples)
        self.style_profiles[player_id] = {
            'features': features,
            'preferred_patterns': self.detect_patterns(code_samples),
            'efficiency_metrics': self.calculate_efficiency(code_samples)
        }
    
    def clone_top_player_style(self, target_player_id, top_player_id):
        # Клонирование стиля топ-игрока
        target_style = self.style_profiles[target_player_id]
        top_style = self.style_profiles[top_player_id]
        
        recommendations = []
        
        # Рекомендации по улучшению стиля
        for pattern in top_style['preferred_patterns']:
            if pattern not in target_style['preferred_patterns']:
                recommendations.append({
                    'type': 'pattern_adoption',
                    'pattern': pattern,
                    'examples': top_style['pattern_examples'][pattern]
                })
        
        # Рекомендации по эффективности
        efficiency_gap = top_style['efficiency_metrics'] - target_style['efficiency_metrics']
        if efficiency_gap > 0.1:
            recommendations.append({
                'type': 'efficiency_improvement',
                'gap': efficiency_gap,
                'suggestions': self.generate_efficiency_suggestions()
            })
        
        return recommendations
    
    def generate_personalized_challenges(self, player_id):
        # Генерация challenges based on player's style gaps
        player_style = self.style_profiles[player_id]
        weaknesses = self.identify_weaknesses(player_style)
        
        return [
            self.create_targeted_challenge(weakness)
            for weakness in weaknesses[:3]  # Top 3 weaknesses
        ]