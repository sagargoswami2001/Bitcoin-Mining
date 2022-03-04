# Python Program to Bitcoin Mining Process.

from hashlib import sha256  # SHA256 is a Cryptographic Hash Function
MAX_NONCE = 1000000000000           
#The "nonce" in a bitcoin block is a 32-bit (4-byte)
# field whose value is adjusted by miners 
# so that the hash of the block will be less than or equal to the current target
# of the network. The rest of the fields may not be changed, 
# as they have a defined meaning.

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"\nHooray! Successfully Mined Bitcoins with Nonce Value: {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find Correct has After Trying {MAX_NONCE} Times")

if __name__=='__main__':
    transactions = '''
    Dhaval->Bhavin->20
    Mando->Cara->45
    '''

    difficulty = 5 # Try Changing This to Higher Number 
                        #and You Will See It Will Take More Time for Mining as Difficulty Increases.
                        #Beware to not Use a Large no. 
                        #Reference: on NVIDIA GeForce GTX 1050Ti Oc GPU it takes >2 min 
                        # Warning: do not use value Above 7

    import time
    start = time.time()
    print("\nStart Mining...")
    new_hash = mine(5, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"End Mining. Mining Took: {total_time} Seconds")
    print(new_hash)
