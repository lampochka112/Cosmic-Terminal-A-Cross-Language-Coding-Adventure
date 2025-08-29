class SpaceEconomy:
    def __init__(self):
        self.resources = {
            'energy': 100,
            'memory': 512,
            'processing': 2.0,  # GHz
            'quantum_cores': 0
        }
        
        self.market_prices = {
            'energy': 1.0,
            'memory': 0.5,
            'processing': 10.0,
            'quantum_cores': 1000.0
        }
        
        self.player_currency = 1000
    
    def resource_based_coding(self, challenge, code_complexity):
        # Потребление ресурсов при выполнении кода
        energy_cost = code_complexity * 0.1
        memory_cost = len(challenge) * 0.01
        
        if self.resources['energy'] >= energy_cost and self.resources['memory'] >= memory_cost:
            self.resources['energy'] -= energy_cost
            self.resources['memory'] -= memory_cost
            return True
        return False
    
    def upgrade_resources(self, resource_type, amount):
        cost = self.market_prices[resource_type] * amount
        
        if self.player_currency >= cost:
            self.player_currency -= cost
            self.resources[resource_type] += amount
            return True
        return False
    
    def trading_with_npcs(self):
        # Торговая система с NPC
        npc_traders = [
            {
                'name': 'Quantum Merchant',
                'offers': {'quantum_cores': 500, 'energy': -50},
                'demands': {'memory': 100, 'processing': 5.0}
            },
            # ... other traders
        ]
        
        return npc_traders
    
    def economic_crisis_event(self):
        # Случайные экономические события
        events = [
            'energy_crisis',
            'market_crash',
            'technological_breakthrough',
            'alien_trade_embargo'
        ]
        
        event = random.choice(events)
        self.apply_economic_event(event)