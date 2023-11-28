from typing import *
from functools import reduce
import math

vals = [7, 14, 81, 56, 9, 17, 43]

def getMetric(
  metric: Union[Literal['mean'], Literal['median']], 
  ListVal: List[int]
):
  lenght: int = len(ListVal)
  if metric == 'mean':
    return reduce((lambda x, y: x + y), ListVal) / lenght
  if metric == 'median':
    midMed: float = lenght / 2
    if lenght % 2 == 0:
      firstMed = ListVal[midMed - 1]
      secondMed = ListVal[midMed]
      return (firstMed + secondMed) / 2
    else:
      return sorted(ListVal)[math.floor(midMed)]

mean = getMetric("mean",vals)
med = getMetric("median",vals)
print(mean)
print(med)
  

