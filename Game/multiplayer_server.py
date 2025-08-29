import asyncio
import websockets
import json
from datetime import datetime

class GameServer:
    def __init__(self):
        self.connected_players = {}
        self.leaderboard = []
        self.current_tournament = None
    
    async def handle_connection(self, websocket, path):
        player_id = await websocket.recv()
        self.connected_players[player_id] = {
            'websocket': websocket,
            'score': 0,
            'current_level': 1
        }
        
        try:
            async for message in websocket:
                data = json.loads(message)
                await self.handle_message(data, player_id)
        finally:
            del self.connected_players[player_id]
    
    async def handle_message(self, data, player_id):
        if data['type'] == 'solution_submit':
            is_correct = await self.check_solution(data)
            if is_correct:
                self.connected_players[player_id]['score'] += 100
                self.connected_players[player_id]['current_level'] += 1
                
                # Рассылка обновления лидерборда
                await self.broadcast_leaderboard()
    
    async def broadcast_leaderboard(self):
        leaderboard = sorted(
            [(pid, data['score']) for pid, data in self.connected_players.items()],
            key=lambda x: x[1],
            reverse=True
        )
        
        message = {
            'type': 'leaderboard_update',
            'data': leaderboard
        }
        
        for player_data in self.connected_players.values():
            await player_data['websocket'].send(json.dumps(message))