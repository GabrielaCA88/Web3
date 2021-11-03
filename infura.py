from web3 import Web3
infura_url= 'https://mainnet.infura.io/v3/#########'
web3= Web3(Web3.HTTPProvider (infura_url))
#connected=web3.isConnected()
#print (connected)
#latest= web3.eth.blockNumber
#print (latest)

#print (web3.eth.getBlock(latest))

hash= '0x129f01b132c06910df2833e007701f83e42054b442908280fe255079ced87037'
data= (web3.eth.getTransactionByBlock (hash,2))
print (data)