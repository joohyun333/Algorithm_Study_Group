def DFS(idx,depth,output):
    global alphabet,word
    if depth == len(word):
        print(output)
        return

    for i in range(len(alphabet)):
        
        if alphabet[i]>0:
            alphabet[i]-=1
            
            output+=chr(ord('a')+i)
            
            DFS(i,depth+1,output)
            alphabet[i]+=1
            output=output[:-1]

if __name__=="__main__":
    N=int(input())
    for i in range(N):
        alphabet = [0 for i in range(26)]
        word = input()
        
        for j in range(len(word)):
            alphabet[ord(word[j])-ord('a')]+=1
        DFS(0,0,'')
