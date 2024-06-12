from transformers import pipeline
import pandas as pd

pd.read_csv("C:\\Users\\17789\\LHL\\Stem-Review-Sentiment-Analysis\\Data\\dataset.csv")

classification = pipeline('sentiment-analysis')

classification("???????")