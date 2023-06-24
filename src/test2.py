text = open('text.txt', 'r').read()

# split text by "
text = text.split(r'secret&lt;/th&gt;&lt;td class=\"prefright\"&gt;')[1].split("&")[0]

print (text)
print(len(text))