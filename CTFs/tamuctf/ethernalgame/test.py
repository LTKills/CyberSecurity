import hashpumpy
import hashlib


key = 'aloalomarciano'
ola = 'ola'
olamundo = 'olamundo'
guessed = '7190d49b6e164dd600e9abb92ed269e3bd9268b454c733bc6f613de3f8449b10'

onehash = hashlib.sha256(key + ola).hexdigest()
tenhash = hashlib.sha256(key + olamundo).hexdigest()

print 'OLA HASH'
print onehash

print 'OLAMUNDO HASH'
print tenhash



guessten, msg = hashpumpy.hashpump(onehash, 'ola', 'mundo', len(key))

print 'GUESS TEN'
print guessten
print int(bytes(msg))
