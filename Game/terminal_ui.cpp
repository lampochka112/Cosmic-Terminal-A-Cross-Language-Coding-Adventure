class TerminalUI {
public:
    void showWelcomeScreen() {
        clearScreen();
        printAsciiArt("assets/ascii_art/welcome.txt");
        printColored("🌌 COSMIC TERMINAL: MULTI-LANGUAGE ODYSSEY\n", Color::CYAN);
        printColored("=============================================\n", Color::WHITE);
    }
    
    void showLanguageSelection() {
        printColored("\n🎯 Select programming language:\n", Color::YELLOW);
        printColored("1. Python 🐍\n", Color::GREEN);
        printColored("2. C++ ⚡\n", Color::BLUE);
        printColored("3. JavaScript 📜\n", Color::YELLOW);
        printColored("4. Java ☕\n", Color::RED);
        printColored("5. Rust 🦀\n", Color::MAGENTA);
        printColored("Choice: ", Color::WHITE);
    }
    
    void showChallenge(const Challenge& challenge) {
        printColored(f"\n🔓 Level {challenge.level} - {challenge.language}\n", Color::CYAN);
        printColored("----------------------------------------\n", Color::WHITE);
        printColored(challenge.description + "\n\n", Color::WHITE);
        printColored("💻 Your code:\n", Color::GREEN);
    }
    
    void printColored(const std::string& text, Color color) {
        // ANSI коды цветов для терминала
        const std::map<Color, std::string> color_codes = {
            {Color::RED, "\033[31m"},
            {Color::GREEN, "\033[32m"},
            {Color::YELLOW, "\033[33m"},
            {Color::BLUE, "\033[34m"},
            {Color::MAGENTA, "\033[35m"},
            {Color::CYAN, "\033[36m"},
            {Color::WHITE, "\033[37m"}
        };
        std::cout << color_codes[color] << text << "\033[0m";
    }
};