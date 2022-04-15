d={}
import re
a="The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"
a1=a.lower()
out = re.sub(r'[^\w\s]','',a1)
b=out.split()
for q in b:
    if q in d:
        d[q]+=1
    else:
        d[q]=1
print(d)

maxc=max(d.values())
for key, con in d.items():
    if con==maxc:
        print('字串%s出現最多次共%d次'%(key,con))