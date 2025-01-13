# Ranking Metrics

## Precision
- *Intuition*: Out of all (k) retrieved docs, how many were correct/relevant?
- For a single query. 

## Recall
- *Intuition*: Out of all (k) ground truth docs, how many were retrieved?
- For a single query. 
- Not meaningful in ranking if the ground truth is the ranked list of all possible docs. 

## F1
- *Intuition*: Harmonic mean of (equally weighted) Precision and Recall. 
- 2 * Precision * Recall / (Precision + Recall)

## Mean Average Precision (MAP):
- *Intuition*: Considers whether all of the correct/relevant docs are ranked highly. 
- Average Precision (AP) is Precision calculated at every k in the retrieved docs, and then averaged. 
- MAP is the mean of AP values over all queries. 

## Mean Reciprocal Rank (MRR):
- *Intuition*: Out of all (k) retrieved docs, at which position is the first correct/relevant doc?
- RR is the inverse of that position index. 
- MRR is the mean of RR values over all queries. 

## Normalized Discounted Cumulative Gain (nDCG):
- *Intuition*: Measures the usefulness (gain) of a doc based on its position in the retrieved docs list. Highly relevant docs should be higher up in the list. 
- DCG is the relevance of a doc discounted by the log of its position in the retrieved list; we sum up this value for all (k) retrieved docs. 
- nDCG is the DCG for the retrieved list divided by the ideal DCG (iDCG) for the ground truth list. 
- Mean nDCG is the mean of nDCG values over all queries. 