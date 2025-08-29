class GalacticMap {
private:
    struct StarSystem {
        std::string name;
        Vector3 position;
        std::vector<Challenge> challenges;
        std::vector<std::string> connected_systems;
        bool discovered;
        bool completed;
    };
    
    std::map<std::string, StarSystem> star_systems;
    std::string current_system;
    
public:
    void generate_procedural_galaxy(int seed) {
        std::mt19937 rng(seed);
        std::uniform_real_distribution<float> dist(-1000.0f, 1000.0f);
        
        for (int i = 0; i < 100; ++i) {
            StarSystem system;
            system.name = generate_system_name(rng);
            system.position = {dist(rng), dist(rng), dist(rng)};
            system.discovered = false;
            system.completed = false;
            
            // Генерация challenges для системы
            system.challenges = generate_system_challenges(rng);
            
            star_systems[system.name] = system;
        }
        
        // Создание гипер-переходов между системами
        create_hyperlanes(rng);
    }
    
    void travel_to_system(const std::string& system_name) {
        if (star_systems[system_name].discovered) {
            current_system = system_name;
            trigger_hyperjump_animation();
            load_system_environment(system_name);
        }
    }
    
    void discover_new_system(const std::string& system_name) {
        star_systems[system_name].discovered = true;
        unlock_achievement("explorer_" + system_name);
    }
    
    std::vector<std::string> get_nearby_systems() const {
        std::vector<std::string> nearby;
        Vector3 current_pos = star_systems.at(current_system).position;
        
        for (const auto& [name, system] : star_systems) {
            if (name != current_system && system.discovered) {
                float distance = (system.position - current_pos).length();
                if (distance < 200.0f) {
                    nearby.push_back(name);
                }
            }
        }
        
        return nearby;
    }
};