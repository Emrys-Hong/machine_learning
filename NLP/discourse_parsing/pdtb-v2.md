9% of all inter-sentential relations Argument 1 is located in non-adjacent previous sentence (Prasad et al., 2008)

See examples for each class at: 
[Data Annotation guide lines](https://www.seas.upenn.edu/~pdtb/PDTBAPI/pdtb-annotation-manual.pdf)



### explicit classification
from [Using Syntax to Disambiguate Explicit Discourse Connectives in Text]
1. Of the 100 connectives annotated in the PDTB, only 11 appear as a discourse connective more than 90% of the time.
2. baseline: \
        using only connective:          F-score 75.33, accuracy 85.86\
        using only syntatic feature:    F-score 88.19, accuracy 92.25 (higher than connective only, interesting)\
        using both:                     F-score 92.28, accuracy 95.04 (highest no doubt)

        
### Implict classification
![pic](images/brown_cluster_data.png)

implications of implict discourse relations: (Patterson and
Kehler, 2013)\
`Temporary` relations constitue 5% of implicit relations, as they are hard to create witout discourse connectives.\
`Expansion` are mostly implicit.\
This imbalance needs greater care in builing statistical classifiers(Wang et al., 2012).

Coreference patterns