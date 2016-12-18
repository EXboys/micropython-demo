import ure as re
import gc
import uos as os
import utime

def render(html,kwargs):
	try:
		tdelta = utime.time() - os.stat(html+'.temp')[8]
	except:
		tdelta = 999
	if tdelta> 60:
		page = pageCompile(html,kwargs)
		f = open(html+'.temp','w+')
		f.write(page)
		f.close()
	else:
		page = getFile(html+'.temp')
	gc.collect()
	return page

def pageCompile(html,kwargs):
	html = getFile(html)
	num = 1
	for key,item in kwargs.items():
		if type(item) is list or type(item) is dict:
			while re.search(r'{for.+?\/for}.+?',html) is not None:
				if num % 3 != 0:
					old,new = forlist(html,key,item)
					html = html.replace(old,new)
					num +=1
				else:
					num +=1
					break
		else:
			html = varCompile(html,key,item)
		while re.search(r'{if.+?\/if}.+?',html) is not None:
			if num % 3 != 0:
				old,new = ifBlock(html,key,item)
				html = html.replace(old,new)
				num +=1
			else:
				num +=1
				break
	return html

def getFile(html):
	f = open(html,'r')
	html = ''.join(f.readlines())
	f.close()
	return html

'''
compile list and dict
'''
def forlist(html,key,item):
	ctn = re.search(r'{for.+?\/for}.+?',html).group(0)
	conArr = ctn.split('\n')
	forctn = conArr[0].split(' ')
	var = forctn[-1].replace('}','')
	if var == key:
		arr = []
		for j in item:
			for i in conArr[1:-2]:
				arr.append(i.format(**{forctn[1]:j}))
		return ctn,''.join(arr)
	else:
		return '',''

def ifBlock(html,key,item):
	ctn = re.search(r'{if.+?\/if}.+?',html).group(0)
	conArr = ctn.split('\n')
	if conArr[0].split(' ')[1] == key:
		ifCtn = ('True '+conArr[0].replace('{','').replace('}',' else False')).replace('eq','==').replace(''+key+'','{'+key+'}')
		ifCtn = ifCtn.format(**{key:item})
		try:
			res = eval(ifCtn)
		except:
			res = False
		if res is True:
			return ctn,''.join(conArr[1:-2])
	else:
		return '',''
	
def varCompile(html,key,item):
	html = html.replace('{'+key+'}',str(item))
	html = html.replace('{'+key+'|upper}',str(item).upper())
	html = html.replace('{'+key+'|lower}',str(item).lower())
	html = html.replace('{'+key+'|b}','<b>'+str(item)+'</b>')
	return html
	
if __name__=='__main__':
	import micropython
	print(micropython.mem_info())
	test = 'test'
	a ={'item':test,'name':[1,2,3,4,6,7,8,9],'display':1}
	res = render('index.html',a)
	print(res)
	print(micropython.mem_info())

