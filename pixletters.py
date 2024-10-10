import os
# cwd =  os.getcwd()
cwd = os.path.dirname(os.path.abspath(__file__))
cwd = cwd + '\\'
print("Opening file at \'"+cwd+"\'")

with open(cwd+'allwords.txt','r') as f:
    words = f.readlines()
    
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaPix = {
    'a':[[0,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,2,2,2,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2]],
    'b':[[2,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,2,2,2,0]],
    'c':[[0,2,2,2,0],[2,0,0,0,2],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,2],[0,2,2,2,0]],
    'd':[[2,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,2,2,2,0]],
    'e':[[2,2,2,2,2],[2,0,0,0,0],[2,0,0,0,0],[2,2,2,2,0],[2,0,0,0,0],[2,0,0,0,0],[2,2,2,2,2]],
    'f':[[2,2,2,2,2],[2,0,0,0,0],[2,0,0,0,0],[2,2,2,2,0],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0]],
    'g':[[0,2,2,2,0],[2,0,0,0,2],[2,0,0,0,0],[2,0,0,2,2],[2,0,0,0,2],[2,0,0,0,2],[0,2,2,2,0]],
    'h':[[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,2,2,2,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2]],
    'i':[[2,2,2,2,2],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0],[2,2,2,2,2]],
    'j':[[2,2,2,2,2],[0,0,0,2,0],[0,0,0,2,0],[0,0,0,2,0],[0,0,0,2,0],[2,0,0,2,0],[0,2,2,0,0]],
    'k':[[2,0,0,0,2],[2,0,0,2,0],[2,0,2,0,0],[2,2,0,0,0],[2,0,2,0,0],[2,0,0,2,0],[2,0,0,0,2]],
    'l':[[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0],[2,2,2,2,2]],
    'm':[[2,0,0,0,2],[2,0,0,0,2],[2,2,0,2,2],[2,0,2,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2]],
    'n':[[2,0,0,0,2],[2,0,0,0,2],[2,2,0,0,2],[2,0,2,0,2],[2,0,0,2,2],[2,0,0,0,2],[2,0,0,0,2]],
    'o':[[0,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[0,2,2,2,0]],
    'p':[[2,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,2,2,2,0],[2,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0]],
    'q':[[0,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,2,0,2],[2,0,0,2,0],[0,2,2,0,2]],
    'r':[[2,2,2,2,0],[2,0,0,0,2],[2,0,0,0,2],[2,2,2,2,0],[2,0,2,0,0],[2,0,0,2,0],[2,0,0,0,2]],
    's':[[0,2,2,2,0],[2,0,0,0,2],[2,0,0,0,0],[0,2,2,2,0],[0,0,0,0,2],[2,0,0,0,2],[0,2,2,2,0]],
    't':[[2,2,2,2,2],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0]],
    'u':[[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[0,2,2,2,0]],
    'v':[[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[0,2,0,2,0],[0,0,2,0,0]],
    'w':[[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,0,0,2],[2,0,2,0,2],[2,0,2,0,2],[0,2,0,2,0]],
    'x':[[2,0,0,0,2],[2,0,0,0,2],[0,2,0,2,0],[0,0,2,0,0],[0,2,0,2,0],[2,0,0,0,2],[2,0,0,0,2]],
    'y':[[2,0,0,0,2],[2,0,0,0,2],[0,2,0,2,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,2,0,0]],
    'z':[[2,2,2,2,2],[0,0,0,0,2],[0,0,0,2,0],[0,0,2,0,0],[0,2,0,0,0],[2,0,0,0,0],[2,2,2,2,2]]
}

class Letter:
    def __init__(self):
        self.row = 0
        self.alpha = alphabet.copy()
        self.mat = [[1,1,1,1,1],[1,1,1,1,1],
                    [1,1,1,1,1],[1,1,1,1,1],
                    [1,1,1,1,1],[1,1,1,1,1],
                    [1,1,1,1,1]]
        self.fixed = False
        self.fixedLetter = ''
    def declare(self,pix0,pix1,pix2,pix3,pix4):
        if self.fixed:
            return
        if self.row < 7:
            self.mat[self.row] = list((pix0,pix1,pix2,pix3,pix4))
            self.row +=1
        else:
            print("Error! Rows have passed 7")
            
    def checkAlpha(self):
        if self.fixed:
            return
        for index, al in enumerate(self.alpha):
            if al == ' ':
                continue
            for i in range(5):
                if self.mat[self.row - 1][i] == 1:
                    continue
                if alphaPix[al][self.row - 1][i] != self.mat[self.row - 1][i]:
                    self.alpha[index] = ' '
                    break
        res = [j for j in self.alpha if j != ' ']
        self.alpha = res.copy()
        if len(self.alpha) == 1:
            self.fixed = True
            self.fixedLetter = self.alpha[0]
        if len(self.alpha) < 1:
            print("Error! Letter not possible!!!")
            return
        
l0 = Letter()
l1 = Letter()
l2 = Letter()
l3 = Letter()
l4 = Letter()
letters = [l0,l1,l2,l3,l4]
                        
def possibleWords(allwords):
    alwords = allwords.copy()
    newWords = []
    for word in alwords:
        valid = True
        for i in range(5):
            if letters[i].fixed:
                if word[i] != letters[i].fixedLetter:
                    valid = False
                    break
            elif word[i] in letters[i].alpha:
                pass
            else:
                valid = False
                break
        if valid:
            newWords.append(word)
    alwords = newWords.copy()
    return alwords
                
    




print("Hint: Use word \'Titer\' as your first word")
print("Use \'2\' as correct pixle and \'0\' as wrong one.")
print("If found one letter just enter the letter")
print("Example: \'22220 02220 r 10001 22222\'")

while (True):
    # if 'state\n' in words:
    #     print("Yes")
    # else:
    #     print("No")
    print("Number of words available: ",end="")
    numberOfWords = len(words)
    print(numberOfWords)
    print("(Enter \'best\' to see possible words)")
    inp = input("Enter your result: ")
    if inp == "best":
        # print words
        for index, i in enumerate(words):
            print(str(index)+".",i[:-1])
        continue
    inp = inp.split()
    for index, val in enumerate(inp):
        if val.isdigit() and len(val) == 5:
            letters[index].declare(int(val[0]),int(val[1]),int(val[2]),int(val[3]),int(val[4]))
        elif len(val) ==1:
            if val.isalpha():
                val = val.lower()
                letters[index].fixed =True
                letters[index].fixedLetter =val
        else:
            print("Error! Wrong input! Try again: ")
            if index > 0: #some letters have changed before seeing the error
                ind = index-1
                while (ind>=0):
                    if letters[ind].fixed:
                        ind -=1
                        continue
                    letters[ind].row -=1
                    ind -=1
            break
    for i in range(5):
        letters[i].checkAlpha()
    words = possibleWords(words)
        
    
