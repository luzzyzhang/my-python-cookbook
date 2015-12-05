# Determin the most frequecntly occurring of items in sequence
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'arround', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
# use collection.Counter class and it's most_common() method
word_counts = Counter(words)
top_tree = word_counts.most_common(3)
print word_counts
print top_tree

# As input Counter objects can be fed any sequence of hashbale input items
# Uder the cover a Counter is a dictionary that maps the items to number of # occurences 
print word_counts['not']
print word_counts['eyes']
# Increment the count manually
morewords = ['why', 'are', 'you', 'not', 'looing', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print word_counts['eys']
# Also can use the update() method
# word_counts.update(morewords)


a = Counter(words)
b = Counter(morewords)
print a
print 50*'~'
print b
# Combine counts,Counter instances can be easily combined using math operations
c = a + b
print c
d = a - b
print 50*'*'
print d

