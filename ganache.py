from web3 import Web3
ganache_url = 'HTTP://127.0.0.1:7545'
web3= Web3(Web3.HTTPProvider (ganache_url))
connected=web3.isConnected()
#print (connected)
account1= '0x7cC942Ede93b7ebFc083D9e3dDEf42BE2FfD1EF0'
account2= '0x19174c89D091B91556F8C5Ae029AF3DCBbf12615'

private_key= 'd8c7e49db31a03c5483ea48cd6c754d57bbf26392a51dd4fba3139cff68e10a9'

#get the nance
nonce= web3.eth.getTransactionCount(account1)
#build the transaction
tx={'nonce':nonce,
    'to': account2,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000,
    'gasPrice': web3.toWei('50','gwei')
}
#sign the transaction
signed_tx=web3.eth.account.signTransaction(tx, private_key)
#send the transaction
tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#get a transaction hash
print(tx_hash)
print (web3.toHex(tx_hash))
