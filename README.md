# NLP_LeMonde_tweets_2022

The main objective of this project is to use natural language processing techniques to analyze the tweets of the newspaper [Le Monde](https://www.lemonde.fr/en/), in order to observe current affairs themes and trends. To do this, we collected a large number of tweets published by Le Monde and used various text analysis techniques to extract meaningful information from the data. The data collection is presented in the file `twitter_generate_data.py`.

In this study, we explored different approaches to processing and analyzing the newspaper's tweets, using both data processing and analytical tools. We also examined the different ways in which these tweets reflect current events and topics that are popular with Le Monde readers.

Throughout this project, we'll be looking at tweets from 2022, enabling us to address our problem for this data.

Initially, we focused on studying the data and how we could clean it up. Next, we decided to focus our analysis on a global view of themes, using a Name Entity Recognition model. Finally, in the last part we focused on a more precise view of the themes, using NMF, a useful tool for NLP text analysis, which enables us to discover hidden themes in a corpus of documents in an efficient way.

The detailed steps of the project are available in the `project_tweeter_LeMonde.ipynb`

The main packages used in this project are :
- `nltk`
- `spacy`
- `wordcloud`
- `unidecode`
- `pandas`
- `numpy`
- `spellchecker`
- `re`

# Different steps of the project

### Data pre-processing

Selection of 2022 tweets and tweets with over 100 likes.

### Text processing

Creation and application of functions to clean tweets.

### First analysis

  - Computation of number, mean, standard deviations and quartiles of likes and retweets.
  - Creation of a word cloud.

### NLP techniques

#### Name Entity Recognition model

Application of the NER model.

#### Topic modelling

Application of topic modelling.
