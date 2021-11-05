from web3 import Web3

infura_url= 'https://mainnet.infura.io/v3/#######'
web3= Web3(Web3.HTTPProvider (infura_url))

# get latest 10 blocks
blocks_id=[]
latest = web3.eth.blockNumber
for i in range(0, 10):
  blocks= (web3.eth.getBlock(latest - i))
  #print(web3.toHex(blocks.hash))
  blocks_id.append (web3.toHex(blocks.hash))

print (blocks_id)
