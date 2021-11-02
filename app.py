from web3 import Web3
import numpy as np
import pandas as pd

#log in
infura_url= 'https://mainnet.infura.io/v3/###########'
web3= Web3(Web3.HTTPProvider (infura_url))

# get latest 100 blocks
blocks_id=[]
latest = web3.eth.blockNumber
for i in range(0, 100):
  blocks= (web3.eth.getBlock(latest - i))
  #print(web3.toHex(blocks.hash))
  blocks_id.append (web3.toHex(blocks.hash))

#get the number of transactions within the blocks
total_txs=[]
for id in blocks_id:
  in_txs= (web3.eth.get_block_transaction_count (id))
  total_txs.append (in_txs)

adresses= []
transaction_index=[]
value= []
block_num = []

d = {'blocks_id':blocks_id,'total_txs':total_txs}
df = pd.DataFrame(d)
#df.head()

for ind in df.index:
  txs=np.arange(0,(df.total_txs[ind]),1)
  block_id=(df.blocks_id[ind])
  for tx in txs:
    try:
      data= (web3.eth.getTransactionByBlock (block_id, str (tx)))
      if (web3.fromWei((data.value),'ether')) > 250:
        adresses.append (data.to)
        transaction_index.append (tx)
        value.append (web3.fromWei((data.value),'ether'))
        block_num. append (data.blockNumber)
    except Exception:
      pass
d2 = {'block_number':block_num, 'transaction_index':transaction_index,'adress':adresses, 'value':value}
df2 = pd.DataFrame(d2)
print (df2)