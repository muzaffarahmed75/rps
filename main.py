from random import choice
R, P, S = 'rock', 'paper', 'scissors'
D, W, L = 0, 1, 2
cap = lambda x: x.capitalize()
weap = (R, P, S)
wdic = {R:S, S:P, P:R}
print '<'+'resize such that this just fits'.center(78,'-')+'>'

def art(x,y):
    ra = ["    _______       ","---'   ____)      ","      (_____)     ",
    "      (_____)     ","      (____)      ","---.__(___)       "]
    pa = ["    _______       ","---'   ____)____  ","          ______) ",
    "          _______)","         _______) ","---.__________)   "]
    sa = ["    _______       ","---'   ____)____  ","          ______) ",
    "       __________)","      (____)      ","---.__(___)       "]
    for t in 'rps':
        l=[]
        for i in eval("%sa"%t):  # calls ra, pa, sa
            a, b = i.find('('), i.find(')')
            s=list(i)
            if (a+1)^(b+1):
                if a+1: s[a]=')'
                if b+1: s[b]='('
            l.append(''.join(s)[::-1])
        exec("%sb=l"%t)
    for i in range(6): print '  '+eval("%sa"%x)[i]+' '*40+eval("%sb"%y)[i]+'  '
    
def vic(w1, w2):
    if w1==w2: return D
    if wdic[w1]==w2: return W
    return L

def findall(a_str, sub):
    start = 0
    while 1:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

def printsym(a,b): print '\n'+a+' '*(80-len(a)-len(b))+b

# This AI takes all the previously played rounds as input. It looks for
# patterns of varying length and increases the probability of a weapon
# depending upon the length of pattern matched. If no match is found, a
# random weapon is picked.

def ai(pc):
    # pc is player+computer, op is only player
    r, p, s = 0, 0, 0
    op = pc[::2]
    for thresh in (8, 7, 6, 5):
        x = op[-thresh:]  # x is thresh number of last rounds
        l = list(findall(pc, x))
        if l:
            for i in l:
                # increment weapon according to the strength of threshold
                try: exec("%s+=thresh*(thresh-1)"%pc[i+thresh])
                except: pass
    for thresh in (4, 3):
        x = op[-thresh:]
        l = list(findall(op, x))
        if l:
            for i in l:
                try: exec("%s+=thresh*(thresh+1)"%op[i+thresh])
                except: pass
    m = r*r+p*p+s*s+0.1  # sum of squares
    r, p, s = r*r/m, p*p/m, s*s/m  # expected probabilities
    o = max(r,p,s)
    if o>0.5: return [P,S,R][[r,p,s].index(o)]
    return choice([R,P,S])
    
def ui():
    dat = list('r'*8)  # initial data, since humans usually play scissors first
    while 1:
        r=raw_input("How many rounds do you wish to play? ")
        if r.isdigit(): r=int(r)
        else: continue
        if r==0: r=999999
        break
    c, sc = 0, [0, 0]
    while c<r:
        w2 = ai(''.join(dat))
        inp = raw_input("\nRound %d%s\nChoose your weapon: "%(c+1,('.',' of %d.'%r)[r!=999999])).lower()
        if not inp: continue
        if inp in ('quit','exit','q'): break
        if any([not(i.find(inp)) for i in weap]): w1=eval(inp[0].upper())
        else:
            print "Invalid weapon. Please try again."
            continue
        c+=1
        dat.extend([w1[0],w2[0]])
        art(w1[0],w2[0])
        printsym("You played %s!"%w1.upper(),"The computer played %s!"%w2.upper())
        v = vic(w1,w2)
        rr = "%s %s %s."%(cap(w1),('draws with','beats','loses to')[v],cap(w2))
        print rr.center(80,' ')
        if v: sc[v-1]+=1
        print "The score is:"+' '*(16-len(na)/2)+"%s %d - %d - %d Computer"%(na,sc[0],c-sum(sc),sc[1])
    if sc[0]!=sc[1]: print "\nThe winner of this match is %s!\n"%(na,'the Computer')[sc[0]<sc[1]]
    else: print "\nThis match ends in a draw!\n"

while 1:
    while 1:
        na = raw_input("Hello! What is your name?\n")
        if not na: continue
        print "\nHello, %s!"%na
        break
    ui()
    while 1:
        ag = raw_input("Do you wish to play again?(y/n) ").lower()[0]
        if ag in ('y', 'n'): break
        else: continue
    if ag=='n': break
