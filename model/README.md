# MODELS

## NOTE : I have used Kaggle to run all these above notebooks and link can be found below for the kaggle notebook and saved model weights.


  There are a bunch of models with which I have experimented. It includes machine learning and deep learning both. At the same time I have tried augmentations also like oversampling and paraphrashing.
  
  a) ```machine-learning.ipynb``` - In this notebook, I have experimented with a lot of ML models like SVMs, Logistic Regression, Naive Bayes and XGBoost. In this notebook I have also shown results after training model with oversamples data. All of the results are shown in notebooks.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/machine-learning)).           b) ```svm-classifier.ipynb``` - In this notebook, I have described different variants of SVM with different types of vectors. The things which worked and didn't worked also being shown in the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/svm-classifier)) 
  c) ```xgboost.ipynb``` - In this notebook, I have trained xgboost model with different hyperparameters and differnt types of vectors. All the results can be seen in the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/xgboost)) 
  d) ```lstm-dl``` - In this notebook, I have shown the training of LSTM model on the data. The results can be found on the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/lstm-dl))   
  e) ```augmentation.ipynb``` - Recently, I came across an NLP augmentation technique called paraphrasing and rasa recently added this functonality in thier library. So in this notebook, I have used rasa library for aumentations. But at last I was not being able to train classifier with augmented data beacuse as all the notebooks are being run on Kaggle, so this notebook took a lot of for creating paraphrases, so the notebook got terminated by the kaggle and because of this the augmentation could not be completed. Actually to reduce time, I divided the data into parts, but still it could not be done, with half the data it took more than 9 hrs and notebook got terminated because of this.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/augmentation1))
                                                                        
  f) ```bert-distilbert.ipynb``` - In this notebook, I have trained two bert models, one is the original bert and other is distilbert. The results can be seen in the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/bert-distilbert)  ). With bert I was getting the highest accuracy which is 0.64(this result is not available in the latest version of notebook provided above, so check this [version](https://www.kaggle.com/adityakumar01/bert-distilbert?scriptVersionId=32581570)), but the problem with bert is it's size which is 428 mb for "bert-base-uncased", I have also tried to deploy it on heroku, but with the accompanying libraries slug size beacomes 1.2GB. So. It's not possible to deploy bert. But still I have also trained another version of bert which is distilbert whose size is approx. 200 mb less than the bert, but "distilbert" is also not appropriate for deployment on heroku, because again the slug size will be more than 500 mb.                                                                                                  
  
  
  
|         | LGR   | XGB   | NB    | SVM   |
|---------|-------|-------|-------|-------|
| TFIDF   | 0.617 | 0.588 | 0.576 | 0.577 |
| COUNT   | 0.621 | 0.590 | 0.611 | 0.621 |
| SVD     |       | 0.577 |       | 0.481 |
| SVD_SC  |       |       |       | 0.513 |
| SMOTE_C | 0.454 |       |       |       |
  
  
