from collections import Counter

listLine: list[str] = []
with open('sampleText.txt', 'r') as file:
  for line in file:
    line = line.strip()
    line = line.replace('.', '')
    
    
    if line:
      listLine.append(line)
  #print(listLine)

allWords = ' '.join(listLine).split(' ')
# print(allWords)
uniqueWords = set(' '.join(listLine).split(' '))

word_counts = Counter(allWords)

# for word in allWords:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1

# sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

print(word_counts)

      
