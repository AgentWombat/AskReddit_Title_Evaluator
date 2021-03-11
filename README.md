# AskReddit_Title_Evaluator
The end goal is to use machine learning to train a model to predict if an AskReddit post will make it to the front page.

the GloVe word embeddings are NEEDED for all machine learning functionality. I downloaded 'glove.6B.zip'. Extract the 100d vector text file and place it in the same directory as the other script files.
https://nlp.stanford.edu/projects/glove/
(I cannot include it here as the file size it too big)

METHOD: The data is the title of reddit posts. Each label is either 1 for 'made it to the front page' and 0 for 'did not make it to the front page'.
        Successes were collected from the top of all time section of AskReddit and the top 25 post of hot for the last week or so (written 3/10). (~900 posts)
        Failures were collected by taking every new post for a spesific time peried and the bottom 25 post of hot for the last week or so (written 3/10). (~900 posts)
        It should be alright to collect faulures like this because over ~1000 posts are made to askreddit every three hours and a negligable portion of those make it to the front page
        
        
- 'model64' is a model which maintained 64% accuracy on test data. More interestingly, if the threshold is set to .75, the model has 80% percision and 41% recall on the test data.
  It was trained on the 'parsed_data'. The last 125 data points were reserved for test data. The GloVE 100d word vectors were used 
  
- 'reddit_scraper.py' provides a function for scraping subreddit pages.

- 'Reddit_Scraping_Script.py' implements 'reddit_scraper' with a simple cli to provide for easy data collection.

- 'embedding.py' provides function for takeing stings -> 2d numerical arrays. For its functions to work with default keyword arguments, the GloVe 100d word vector text file must be in the same directory.

- 'model.py' contains the StringModel class which is a wraps around a keras LSTM model. It automatically converts string inputs using embeddings for ease of use.

- 'train_model_script.py' Is what I used to train the model

- 'parsed_data' has the data I used to train and evaluate model64.



EXTERNAL LIBRARIES:

Tensorflow

NumPy

scikit-learn

also, GloVe word embeddings were used to convert strings to numerical arrays. The embeddings can be found here: https://nlp.stanford.edu/projects/glove/

