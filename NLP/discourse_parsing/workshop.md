# CoNLL 2015 Shared Task Shallow Discourse Parsing
- [Main website](http://www.cs.brandeis.edu/~clp/conll15st/)
- [Dataset and Linguistic resources](http://www.cs.brandeis.edu/~clp/conll15st/dataset.html)
- [getting started](https://nbviewer.jupyter.org/github/attapol/conll15st/blob/master/tutorial/tutorial.ipynb), [repo](https://github.com/attapol/conll15st)
- [dataset insights](http://conll15st.blogspot.com/?view=classic)
  
## Rule:
(a) the discourse connective span is correctly
detected (for Explicit discourse relations) \
(b) the sense of the discourse connective is correctly
predicted \
(c) the text spans of its two arguments
are correctly predicted (Arg1 and Arg2). (it is a 1-0 mark)\
it is only a true positive if all the subtasks mentioned above is correct.


## Linguistic Resources:
- Brown clusters
- VerbNet
- Sentiment lexicon
- Word embeddings(word2vec)

## NLP tools:
- Phrase structure parses (predicted using the
Berkeley parser (Petrov and Klein, 2007))
- Dependency Parses (converted from phrase
structure parses using the Stanford converter
(Manning et al., 2014))

Brown clusters to determine the sense


## Problem framing
discourse connective identification -> token-level sequence labeling tasks. OR rule based \
argument extraction -> token-level sequence labeling tasks. \
Sense determination -> multi-category classification. 

## Approaches
machine learning: \
discourse connective identification and argument extraction: CRF \
sense determination: MaxEnt, SVMs, decision trees

deep learning:\
RNN for token level sequence labeling.\
discourse relation identification -> paragraph embeddings or word embeddings.


System | Learning Methods | Resource used | Paper | Code
---    | ---              | ---           | ---   | ---
ECNU   | MaxEnt and Navie Bayes | Brown clusters, MPQA subjectivity lexicon | https://aclweb.org/anthology/K15-2002 | https://github.com/lanmanok/conll2015_discourse
University of Trento | CRF++, Ada Boost | Brown clusters, dependency/phrase structure parses |  https://disi.unitn.it/~riccardi/papers2/CoNLL15-UNITNDiscourseParser.pdf | https://github.com/esrel/DP 
Soochow | MaxEnt in OpenNLP | VerbNet, MPQA subjectivity lexicon, Brown clusters | https://aclweb.org/anthology/K15-2004 | 
JAIST | CRF++, LibSVM | syntactic parses, Brown clusters | https://aclweb.org/anthology/K15-2010
UIUC | LibLinear | Brown cluster, MPQA lexicon | |
... | ... | ... | ... | ...

Other teams refer to paper.

[Two End-to-end Shallow Discourse Parsers for English and Chinese in CoNLL-2016 Shared Task](https://aclweb.org/anthology/K16-2004)

