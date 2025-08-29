#ifndef GAME_ENGINE_H
#define GAME_ENGINE_H

#include <string>
#include <vector>
#include <functional>

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