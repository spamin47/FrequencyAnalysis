alphabet = [0]*26
abcLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abcLettersTest = [chr(x+ord('a')) for x in range(26)]
englishLetterFreq = ['e','t','a','o','n','s','i','r','h','l','d','c','m','u','w','f','b','g','p','y','v','k','q','x','j','z']
with open("cipher.txt","r") as file:
    #read lines from files
    lines = file.readlines()
    #Count in character in file
    for l in lines: 
        for c in l:
            #Ignore counting spaces and whitespaces
            if(ord(c)<ord('a') or ord(c)> ord('z')):
                continue
            alphabet[ord(c)-ord('a')] +=1
    print(alphabet)
    print(sum(alphabet)) #total num of characters in file
    alphabet = [round(i/sum(alphabet),3) for i in alphabet] #divide all number by the number of characters in file (excluding spaces and whitespaces)
    alphabet = [round(100*i,2) for i in alphabet] #convert to percentage

    #pair letters and frequency together
    frequency = zip(abcLetters,alphabet)
    ls = list(frequency)
    ls.sort(key = lambda x: -x[1]) #sort in descending order
    print(ls)
    # print(abcLettersTest)
    
    #reset cursor to reread file
    file.seek(0)
    data = file.read()
    # print(data)
    indx = 0
    key = [0]*26
    #replace characters with presumed actual characters based on English Letter Frequency table 
    for i in ls:
        data = data.replace(i[0],englishLetterFreq[indx].upper())
        #Put together a key in the process of decrypting
        key[ord(i[0]) - ord('a')] = englishLetterFreq[indx]
        indx+=1    
    print(data.lower()) #Print out decrypted cipher
    print(''.join(key)) #Print out key