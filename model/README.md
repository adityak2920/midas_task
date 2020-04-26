# MODELS

## NOTE : I have used Kaggle to run all these above notebooks and link can be found below for the kaggle notebook and saved model weights.
**NOTE** : Please check the notebook in the way shown below.


  There are a bunch of models with which I have experimented. It includes machine learning and deep learning both. At the same time I have tried augmentations also like oversampling and paraphrashing.
  
  a) ```machine-learning.ipynb``` - In this notebook, I have experimented with a lot of ML models like SVMs, Logistic Regression, Naive Bayes and XGBoost. In this notebook I have also shown results after training model with oversamples data. All of the results are shown in notebooks.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/machine-learning)). 
  
  b) ```svm-classifier.ipynb``` - In this notebook, I have described different variants of SVM with different types of vectors. The things which worked and didn't worked also being shown in the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/svm-classifier))
  
  c) ```xgboost.ipynb``` - In this notebook, I have trained xgboost model with different hyperparameters and differnt types of vectors. All the results can be seen in the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/xgboost))
 
  
  d) ```augmentation.ipynb``` - Recently, I came across an NLP augmentation technique called paraphrasing and rasa recently added this functonality in thier library. So in this notebook, I have used [rasa library](https://forum.rasa.com/t/paraphrasing-for-nlu-data-augmentation-experimental/27744) for aumentations. But at last I was not being able to train classifier with augmented data beacuse as all the notebooks are being run on Kaggle, so this notebook took a lot of for creating paraphrases, so the notebook got terminated by the kaggle and because of this the augmentation could not be completed. Actually to reduce time, I divided the data into parts, but still it could not be done, with half the data it took more than 9 hrs and notebook got terminated because of this.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/augmentation1))
  
  e) ```lstm-dl.ipynb``` - In this notebook, I have shown the training of LSTM model on the data. The results can be found on the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/lstm-dl))
                                                                        
  f) ```bert-distilbert.ipynb``` - In this notebook, I have trained two bert models, one is the original bert and other is distilbert. The results can be seen in the notebook.([Kaggle Notebook](https://www.kaggle.com/adityakumar01/bert-distilbert)  ). With bert I was getting the highest accuracy which is 0.64(this result is not available in the latest version of notebook provided above, so check this [version](https://www.kaggle.com/adityakumar01/bert-distilbert?scriptVersionId=32581570)), but the problem with bert is it's size which is 428 mb for "bert-base-uncased", I have also tried to deploy it on heroku, but with the accompanying libraries slug size beacomes 1.2GB. So. It's not possible to deploy bert. But still I have also trained another version of bert which is distilbert whose size is approx. 200 mb less than the bert, but "distilbert" is also not appropriate for deployment on heroku, because again the slug size will be more than 500 mb.                                                                                                  
  
## Comparison of Different Classifiers with Differnt Vectors
  
|         | LGR   | XGB   | NB    | SVM   |
|---------|-------|-------|-------|-------|
| TFIDF   | 0.617 | 0.588 | 0.576 | 0.577 |
| COUNT   | 0.621 | 0.590 | 0.611 | 0.621 |
| SVD     |       | 0.577 |       | 0.481 |
| SVD_SC  |       |       |       | 0.513 |
| SMOTE_C | 0.454 |       |       |       |

SVD - Singular Value Decompostion used in svm-classifier notebook.                                                             
SVD_SC - SVD with Scaling used in svm-classifier notebook.                                                                     
SMOTE_C - SMOTE oversampling with Count Vectors used in machine-learning notebook.
SVM - The results are shown for SGDClassfier.

**NOTE**: The table above doesn't contain results or we can say columns to show full comparison. It just shows the best of results.

## What worked ?
1. Logistic Regression is best of all classifiers but the other classifiers like XGBoost can also give better results if hyperparameters are tuned.
2. BERT worked in terms of accuracy as it has the highest accuracy which is 0.644 but the differnce in accuracy with logistics regression is not much which 1.2%.
3. Instead of using tokenization pattern defined in TFIDF and Count Vectorizer, I have tried to use custom tokenizer function, which actually gave better accuracies the increase was just of 1%.(the accuracy in the table for SVM, Naive Bayes, Logistic Regression are without custom tokenizer).
4. In SVMs, SGDClassifier worked best out of SGD, LinearSVC and SVC and with count vectors it gave the highest accuracy of 0.62.
5. Out of vectors, the Count Vectorizer gave better accuarcies always compared to another as seen on the above table. With SVMs and Naive Bayes the differnce is huge which is of 4-5%.

## What didn't worked?
1. SVC didn't worked as it was taking a lot of time to converge without restricting it's "max_iter" parameter.
2. BERT could not be used for production or deployment because of model size which increases the slug size.
3. The vectors with tokenization function didn't worked because while running the flask app with gunicorn as it's was failing in calling the tokenization function. It is happening because of gunicorn multithreading. It was working fine without gunicorn i.e, directly with "flask run".
4. The paraphrasing augmentation can't be used because it was taking a lot of time for completing the augmentation of whole dataset. I have tried to split the dataset into parts and start the two kernels simultaneously for augmentation with the two splited dataset, but a single kernel took more than 9 hrs(The maximum time to run kernel on kaggle in 9 hrs).
  
## Important Points
1. I have not gone for every posssible combination of classifiers and vectors because it was not necessary.
2. The hyperparameters which are used are based on different kaggle notebooks that I have seen during my research and learning for this task.
3. I have only used SMOTE with Logistic Regression because of the above results shown in table we can see logistic regression is best.
