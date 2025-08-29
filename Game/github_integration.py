class GitHubIntegration:
    def __init__(self):
        self.gh = github.Github(os.getenv('GITHUB_TOKEN'))
        self.user_repo = None
    
    def create_github_repository(self, username):
        try:
            repo_name = f"cosmic-terminal-solutions-{username}"
            self.user_repo = self.gh.get_user().create_repo(
                repo_name,
                description="Мои решения задач из Cosmic Terminal",
                private=False
            )
            return True
        except:
            return False
    
    def push_solution(self, challenge_id, solution_code, language):
        if self.user_repo:
            filename = f"solutions/{challenge_id}_{language}.{self.get_file_extension(language)}"
            self.user_repo.create_file(
                filename,
                f"Add solution for {challenge_id}",
                solution_code
            )
    
    def get_community_solutions(self, challenge_id):
        # Поиск решений других игроков
        query = f"cosmic-terminal {challenge_id} in:name,description"
        repos = self.gh.search_repositories(query)
        
        solutions = []
        for repo in repos[:5]:  # Top 5 results
            solutions.append({
                'username': repo.owner.login,
                'repo_url': repo.html_url,
                'stars': repo.stargazers_count
            })
        
        return solutions