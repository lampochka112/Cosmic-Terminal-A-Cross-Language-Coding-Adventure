
cmake_minimum_required(VERSION 3.15)
project(CosmicTerminalMulti)

set(CMAKE_CXX_STANDARD 17)

# Поиск зависимостей
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(NodeJS REQUIRED)  # Для JavaScript выполнения
find_package(Java REQUIRED)    # Для Java выполнения

# WebAssembly сборка
if(EMSCRIPTEN)
    set(CMAKE_EXECUTABLE_SUFFIX ".js")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -s WASM=1 -s ASSERTIONS=1")
endif()

# Основной исполняемый файл
add_executable(cosmic_terminal_multi 
    src/main.cpp 
    src/game_engine.cpp
    src/terminal_ui.cpp
    src/score_system.cpp
    src/config_loader.cpp
)

# WebAssembly target
add_executable(cosmic_terminal_web src/main.cpp src/game_engine.cpp)
set_target_properties(cosmic_terminal_web PROPERTIES SUFFIX ".html")

# Подключение библиотек
target_link_libraries(cosmic_terminal_multi 
    PRIVATE 
    ${Python3_LIBRARIES}
    pthread
    dl
)

# Установка путей для Python модулей
target_compile_definitions(cosmic_terminal_multi 
    PRIVATE 
    PYTHON_MODULE_PATH="${CMAKE_CURRENT_SOURCE_DIR}/challenges"
)