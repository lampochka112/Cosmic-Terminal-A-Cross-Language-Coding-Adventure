# Блокчейн система достижений и NFT наград
from web3 import Web3
import json

class BlockchainRewards:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_RPC_URL')))
        self.contract_address = os.getenv('REWARDS_CONTRACT_ADDRESS')
        
        with open('abi/RewardsContract.json') as f:
            contract_abi = json.load(f)
        
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=contract_abi
        )
    
    def mint_achievement_nft(self, player_wallet, achievement_id):
        # Минт NFT за достижение
        nonce = self.w3.eth.getTransactionCount(player_wallet)
        
        transaction = self.contract.functions.mintAchievement(
            player_wallet,
            achievement_id
        ).buildTransaction({
            'gas': 200000,
            'gasPrice': self.w3.toWei('50', 'gwei'),
            'nonce': nonce,
        })
        
        signed_txn = self.w3.eth.account.signTransaction(
            transaction, 
            private_key=os.getenv('CONTRACT_PRIVATE_KEY')
        )
        
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return tx_hash.hex()
    
    def get_player_nfts(self, player_wallet):
        # Получение NFT коллекции игрока
        nft_count = self.contract.functions.balanceOf(player_wallet).call()
        nfts = []
        
        for i in range(nft_count):
            token_id = self.contract.functions.tokenOfOwnerByIndex(player_wallet, i).call()
            metadata_uri = self.contract.functions.tokenURI(token_id).call()
            nfts.append({'token_id': token_id, 'metadata_uri': metadata_uri})
        
        return nfts
    
    def create_marketplace_listing(self, token_id, price):
        # Размещение NFT на маркетплейсе
        # ... implementation ...