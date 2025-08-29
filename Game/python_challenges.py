import random
import sys

class ChallengeSystem:
    def __init__(self):
        self.challenges = {
            1: {
                'description': 'Write a Python function to add two numbers',
                'solution': 'def add(a, b): return a + b',
                'test_cases': [(1, 2), (5, 3), (-1, 1)]
            },
            2: {
                'description': 'Create a function to reverse a string',
                'solution': 'def reverse_string(s): return s[::-1]',
                'test_cases': ['hello', 'world', 'python']
            },
            3: {
                'description': 'Write a function to find the factorial of a number',
                'solution': '''def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)''',
                'test_cases': [0, 1, 5, 7]
            },
            4: {
                'description': 'Create a function that returns Fibonacci sequence up to n',
                'solution': '''def fibonacci(n):
    a, b = 0, 1
    result = []
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result''',
                'test_cases': [5, 10, 20]
            },
            5: {
                'description': 'Write a function to check if a string is a palindrome',
                'solution': '''def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]''',
                'test_cases': ['radar', 'hello', 'A man a plan a canal Panama']
            }
        }
    
    def generate_challenge(self, level):
        if level in self.challenges:
            challenge = self.challenges[level]
            return f"Level {level}: {challenge['description']}"
        return "No challenge available for this level"
    
    def check_solution(self, level_str, user_code):
        try:
            level = int(level_str)
            if level not in self.challenges:
                return False
            
            challenge = self.challenges[level]
            
            # Создаем локальное пространство имен для выполнения
            local_namespace = {}
            
            # Выполняем код пользователя
            exec(user_code, {}, local_namespace)
            
            # Ищем функцию (обычно первая функция в коде)
            user_function = None
            for obj in local_namespace.values():
                if callable(obj):
                    user_function = obj
                    break
            
            if not user_function:
                return False
            
            # Тестируем на тестовых случаях
            for test_case in challenge['test_cases']:
                if isinstance(test_case, tuple):
                    result = user_function(*test_case)
                else:
                    result = user_function(test_case)
                
                # Сравниваем с ожидаемым результатом
                exec(challenge['solution'], {}, local_namespace)
                expected_function = None
                for obj in local_namespace.values():
                    if callable(obj):
                        expected_function = obj
                        break
                
                if expected_function:
                    if isinstance(test_case, tuple):
                        expected_result = expected_function(*test_case)
                    else:
                        expected_result = expected_function(test_case)
                    
                    if result != expected_result:
                        return False
            
            return True
            
        except Exception as e:
            print(f"Error checking solution: {e}", file=sys.stderr)
            return False

# Глобальный экземпляр для C++ bridge
challenge_system = ChallengeSystem()

def generate_challenge(level):
    return challenge_system.generate_challenge(level)

def check_solution(level, user_code):
    return challenge_system.check_solution(level, user_code)