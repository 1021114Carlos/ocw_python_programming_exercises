def search(keyword) :
   # implement the function here
   class Entry:
      def __init__(self, word, synonyms):
         self.word = word
         self.synonyms = synonyms

   All_words = []
   All_words.append(keyword)
   for Entry in Thesaurus:
      if keyword == Entry.word:
         for synonym in Entry.synonyms:
            All_words.append(synonym)
   word_syn
   for word in All_words:
      count = 0
      for document in Corpus:
         count += 1
           
      word_syn.append(word, count)
   return word_syn

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
