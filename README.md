# PLN - Assignment 1

The aim of this assignment is to build NLP classifiers for a specific text classification task. For that, you may explore any of the techniques that we are exploring during the course, including pre-processing, feature extraction, and sparse vs dense feature representations (including word embeddings). In the scope of this first assignment, you can also use any "traditional" machine learning classifier, including Naive Bayes, Logistic Regression, Decision Trees, Random Forest, Support Vector Machine, Multi-Layer Perceptron, XGBoost, and so on. You may NOT use any deep learning architecture based on CNNs, RNNs, or Transformers.

| Model | Bag of Words (BoW) | TF-IDF (Sparse Weights) | N-grams (Sparse Context) | Hashing Vectorizer (Sparse Speed) | LSA / SVD (Dense Reduction) | Embeddings (Dense Word2Vec) | Dense N-grams (FastText) | Linguistic / Style Features |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **LogReg (Logistic Regression)** | Best Match | Best Match | Excellent | Excellent | Good | Good (Averaged) | Best Match | Excellent |
| **SVM (One vs Rest)** | Excellent | Best Match | Best Match | Excellent | Good | Good | Best Match | Excellent |
| **Naive Bayes (Multinomial)** | Best Match | Excellent | Good | Fair (Requires non-negative config) | Poor (Produces negatives) | Poor (Produces negatives) | Poor (Produces negatives) | Poor |
| **SentimentLDA** | Best Match (Required) | No | Fair (Bigrams work ok) | No | No | No | No | No |
| **HMM** | Best Match (Requires counts) | Poor (Breaks probability math) | Fair | No | No | No | No | Good |
| **k-NN** | Poor | Fair | Poor | Poor (Distance fails on hash collisions) | Best Match | Best Match | Excellent | Good (Requires strict scaling) |
| **XGBoost / Random Forest** | Fair | Good | Fair (Trees get too deep) | Good (Limits max features) | Excellent | Excellent | Excellent | Best Match |
| **AdaBoost** | Poor | Fair | Poor | Fair | Good | Good | Good | Best Match |

Other options:
- Passive agressive classifier. only makes sense for online learning
- Contidional Random Field. only makes sense for long documents, not short sentences.


Group 20:
- João Guedes (202108711)
- Luís Fiunte (202208819)