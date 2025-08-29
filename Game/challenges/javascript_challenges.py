class JavaScriptChallenges:
    def __init__(self):
        self.challenges = {
            1: {
                'description': 'Write a function to sum two numbers (JavaScript)',
                'solution': 'function sum(a, b) { return a + b; }',
                'test_cases': [(2, 3), (5, 7), (-1, 1)]
            },
            2: {
                'description': 'Create array map function (JavaScript)',
                'solution': '''function mapArray(arr, fn) {
    return arr.map(fn);
}''',
                'test_cases': [
                    ([1, 2, 3], "x => x * 2"),
                    ([5, 10, 15], "x => x - 1")
                ]
            },
            3: {
                'description': 'Promise-based timer (JavaScript)',
                'solution': '''function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}''',
                'test_cases': [100, 500, 1000]
            }
        }
    
    def check_js_solution(self, challenge_id, user_code):
        # Используем Node.js для выполнения JavaScript
        try:
            import subprocess
            import json
            
            challenge = self.challenges[int(challenge_id)]
            test_code = f"""
            {user_code}
            
            // Тестовые случаи
            const testCases = {json.dumps(challenge['test_cases'])};
            let results = [];
            
            for (const testCase of testCases) {{
                if (Array.isArray(testCase)) {{
                    results.push(sum(...testCase));
                }} else {{
                    results.push('manual_check');
                }}
            }}
            
            console.log(JSON.stringify(results));
            """
            
            result = subprocess.run(['node', '-e', test_code], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                return True
            return False
            
        except Exception as e:
            print(f"JS execution error: {e}")
            return False