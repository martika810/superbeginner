
code_article_file = open('code_article.txt','r')

words_dictionary = {}
for line in code_article_file.readlines():
    for word in line.lower().split(' '):
        if word in words_dictionary.keys():
            words_dictionary[word] +=1
        else:
            words_dictionary[word] = 1

for word,count in words_dictionary.items():
    print(word + " - "+ str(count))