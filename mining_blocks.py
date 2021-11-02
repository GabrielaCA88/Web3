from web3 import Web3
import numpy as np
import pandas as pd

infura_url= 'https://mainnet.infura.io/v3/#########'
web3= Web3(Web3.HTTPProvider (infura_url))

hash= '0xe4f4a4c234de8f0c52f1257e53e3adcef2d698198385b6110775b830a118550d'
adresses= []
transaction_index=[]
value=[]

total_txs= (web3.eth.get_block_transaction_count (hash))
print (total_txs)
txs=np.arange(0,total_txs,1)

for tx in txs:
  try:
    data= (web3.eth.getTransactionByBlock (hash, str (tx)))
    if (web3.fromWei((data.value),'ether')) > 2:
      adresses.append (data.to)
      transaction_index.append (tx)
      value.append (web3.fromWei((data.value),'ether'))
  except Exception:
    pass

d = {'transaction_index':transaction_index,'adress':adresses, 'value':value}
df = pd.DataFrame(d)
#print (df)