class AchievementSystem {
public:
    enum class Achievement {
        FIRST_CODE,
        MULTI_LANGUAGE_MASTER,
        SPEED_RUNNER,
        PERFECT_SCORE,
        BUG_HUNTER
    };
    
    void unlockAchievement(Achievement achievement) {
        achievements[achievement] = true;
        showAchievementPopup(achievement);
    }
    
    void checkLanguageMastery() {
        std::map<ProgrammingLanguage, int> lang_scores;
        for (const auto& score : level_scores) {
            lang_scores[score.language]++;
        }
        
        if (lang_scores.size() >= 3) {
            unlockAchievement(Achievement::MULTI_LANGUAGE_MASTER);
        }
    }
    
private:
    std::map<Achievement, bool> achievements;
    std::vector<std::string> achievement_names = {
        "First Code Execution",
        "Multi-Language Master",
        "Speed Runner",
        "Perfect Score",
        "Bug Hunter"
    };
};