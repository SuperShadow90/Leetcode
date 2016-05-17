class Solution(object):
    def getHint(self, secret, guess):
        length = len(secret)
        a, b = 0, 0
        d = {}
        for i in secret:
        	if i not in d:
        		d[i] = 1
        	else:
        		d[i] += 1
        for i in guess:
        	if d[i] > 0:
        		b += 1
        		d[i] -= 1
        for i in range(length):
        	if secret[i] == guess[i]:
        		a += 1
        		b -= 1
        
        return "{0}A{1}B".format(a, b)




def getHint(self, secret, guess):
        lens = len(secret)
        a,b = 0, 0
        d = {}
        ls = []
        for i in range(lens):
        	if secret[i] == guess[i]:
        		a += 1
        	else:
        		if secret[i] not in d:
        			d[secret[i]] = 1
        		else:
        			d[secret[i]] += 1
        		ls.append(guess[i])


        for value in ls:
        	if value in d:
        		b += 1
        		if d[value] > 1:
        			d[value] -= 1
        		else: 
        			del d[value]

        return (str(a) + "A" + str(b) + "B")



