#ifndef GAME_ENGINE_H
#define GAME_ENGINE_H

#include <string>
#include <vector>
#include <functional>

enum class ProgrammingLanguage {
    PYTHON,
    CPP,
    JAVASCRIPT,
    JAVA, 
    RUST,
    GO,
    LUA,
    BASH
};

class MultiLanguageEngine {
public:
    std::string generateChallenge(ProgrammingLanguage lang, int level);
    bool checkSolution(ProgrammingLanguage lang, const std::string& challenge_id, 
                     const std::string& solution);
    
    void setLanguagePreference(ProgrammingLanguage lang);
    ProgrammingLanguage detectLanguage(const std::string& code);
    
private:
    std::unordered_map<ProgrammingLanguage, std::string> language_modules = {
        {ProgrammingLanguage::PYTHON, "python_challenges"},
        {ProgrammingLanguage::CPP, "cpp_challenges"},
        {ProgrammingLanguage::JAVASCRIPT, "javascript_challenges"},
        {ProgrammingLanguage::JAVA, "java_challenges"},
        {ProgrammingLanguage::RUST, "rust_challenges"},
        {ProgrammingLanguage::GO, "go_challenges"}
    };
};

class GameEngine {
public:
    GameEngine();
    ~GameEngine();
    
    void initialize();
    void run();
    void shutdown();
    
    // Взаимодействие с Python
    std::string getPythonChallenge(int level);
    bool checkPythonSolution(const std::string& challenge_id, 
                           const std::string& solution);
    
    // Состояние игры
    int getCurrentLevel() const;
    int getScore() const;
    bool isGameComplete() const;
    
private:
    int current_level;
    int score;
    bool game_running;
    
    void renderTerminal();
    void processInput();
    void showChallenge();
    void showVictory();
    
    std::vector<std::string> terminal_history;
};

#endif // GAME_ENGINE_H