import json_lines
import pickle
f = open('signalmedia-1m.jsonl','rb')
title = []
content = []
i = 0
for item in json_lines.reader(f):
	# print(item['title'],item['content'])
	title.append(item['title'])
	content.append(item['content'])
	i += 1
	print(i)
pickle.dump((title,content,None),open('signalmedia.pkl','wb'))
	# break
# result = [json.loads(jline) for jline in f.split('\n')]	
