word=input()
counts=dict()
midletter=''
final=''
for letter in word:
    counts[letter]=counts.get(letter,0)+1

for letter in sorted(counts,):
    if counts[letter]%2 !=0 :
        midletter+=letter
        counts[letter]-=1
    if len(midletter)>1 : #checking if more then one letter is even
        final="impossible"
        break
    else:
            for i in range(counts[letter]//2):
                final+= letter
                
reverse= final[::-1]
final+=midletter+reverse
    
print(final)
