# Install mmh3 and bitarray 3rd party module first
# pip install mmh3
# pip install bitarray
import random
import mmh3
from bitarray import bitarray

#The optimal number of hash functions is k = (m/n)*ln(2), 
#where m is the size of the bit array and n is the number of items to be inserted in the filter.

#the optimal size of the bit array is m = -(n*ln(p))/(ln(2)^2),
#where p is the desired false positive probability.

#The probability of false positives is given by the equation (1 - (1 - 1/m)^(kn))^k

class BloomFilter(object):

	def __init__(self, m, k):
        
		# Size of bit array to use
		self.size = m

		# Bit array of given size
		self.bit_array = bitarray(m)

		# initialize all bits as 0
		self.bit_array.setall(0)
		
        # number of hash functions to use
		self.hash_count = k

    #Add an item to the filter
	def add(self, item):

		digests = []
		for i in range(self.hash_count):

			# create digest for given item.
			# i work as seed to mmh3.hash() function
			# With different seed, digest created is different
			digest = mmh3.hash(item, i) % self.size
			digests.append(digest)

			# set the bit True in bit_array
			self.bit_array[digest] = 1

    #Check if an item is present in the filter
	def check(self, item):
		
		for i in range(self.hash_count):
			digest = mmh3.hash(item, i) % self.size
			if self.bit_array[digest] == 0:
				# if any of bit is False then,its not present
				# if not, there is probability that it exist
				return 0
		return 1



#------------------------------------------------------------
# Test
#------------------------------------------------------------
m = 1000
k = 10

bfilter = BloomFilter(m,k)


# words to be added
word_present = ['abound','abounds','abundance','abundant','accessible',
                'bloom','blossom','bolster','bonny','bonus','bonuses',
                'coherent','cohesive','colorful','comely','comfort',
                'gems','generosity','generous','generously','genial']
  
# word not added
word_absent = ['bluff','cheater','hate','war','humanity',
               'racism','hurt','nuke','gloomy','facebook',
               'geeksforgeeks','twitter']
  
#add the words to the bloom filter
for item in word_present:
    bfilter.add(item)
    
#Create a test set of 10 words
random.shuffle(word_present)
random.shuffle(word_absent)
test_words = word_present[:10] + word_absent
random.shuffle(test_words)

#Check if the words are present in the bloom filter
for word in test_words:
	if bfilter.check(word):
		if word in word_absent:
			print("'{}' is a false positive!".format(word))
		else:
			print("'{}' is probably present!".format(word))
	else:
		print("'{}' is definitely not present!".format(word))

