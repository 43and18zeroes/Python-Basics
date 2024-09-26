import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def analyze_text(text):
  # Tokenisierung
  words = word_tokenize(text)
  
  # Entfernung von Stopwords
  stop_words = set(stopwords.words('english'))
  filtered_words = [word for word in words if word not in stop_words]
  
  # Häufigkeitsverteilung
  word_freq = nltk.FreqDist(filtered_words)
  
  # Ausgabe der häufigsten 10 Wörter
  print(word_freq.most_common(10))

# Beispieltext
text = "This is a sample text for natural language processing. We can use NLTK to analyze it."
analyze_text(text)