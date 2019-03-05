from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')

def count(request):
	data = request.GET['fulltextarea']
	word_list= data.split()
	len_word= len(word_list)
	worddic={}
	
	for word in word_list:
		if word in worddic:
			worddic[word] +=1
		else:
			worddic[word]=1
	sort_list=sorted(worddic.items(), key = operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'data':data,'length':len_word,'worddic':sort_list})

def about(request):
	return render(request,'about.html',{'author':'Harish Kumwat','Branch':'Computer Science'})


