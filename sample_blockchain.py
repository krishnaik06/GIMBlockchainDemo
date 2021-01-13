

from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("We have successfully mined our block and the nonce is {}".format(nonce))
            return new_hash

    raise BaseException("We did not find the hash for {} iterations".format(MAX_NONCE))

if __name__=='__main__':
    transactions='''
    Krish-tranaction-50$
    '''
    prefix_zeros=6 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(2,transactions,'000000067f29319ce46e3d4611481b8d826d9519242f675d67ff6c9c987afcc3', prefix_zeros)
    total_time = str((time.time() - start))
    print("end mining. Total time Taken by the mining is: {} seconds".format(total_time))
    print(new_hash)
    

    
    
    