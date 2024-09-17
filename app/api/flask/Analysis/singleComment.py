from flask import request, jsonify
from preprocessing import preprocessing_RNN
import global_variables

from Analysis.roberta import preprocess_Roberta, tokenizer_Roberta, model_Roberta

from utils.prediction_utils import run_model_prediction, run_roberta_prediction
from utils.utils import filter_english_comments, remove_emojis


def single_comment_analysis():
    """
    Analyze a single comment using multiple models: LSTM, GRU, RNN, and Roberta.

    This function takes a text comment passed via query parameters and returns a sentiment analysis
    score using various models. Each model returns a sentiment type (negative, neutral, positive)
    along with the probability scores for each sentiment.

    Returns:
        JSON: A response object containing sentiment analysis results from each model.
    """
    # Retrieve the comment from query parameters
    comment = request.args.get("text")
    initComment = comment  # Preserve original comment for Roberta
    print(f"Sentiment  Analysis of : {comment}\n")

    # Handle the case where no comment is provided
    if comment is None:
        return jsonify({"error": "Failed to retrieve comment"}), 500

    # Remove emojis from the comment to ensure only textual data remains
    comment = remove_emojis(comment)
    print(f"Comment after emoji removal: {comment}\n")

    # Filter out non-English comments
    comment = filter_english_comments(comment)
    print(f"Filtered English comment: {comment}\n")

    if not comment or comment == "" or comment == ".":
        return jsonify({"error": "Text is not in English"}), 500

    # Preprocess the comment for use in RNN-based models
    comment = preprocessing_RNN(comment)

    # Prepare the comment for the Roberta model
    comment_rob = preprocess_Roberta(initComment)

    if (
        not comment_rob
        or comment_rob == ""
        or comment_rob == "."
        or not comment
        or comment == ""
        or comment == "."
    ):
        return (
            jsonify(
                {
                    "error": "Text cannot be analyzed as text is empty after preprocessing"
                }
            ),
            500,
        )
    else:
        # LSTM prediction
        type_LSTM, scores_LSTM = run_model_prediction(
            global_variables.tokenizer_LSTM, global_variables.LSTM, comment, maxlen=50
        )

        # GRU prediction
        type_GRU, scores_GRU = run_model_prediction(
            global_variables.tokenizer_LSTM, global_variables.GRU, comment, maxlen=50
        )

        # RNN prediction
        type_RNN, scores_RNN = run_model_prediction(
            global_variables.tokenizer_RNN, global_variables.RNN, comment, maxlen=100
        )

        # Roberta prediction
        type_roberta, scores_roberta = run_roberta_prediction(
            tokenizer_Roberta, model_Roberta, comment_rob
        )

        # Construct the JSON response containing the results from all models
        return jsonify(
            {
                "comment": initComment,
                "LSTM": {
                    "type": type_LSTM,
                    "negative_score": round(scores_LSTM[0] * 100, 2),
                    "neutral_score": round(scores_LSTM[1] * 100, 2),
                    "positive_score": round(scores_LSTM[2] * 100, 2),
                },
                "GRU": {
                    "type": type_GRU,
                    "negative_score": round(scores_GRU[0] * 100, 2),
                    "neutral_score": round(scores_GRU[1] * 100, 2),
                    "positive_score": round(scores_GRU[2] * 100, 2),
                },
                "RNN": {
                    "type": type_RNN,
                    "negative_score": round(scores_RNN[0] * 100, 2),
                    "neutral_score": round(scores_RNN[1] * 100, 2),
                    "positive_score": round(scores_RNN[2] * 100, 2),
                },
                "Roberta": {
                    "type": type_roberta,
                    "negative_score": round(scores_roberta[0] * 100, 2),
                    "neutral_score": round(scores_roberta[1] * 100, 2),
                    "positive_score": round(scores_roberta[2] * 100, 2),
                },
            }
        )


# def single_comment_analysis():
#     comment = request.args.get("text")
#     initComment = comment
#     print(f"comment {comment}")
#     if comment is None:
#         return jsonify({"error": "Failed to retrieve Text"}), 500
#     comment = removeemoji(comment)
#     print(f"emoji {comment}")
#     comment = filter_english_comments(comment)
#     print(f"filter {comment}")

#     comment = preprocessing_RNN(comment)
#     if not comment or comment == "" or comment == ".":
#         return jsonify({"error": "Text is not in english Language"}), 500
#     else:
#         sequence = tokenizer_LSTM.texts_to_sequences([comment])
#         padded_sequences = pad_sequences(sequence, maxlen=50)
#         prediction_LSTM = lstm.predict(padded_sequences)
#         result1_LSTM = prediction_LSTM.tolist()
#         result_LSTM = result1_LSTM[0]
#         type_LSTM = np.argmax(np.array(result_LSTM))
#         type_LSTM = 0 if type_LSTM == 0 else 4 if type_LSTM == 2 else 2

#         prediction_GRU = gru.predict(padded_sequences)
#         result1_GRU = prediction_GRU.tolist()
#         result_GRU = result1_GRU[0]
#         type_GRU = np.argmax(np.array(result_GRU))
#         type_GRU = 0 if type_GRU == 0 else 4 if type_GRU == 2 else 2

#         sequence_RNN = tokenizer_RNN.texts_to_sequences([comment])
#         padded_sequences_RNN = pad_sequences(sequence_RNN, maxlen=100)
#         prediction_RNN = rnn.predict(padded_sequences_RNN)
#         prediction_RNN = prediction_RNN.tolist()
#         result_RNN = prediction_RNN[0]
#         type_RNN = np.argmax(np.array(result_RNN))
#         type_RNN = 0 if type_RNN == 0 else 4 if type_RNN == 2 else 2

#         comment_rob = preprocess_Roberta(initComment)
#         if not comment_rob or comment_rob == "" or comment_rob == ".":
#             return jsonify({"error": "Text is not in english Language"}), 500
#         else:
#             encoded_input = tokenizer_Roberta(comment, return_tensors="tf")
#             output = model_Roberta(encoded_input)
#             scores = output[0][0].numpy()
#             scores = softmax(scores)
#             type_roberta = np.argmax(np.array(scores))
#             type_roberta = 0 if type_roberta == 0 else 4 if type_roberta == 2 else 2
#             return jsonify(
#                 {
#                     "comment": initComment,
#                     "LSTM": {
#                         "type": type_LSTM,
#                         "negative_score": round(result_LSTM[0] * 100, 2),
#                         "neutral_score": round(result_LSTM[1] * 100, 2),
#                         "positive_score": round(result_LSTM[2] * 100, 2),
#                     },
#                     "GRU": {
#                         "type": type_GRU,
#                         "negative_score": round(result_GRU[0] * 100, 2),
#                         "neutral_score": round(result_GRU[1] * 100, 2),
#                         "positive_score": round(result_GRU[2] * 100, 2),
#                     },
#                     "RNN": {
#                         "type": type_RNN,
#                         "negative_score": round(result_RNN[0] * 100, 2),
#                         "neutral_score": round(result_RNN[1] * 100, 2),
#                         "positive_score": round(result_RNN[2] * 100, 2),
#                     },
#                     "Roberta": {
#                         "type": type_roberta,
#                         "negative_score": round(scores[0] * 100, 2),
#                         "neutral_score": round(scores[1] * 100, 2),
#                         "positive_score": round(scores[2] * 100, 2),
#                     },
#                 }
#             )
