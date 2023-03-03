import spacy
nlp = spacy.load('en_core_web_sm')

# Example 1
# Getting the similarity between the words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2)) 
print(word3.similarity(word2)) 
print(word3.similarity(word1))

# Note Compulsory Task 1
''' 
It is interesting that the similarities between cat and banana are almost equal to the similarities between cat and monkey
And when compare single words(Example 1).
Result is different.
When tokenise same words in sentence and compare(Example 2) 
example 1:
    cat.similarity(monkey) = 0.6770566055016188, monkey.similarity(banana) = 0.7276309976205778, cat.similarity(banana) = 0.6806929905901463
example 2:
    cat.similarity(monkey) = 0.6455236077308655, monkey.similarity(banana) = 0.4232019782066345, cat.similarity(banana) = 0.2214718759059906
'''

# Example 2
# First compare one word 'token1' to all the other ‘tokens’ in the string.
# And then do the same for the next word (token2) and repeat the cycle.
tokens = nlp('cat apple monkey banana ') 
for token1 in tokens:
     for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Example 3
# Similarity between longer sentences     
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", "Hello, there is my car",
"I\'ve lost my car in my car", "I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence) 
    print(sentence + " - ", similarity)
    
# Note Compulsory Task 1
'''
When run the example file with the simpler language model 'en_core_web_sm'
and when run the example file with the simpler language model 'en_core_web_md'
the result obtained is different.
'en_core_web_sm' model has no word vectors loaded, 
so the result of the similarity method will be based on the tagger, 
parser and NER, which may not give useful similarity judgments. 
This may happen if use one of the small models,
which don't ship with word vectors and only use context-sensitive tensors. 
Can always add own word vectors, or use one of the larger models, e.g. `en_core_web_md`, instead if available.
'''

# My examples:
'''
word1 = nlp("donkey")
word2 = nlp("monkey")
word3 = nlp("turkey")
print(word1.similarity(word2)) 
print(word3.similarity(word2)) 
print(word3.similarity(word1))

#result:
#0.6620404782140428
#0.7420689732983106
#0.5218798273360314

# =================================================================================

tokens = nlp('donkey monkey turkey grass') 
for token1 in tokens:
     for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#result:
#donkey donkey 1.0
#donkey monkey 0.6004133820533752
#donkey turkey 0.5905258059501648
#donkey grass 0.22233907878398895
#monkey donkey 0.6004133820533752
#monkey monkey 1.0
#monkey turkey 0.6059881448745728
#monkey grass 0.34400779008865356
#turkey donkey 0.5905258059501648
#turkey monkey 0.6059881448745728
#turkey turkey 1.0
#turkey grass 0.24696572124958038
#grass donkey 0.22233907878398895
#grass monkey 0.34400779008865356
#grass turkey 0.24696572124958038
#grass grass 1.0
'''