from utils.topic import get_topics
from utils.search import search_news
import numpy as np

topics = get_topics("Kolkata")

result_arrays = []

for topic in topics:
    arr = search_news(topic)
    result_arrays.append(arr)

result_arrays = np.concatenate(result_arrays, axis=0)
result_arrays = list(set(result_arrays))

for topic in result_arrays:
    print(topic)


