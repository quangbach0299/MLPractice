import gensim.downloader as api
import numpy as np

# 25, 50, 100 or 200. Số càng lớn thì càng chính xác, nhưng chạy càng lâu các bạn nhé
model = api.load("glove-twitter-200")
word = "beautiful"
print(model[word])

print("1----------")
result = model.most_similar(word, topn=10)
print(result)

print("2----------")
result = model.most_similar(positive=["january", "february"], topn=10)
print(result)

print("3----------")
result = model.similarity("man", "woman")
print(result)

print("4----------")
result = model.most_similar(positive=["woman", "king"], negative=["man"], topn=1)
print(result)

print("5----------")
result = model.most_similar(positive=["berlin", "vietnam"], negative=["hanoi"], topn=1)
print(result)

print("6----------")
result = model.similarity("marriage", "happiness")
print(result)


#TODO: Các bạn thử viết 2 cách khác nhau để tính cosine similarity
# giữa 2 vector nhé. Kết quả giống với khi dùng model.similarity() là được
# 1 cách là dùng numpy, 1 cách là không dùng numpy nhé

# import numpy as np
# import math
# cosine_similarity = (vec1 · vec2) / (|vec1| * |vec2|)

# def cosine_similarity_numpy(vec1, vec2):
#     dot = np.dot(vec1, vec2)
#     norm1 = np.linalg.norm(vec1)
#     norm2 = np.linalg.norm(vec2)
#     return dot / (norm1 * norm2)

# def cosine_similarity_manual(vec1, vec2):
#     dot = sum(a * b for a, b in zip(vec1, vec2))
#     norm1 = math.sqrt(sum(a * a for a in vec1))
#     norm2 = math.sqrt(sum(b * b for b in vec2))
#     return dot / (norm1 * norm2)