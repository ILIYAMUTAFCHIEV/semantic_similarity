

# Semantic Similarity (NLP)

#### A Python program uses spaCy to detect similarities between single words, similarities between series of words all with one another, similarities between sentences 
---------------------------------------------------------------

## A table of contents:

### semantic.py

---------------------------------------------------------------
### 'semantic.py' content:

#### Example 1

- Getting the similarity between the words
    
Note Compulsory Task 1:

''' 
It is interesting that the similarities between cat and banana are almost equal to the similarities between cat and monkey
And when comparing single words(Example 1).
The result is different.
When tokenise same words in the sentence and comparing (Example 2) 
example 1:
    cat.similarity(monkey) = 0.6770566055016188, monkey.similarity(banana) = 0.7276309976205778, cat.similarity(banana) = 0.6806929905901463
example 2:
    cat.similarity(monkey) = 0.6455236077308655, monkey.similarity(banana) = 0.4232019782066345, cat.similarity(banana) = 0.2214718759059906
'''

#### Example 2

- Getting similarity between series of words all with one another


    
#### Example 3

- Getting similarities between sentences

Note Compulsory Task 1

'''
When running the example file with the simpler language model 'en_core_web_sm'
and then run the example file with the simpler language model 'en_core_web_md'
the result obtained is different.
The 'en_core_web_sm' model has no word vectors loaded, 
so the result of the similarity method will be based on the tagger, 
parser and NER, which may not give useful similarity judgments. 
This may happen if use one of the small models,
which don't ship with word vectors and only use context-sensitive tensors. 
Can always add your own word vectors, or use one of the larger models, e.g. `en_core_web_md`, instead if available.
'''
    
#### My Examples
    



## Clone the repo
git clone https://github.com/ILIYAMUTAFCHIEV/semantic_similarity.git




## Contact
Iliya Mutafchiev - https://www.linkedin.com/in/iliya-mutafchiev-974471211/

Project Link: https://github.com/ILIYAMUTAFCHIEV/semantic_similarity
