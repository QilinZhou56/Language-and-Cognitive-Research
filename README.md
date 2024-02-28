# Language-and-Cognitive-Research

## Overview
This project, supervised by Dr. Catherine Sandhofer and led by graduate student Erjing Zhang, focuses on the cognitive aspects of language acquisition in children. Utilizing text mining and visualization tools, we explore how young children use adjectives to describe various referents in picture-reading activities.

## Team Members
- Dr. Catherine Sandhofer (Supervisor)
- Erjing Zhang
- Qilin Zhou
- Shalmalee Joshi

## Data Source
We analyzed 33 transcripts from the CHILDES database, specifically from Gelman's 2014 individual differences corpus. The transcripts are based on picture-reading activities involving one-referent pictures, conducted between children and their parents.

## Methodology
Our approach involved two primary tools:
- **spaCy**: For text mining, specifically focusing on the use of adjectives for each referent in the pictures, including n-grams analysis for adjectives and nouns.
- **Pyvis**: To visualize the associations between adjectives and different types of referents (e.g., social, food, animals).

## Sample Visualization
- [Adjs Across Categories by spaCy](https://github.com/QilinZhou56/Language-and-Cognitive-Research/blob/main/referential_communication/Result/general_adj_freq_Spacy.png)
- [N_grams](https://github.com/QilinZhou56/Language-and-Cognitive-Research/blob/main/referential_communication/Result/n_grams_viz.png)
- [Food Adjs Frequency](https://github.com/QilinZhou56/Language-and-Cognitive-Research/blob/main/referential_communication/Result/food_adj_freq.png)
  
[View Pair-wise Association](https://htmlpreview.github.io/?https://github.com/QilinZhou56/Language-and-Cognitive-Research/blob/main/referential_communication/Result/food_adj_referent.html)

If not worked properly, you could reference [HTML](https://github.com/QilinZhou56/Language-and-Cognitive-Research/blob/main/referential_communication/Result/food_adj_referent.html)

## Findings
Our findings reveal interesting patterns in the use of adjectives by four-year-old children:
- For food referents, children commonly used color, size, and taste adjectives, while quality or functional adjectives were less frequent.
- In describing human referents, children focused more on perceptual features and less on inherent qualities like "alive", "good", or "kind".
- There was a larger variety of adjectives used for food referents compared to human referents, indicating a protracted process in adjective usage relative to noun acquisition.

## Cross-Validation
We extended our research by conducting cross-validation with other linguistic transcripts. This further established spaCy as a robust tool for identifying parts of speech and analyzing language patterns in young children, with consistent 90% baseline accuracy. We will continue improving this model with modification regarding dependency and classification threshold.

## Conclusion
Our project contributes to understanding how children's language and cognitive abilities develop, particularly in the context of adjective usage in descriptive tasks. These insights can be crucial for further research in developmental psychology and linguistics.

## Acknowledgments and Confidentiality
We would like to thank all contributors and participants involved in this research project. The two sample data, if used, should inform us for research confidentiality purposes.
