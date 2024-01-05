from collections import Counter,deque

def interweaving(s,t,u):
    if t == '':
        return s == u
    if u == '':
        return s == t
    sfx = s[1:]
    tfx = t[1:]
    ufx = u[1:]
    if t[0]==s[0] and u[0]==s[0]:
        return interweaving(sfx,tfx,u) or interweaving(sfx,t,ufx)
    if t[0]==s[0]:
        return interweaving(sfx,tfx,u)
    if u[0]==s[0]:
        return interweaving(sfx,t,ufx)
    return False
s,t,u=(input() for _ in '...') 
seglen=len(t)+len(u)
count=Counter()
BC=Counter(t+u)
for i,c in enumerate(s):
    count[c]+=1
    if i<seglen-1:
        continue
    if count==BC:
        if interweaving(s[i-seglen+1:i+1],t,u):
            print('Yes')
            break
    count[s[i-seglen+1]]-=1
    if count[s[i-seglen+1]]==0:
        del count[s[i-seglen+1]]
else:
    print('No')