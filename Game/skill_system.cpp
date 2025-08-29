class SkillSystem {
public:
    enum class SkillType {
        CODING_SPEED,
        DEBUGGING,
        ALGORITHMS,
        MEMORY_MANAGEMENT,
        CONCURRENCY
    };
    
    struct Skill {
        SkillType type;
        std::string name;
        std::string description;
        int current_level;
        int max_level;
        std::vector<int> upgrade_costs;
    };
    
    void addExperience(SkillType skill, int exp) {
        skills[skill].experience += exp;
        checkLevelUp(skill);
    }
    
    void applySkillEffects(ChallengeResult& result) {
        for (const auto& [skill, data] : skills) {
            if (data.current_level > 0) {
                switch (skill) {
                    case SkillType::CODING_SPEED:
                        result.time_bonus += data.current_level * 0.1;
                        break;
                    case SkillType::DEBUGGING:
                        result.error_tolerance += data.current_level * 0.05;
                        break;
                    case SkillType::ALGORITHMS:
                        result.score_multiplier += data.current_level * 0.02;
                        break;
                }
            }
        }
    }
    
private:
    std::map<SkillType, SkillData> skills;
};