# TEXT QUALITY EVALUATOR
### De Leo Gabriele
#### A tool that extract lexical information from .docx file

The purpouse of this tool is to help user understand where a text is 'weaker' in terms of grammatical structure or lexic by calculating some numerical indexes that better can represent its feature and analyzing its spelling accuracy. These indexes are:
  - The **Gulpease Index** (GIX) - legibility index specific for italian language. It is calculated by the formula:
    
$$
GIX = 89 + \frac{300 \cdot \text{frasi} - 10 \cdot \text{lettere}}{\text{parole}}
$$


where 0 represent the lowest legibility and 100 the highest.

---
  - The **Syntactic Complexity Index** (SCIX) - measures the complexity of sentence structure in a text. It can be calculated by the formula:
    
$$
SCIX = \mathrm{MLS} \cdot \mathrm{S/C\ Ratio} \cdot \mathrm{SR}
$$

  where MLS is the Mean Length of Sentence, S/C Ratio is the Sentence-to-Clause Ratio and SR is the Subordination Ratio. Higher value means Higher syntactic complexity.

  ---
  - The **Lexical Diversity Index** (LDIX) - measures the variety of words used in a text, helping to assess the richness or variation in vocabulary:
    
$$
LDIX = \frac{\text{unique words}}{\text{total words}}
$$

  Range from 0 to 1 where higher value means more lexical diversity

---
Also, for each word, will be displayed if that word **belong or not to the Base Vocabulary**

The usage is simple, launch the tool, open a .docx file from the button on the up left and enjoy your stats
