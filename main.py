from random import choice
R,P,S='rock','paper','scissors'
D,W,L=0,1,2
cap=lambda x: x.capitalize()
weap=(R,P,S)
wdic={R:S,S:P,P:R}



def vic(w1,w2):
  if w1==w2: return D
  if wdic[w1]==w2: return W
  else: return L

def ai():
  return choice([R,P,S])

def cnt(): pass
  

def ui():
  while 1:
    na=raw_input("Hello! What is your name?\n")
    if not na: continue
    break
  while 1:
    r=raw_input("How many rounds do you wish to play? ")
    if r.isdigit(): r=int(r)
    else: continue
    break
  c,sc=0,[0,0]
  while c<r:
    inp=raw_input("\nRound %d of %d.\nChoose your weapon: "%(c+1,r))
    if any([not(i.find(inp)) for i in weap]): w1=eval(inp[0].upper())
    else:
     print "Invalid weapon. Please try again."
     continue
    print "You played %s!"%w1
    c+=1
    w2=ai()
    print "The computer played %s!"%w2
    v=vic(w1,w2)
    print "%s %s %s."%(cap(w1),('draws with','beats','loses to')[v],w2)
    if v: sc[v-1]+=1
    print "The score is %s %d - %d Computer."%(na,sc[0],sc[1])
  if sc[0]!=sc[1]: print "\nThe winner of this match is %s!\n"%(na,'the Computer')[sc[0]<sc[1]]
  else: print "This match ends in a draw!\n"
while 1:
  ui()
  while 1:
    ag=raw_input("Do you wish to play again? (y/n)").lower()[0]
    if ag in ('y','n'): break
    else: continue
  if ag=='n': break
