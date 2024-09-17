from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import tokenizer_from_json
import pickle

commentCountPerPage: int = 12

# # Load Keras model
# lstm = load_model("app/api/flask/Model/LSTM_sentimentmodel.h5")
# rnn = load_model("app/api/flask/Model/RNN_sentimentmodel.h5")
# gru = load_model("app/api/flask/Model/GRU_sentimentmodel.h5")
# # rnn = load_model('app/api/flask/rnnmodel.h5')

# tokenizer_LSTM = Tokenizer()
# with open("app/api/flask/Tokenizer/LSTMtokenizer.pkl", "rb") as tokenizer_file:
#     tokenizer_LSTM = pickle.load(tokenizer_file)

# tokenizer_RNN = Tokenizer()
# with open("app/api/flask/Tokenizer/RNNtokenizer.pkl", "rb") as tokenizer_file_RNN:
#     tokenizer_RNN = pickle.load(tokenizer_file_RNN)


# Dictionary containing filenames and their corresponding Google Drive file IDs
file_ids = {
    "LSTMtokenizer.pkl": "https://drive.google.com/uc?id=1N4GEIE-5S4w__5zkb6nfMemdvitFKlt8",
    "RNNtokenizer.pkl": "https://drive.google.com/uc?id=1a0j2ZFgve0gBc8viw5xd6yyf6pnh4lXQ",
    "GRU_sentimentmodel.h5": "https://drive.google.com/uc?id=1bT7A40Iq8zcV3jy4ZwOir6NM0CfbRI5Z",
    "LSTM_sentimentmodel.h5": "https://drive.google.com/uc?id=1u_XMGhnlOcIqTqaid1K8p-azeuLzlhBH",
    "RNN_sentimentmodel.h5": "https://drive.google.com/uc?id=1PZOjp-IasfKuiidblk3hEBfcQslWk90E",
    "rnnmodel.h5": "https://drive.google.com/uc?id=1HvGBifFz_Rj_9CAKbrNr92-JGPj-rRZD",
}


words_to_remove = [
    "y",
    "ain",
    "aren",
    "aren't",
    "couldn",
    "couldn't",
    "didn",
    "didn't",
    "doesn",
    "doesn't",
    "hadn",
    "hadn't",
    "hasn",
    "hasn't",
    "haven",
    "haven't",
    "isn",
    "isn't",
    "ma",
    "mightn",
    "mightn't",
    "mustn",
    "mustn't",
    "needn",
    "needn't",
    "shan",
    "shan't",
    "shouldn",
    "shouldn't",
    "wasn",
    "wasn't",
    "weren",
    "weren't",
    "won",
    "won't",
    "wouldn",
    "wouldn't",
    "not",
]

contractions = {
    "ilove": "i love",
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "could've": "could have",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'll": "he will",
    "he's": "he is",
    "how'd": "how did",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'll": "I will",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'd": "it would",
    "it'll": "it will",
    "it's": "it is",
    "let's": "let us",
    "might've": "might have",
    "mightn't": "might not",
    "must've": "must have",
    "mustn't": "must not",
    "needn't": "need not",
    "oughtn't": "ought not",
    "shan't": "shall not",
    "she'd": "she would",
    "she'll": "she will",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "that's": "that is",
    "there'd": "there would",
    "there'll": "there will",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'll": "we will",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "where'd": "where did",
    "where's": "where is",
    "who'd": "who would",
    "who'll": "who will",
    "who's": "who is",
    "won't": "will not",
    "would've": "would have",
    "wouldn't": "would not",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have",
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'll": "he will",
    "he's": "he is",
    "how'd": "how did",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'll": "I will",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'd": "it would",
    "it'll": "it will",
    "it's": "it is",
    "let's": "let us",
    "might've": "might have",
    "mightn't": "might not",
    "must've": "must have",
    "mustn't": "must not",
    "needn't": "need not",
    "oughtn't": "ought not",
    "shan't": "shall not",
    "she'd": "she would",
    "she'll": "she will",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "that's": "that is",
    "there'd": "there would",
    "there'll": "there will",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'll": "we will",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "where'd": "where did",
    "where's": "where is",
    "who'd": "who would",
    "who'll": "who will",
    "who's": "who is",
    "won't": "will not",
    "would've": "would have",
    "wouldn't": "would not",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have",
    "I'd've": "I would have",
    "he'd've": "he would have",
    "it'd've": "it would have",
    "she'd've": "she would have",
    "we'd've": "we would have",
    "they'd've": "they would have",
    "should've": "should have",
    "shouldn't've": "should not have",
    "could've": "could have",
    "couldn't've": "could not have",
    "might've": "might have",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't've": "must not have",
    "needn't've": "need not have",
    "oughtn't've": "ought not have",
    "shan't've": "shall not have",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't've": "would not have",
    "you'd've": "you would have",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have",
    "aint": "am not",
    "arent": "are not",
    "cant": "cannot",
    "couldve": "could have",
    "couldnt": "could not",
    "didnt": "did not",
    "doesnt": "does not",
    "dont": "do not",
    "hadnt": "had not",
    "hasnt": "has not",
    "havent": "have not",
    "hed": "he would",
    "hell": "he will",
    "hes": "he is",
    "howd": "how did",
    "howll": "how will",
    "hows": "how is",
    "Id": "I would",
    "Ill": "I will",
    "Im": "I am",
    "Ive": "I have",
    "isnt": "is not",
    "itd": "it would",
    "itll": "it will",
    "its": "it is",
    "lets": "let us",
    "mightve": "might have",
    "mightnt": "might not",
    "mustve": "must have",
    "mustnt": "must not",
    "neednt": "need not",
    "oughtnt": "ought not",
    "shant": "shall not",
    "shed": "she would",
    "shell": "she will",
    "shes": "she is",
    "shouldve": "should have",
    "shouldnt": "should not",
    "thats": "that is",
    "thered": "there would",
    "therell": "there will",
    "theres": "there is",
    "theyd": "they would",
    "theyll": "they will",
    "theyre": "they are",
    "theyve": "they have",
    "wasnt": "was not",
    "wed": "we would",
    "well": "we will",
    "were": "we are",
    "weve": "we have",
    "werent": "were not",
    "whatll": "what will",
    "whatre": "what are",
    "whats": "what is",
    "whatve": "what have",
    "whered": "where did",
    "wheres": "where is",
    "whod": "who would",
    "wholl": "who will",
    "whos": "who is",
    "wont": "will not",
    "wouldve": "would have",
    "wouldnt": "would not",
    "youd": "you would",
    "youll": "you will",
    "youre": "you are",
    "youve": "you have",
    "arent": "are not",
    "cant": "cannot",
    "couldnt": "could not",
    "didnt": "did not",
    "doesnt": "does not",
    "dont": "do not",
    "hadnt": "had not",
    "hasnt": "has not",
    "havent": "have not",
    "hed": "he would",
    "hell": "he will",
    "hes": "he is",
    "howd": "how did",
    "howll": "how will",
    "hows": "how is",
    "Id": "I would",
    "Ill": "I will",
    "Im": "I am",
    "Ive": "I have",
    "isnt": "is not",
    "itd": "it would",
    "itll": "it will",
    "its": "it is",
    "lets": "let us",
    "mightve": "might have",
    "mightnt": "might not",
    "mustve": "must have",
    "mustnt": "must not",
    "neednt": "need not",
    "oughtnt": "ought not",
    "shant": "shall not",
    "shed": "she would",
    "shell": "she will",
    "shes": "she is",
    "she'd": "she would",
    "shouldve": "should have",
    "shouldnt": "should not",
    "thats": "that is",
    "thered": "there would",
    "therell": "there will",
    "theres": "there is",
    "theyd": "they would",
    "theyll": "they will",
    "theyre": "they are",
    "theyve": "they have",
    "wasnt": "was not",
    "wed": "we would",
    "well": "we will",
    "were": "we are",
    "weve": "we have",
    "werent": "were not",
    "whatll": "what will",
    "whatre": "what are",
    "whats": "what is",
    "whatve": "what have",
    "whered": "where did",
    "wheres": "where is",
    "whod": "who would",
    "wholl": "who will",
    "whos": "who is",
    "wont": "will not",
    "wouldve": "would have",
    "wouldnt": "would not",
    "youd": "you would",
    "youll": "you will",
    "youre": "you are",
    "youve": "you have",
    "Idve": "I would have",
    "hedve": "he would have",
    "itdve": "it would have",
    "shedve": "she would have",
    "wedve": "we would have",
    "theydve": "they would have",
    "shouldve": "should have",
    "shouldntve": "should not have",
    "couldve": "could have",
    "couldntve": "could not have",
    "mightve": "might have",
    "mightntve": "might not have",
    "mustve": "must have",
    "mustntve": "must not have",
    "needntve": "need not have",
    "oughtntve": "ought not have",
    "shantve": "shall not have",
    "wontve": "will not have",
    "wouldve": "would have",
    "wouldntve": "would not have",
    "youdve": "you would have",
    "youllve": "you will have",
    "youre": "you are",
    "youve": "you have",
}
