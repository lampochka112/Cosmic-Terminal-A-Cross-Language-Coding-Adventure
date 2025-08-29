#include "game_engine.h"
#include <iostream>
#include <cstdlib>
#include <Python.h>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

GameEngine::GameEngine() : current_level(1), score(0), game_running(false) {}

GameEngine::~GameEngine() {
    shutdown();
}

void GameEngine::initialize() {
    // Инициализация Python
    Py_Initialize();
    
    // Добавление пути к Python модулям
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./challenges')");
    
    std::cout << "🚀 Cosmic Terminal Initialized!" << std::endl;
    std::cout << "📡 Connecting to Python interpreter..." << std::endl;
    
    game_running = true;
}

void GameEngine::shutdown() {
    Py_Finalize();
    std::cout << "👋 Game shutdown complete." << std::endl;
}

std::string GameEngine::getPythonChallenge(int level) {
    PyObject *pModule, *pFunc, *pArgs, *pValue;
    
    try {
        pModule = PyImport_ImportModule("python_challenges");
        if (pModule == nullptr) {
            PyErr_Print();
            return "Error: Python module not found";
        }
        
        pFunc = PyObject_GetAttrString(pModule, "generate_challenge");
        if (pFunc && PyCallable_Check(pFunc)) {
            pArgs = PyTuple_New(1);
            PyTuple_SetItem(pArgs, 0, PyLong_FromLong(level));
            
            pValue = PyObject_CallObject(pFunc, pArgs);
            
            if (pValue != nullptr) {
                std::string result = PyUnicode_AsUTF8(pValue);
                Py_DECREF(pValue);
                Py_DECREF(pArgs);
                Py_DECREF(pFunc);
                Py_DECREF(pModule);
                return result;
            }
        }
        
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
        return "Error: Failed to generate challenge";
    }
    catch (...) {
        return "Error: Exception in Python bridge";
    }
}

bool GameEngine::checkPythonSolution(const std::string& challenge_id, 
                                   const std::string& solution) {
    PyObject *pModule, *pFunc, *pArgs, *pResult;
    
    try {
        pModule = PyImport_ImportModule("python_challenges");
        if (pModule == nullptr) return false;
        
        pFunc = PyObject_GetAttrString(pModule, "check_solution");
        if (pFunc && PyCallable_Check(pFunc)) {
            pArgs = PyTuple_New(2);
            PyTuple_SetItem(pArgs, 0, PyUnicode_FromString(challenge_id.c_str()));
            PyTuple_SetItem(pArgs, 1, PyUnicode_FromString(solution.c_str()));
            
            pResult = PyObject_CallObject(pFunc, pArgs);
            
            if (pResult != nullptr && PyBool_Check(pResult)) {
                bool result = PyLong_AsLong(pResult);
                Py_DECREF(pResult);
                Py_DECREF(pArgs);
                Py_DECREF(pFunc);
                Py_DECREF(pModule);
                return result;
            }
        }
        
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
        return false;
    }
    catch (...) {
        return false;
    }
}

void GameEngine::run() {
    initialize();
    
    std::cout << "\n🌌 WELCOME TO COSMIC TERMINAL" << std::endl;
    std::cout << "🎯 Your mission: Hack the ship's systems" << std::endl;
    std::cout << "💻 Solve coding challenges to progress" << std::endl;
    std::cout << "========================================" << std::endl;
    
    while (game_running && current_level <= 5) {
        std::cout << "\n🚪 Level " << current_level << " - System Access Required" << std::endl;
        std::cout << "----------------------------------------" << std::endl;
        
        std::string challenge = getPythonChallenge(current_level);
        std::cout << "\n🔓 Challenge: " << challenge << std::endl;
        
        std::cout << "\n💬 Your solution: ";
        std::string solution;
        std::getline(std::cin, solution);
        
        if (checkPythonSolution(std::to_string(current_level), solution)) {
            std::cout << "✅ Access granted! System compromised." << std::endl;
            score += 100;
            current_level++;
            
            if (current_level <= 5) {
                std::cout << "\n⬆️  Moving to next security level..." << std::endl;
            }
        } else {
            std::cout << "❌ Access denied! Try again." << std::endl;
        }
        
        // Небольшая пауза для эффекта
        #ifdef _WIN32
        Sleep(1000);
        #else
        sleep(1);
        #endif
    }
    
    if (current_level > 5) {
        showVictory();
    }
    
    shutdown();
}

void GameEngine::showVictory() {
    std::cout << "\n🎉 CONGRATULATIONS! MISSION COMPLETE" << std::endl;
    std::cout << "========================================" << std::endl;
    std::cout << "🏆 Final Score: " << score << " points" << std::endl;
    std::cout << "🛸 Ship systems: FULLY COMPROMISED" << std::endl;
    std::cout << "👨‍💻 You are now the master of this vessel!" << std::endl;
}

int GameEngine::getCurrentLevel() const { return current_level; }
int GameEngine::getScore() const { return score; }
bool GameEngine::isGameComplete() const { return current_level > 5; }

// Главная функция
int main() {
    GameEngine game;
    game.run();
    return 0;
}