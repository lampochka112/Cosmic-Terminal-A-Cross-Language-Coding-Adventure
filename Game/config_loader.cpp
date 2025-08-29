class ConfigLoader {
public:
    void loadConfig(const std::string& filename) {
        try {
            auto config = YAML::LoadFile(filename);
            
            difficulty = config["difficulty"].as<std::string>();
            enable_sound = config["sound"]["enabled"].as<bool>();
            language_preferences = config["languages"].as<std::vector<std::string>>();
            timeout_settings = config["timeouts"].as<std::map<std::string, int>>();
            
        } catch (const std::exception& e) {
            std::cerr << "Config loading error: " << e.what() << std::endl;
            loadDefaultConfig();
        }
    }
    
    int getTimeoutForLanguage(ProgrammingLanguage lang) {
        std::string lang_name = languageToString(lang);
        return timeout_settings[lang_name];
    }
};