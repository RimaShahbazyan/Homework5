from collections import Counter

word=input()
counts =  Counter(word)
midletter=''
final=''

for letter in sorted(counts,):
    if counts[letter]%2 :
        midletter+=letter
    if len(midletter)>1 : #checking if more then one letter is even
        final="impossible"
        break
    else:
        final+= letter*(counts[letter]//2)

reverse= final[::-1]
final+=midletter+reverse
    
print(final)
