#encoding:utf-8
from random import *
class Data:
	def __init__(self,tag,s):
		self.tag=tag
		self.s=s
	def play(self):
		tot=len(self.s)
		idx=randint(0,tot-1)
		for i in range(tot):
			if i==idx:
				print('__QAQ__')
			else:
				print(self.s[i])
		input('ok?')
		for i in self.s:
			print(i)
			pass
print('Deep Dark Fantasy!')
f=open('poem.txt','r')
da=[]
nwtag={}
while True:
	a=f.readline()
	if a:
		if a[0]=='S':
			nwtag=set(a[2::].split())
		else:
			da.append(Data(nwtag,a.split()))
	else:
		break
nwtag=set()
def work():
	tmp=[]
	for i in da:
		if (nwtag.issubset(i.tag)):
			tmp.append(i)
	idx=randint(0,len(tmp)-1)
	tmp[idx].play()
