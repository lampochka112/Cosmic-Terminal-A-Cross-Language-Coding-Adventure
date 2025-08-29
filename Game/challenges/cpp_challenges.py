class CppChallenges:
    def __init__(self):
        self.challenges = {
            1: {
                'description': 'Write a function to find max of two numbers (C++)',
                'solution': '''int max(int a, int b) {
    return a > b ? a : b;
}''',
                'test_cases': [(3, 5), (10, 2), (-1, -5)]
            },
            2: {
                'description': 'Template function for sum (C++)',
                'solution': '''template<typename T>
T sum(T a, T b) {
    return a + b;
}''',
                'test_cases': [(2.5, 3.5), (10, 20)]
            }
        }
    
    def check_cpp_solution(self, challenge_id, user_code):
        # Компиляция и выполнение C++ кода
        try:
            import tempfile
            import subprocess
            import os
            
            challenge = self.challenges[int(challenge_id)]
            
            # Создаем временный файл
            with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False) as f:
                f.write(f"""
#include <iostream>
#include <vector>
using namespace std;

{user_code}

int main() {{
    // Тестовые случаи
    vector<pair<int, int>> tests = {{{{(3, 5)}, {(10, 2)}, {(-1, -5)}}}};
    
    for (auto& test : tests) {{
        cout << max(test.first, test.second) << endl;
    }}
    return 0;
}}
""")
                temp_file = f.name
            
            # Компилируем
            compile_result = subprocess.run(['g++', temp_file, '-o', temp_file + '.out'], 
                                          capture_output=True, timeout=10)
            
            if compile_result.returncode == 0:
                # Запускаем
                run_result = subprocess.run([temp_file + '.out'], 
                                          capture_output=True, text=True, timeout=5)
                expected_output = "5\\n10\\n-1\\n"
                if run_result.stdout == expected_output:
                    return True
            
            # Cleanup
            os.unlink(temp_file)
            if os.path.exists(temp_file + '.out'):
                os.unlink(temp_file + '.out')
                
            return False
            
        except Exception as e:
            print(f"C++ execution error: {e}")
            return False