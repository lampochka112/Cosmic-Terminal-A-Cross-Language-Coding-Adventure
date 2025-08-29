cmake_minimum_required(VERSION 3.12)
project(CosmicTerminal)

set(CMAKE_CXX_STANDARD 17)

# Настройка Python
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Добавление исполняемого файла
add_executable(cosmic_terminal src/main.cpp src/game_engine.cpp)

# Подключение Python
target_include_directories(cosmic_terminal PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(cosmic_terminal PRIVATE ${Python3_LIBRARIES})

# Для Windows
if(WIN32)
    target_link_libraries(cosmic_terminal PRIVATE ws2_32)
endif()