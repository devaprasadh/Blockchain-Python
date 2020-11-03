# creating a blockchain
# needs a class block
# a block contains the hash of the previous block and its own transaction

from block import Block

blockchain = []

genesis_block = Block("there is no previous hash",["a sent b 7 btc","b sent c 8 btc"])
block1 = Block("genesis_block.block_hash",["w sent y 3 btc","q sent r 9 btc"])

print(block1.block_hash)




