import json
import pandas as pd
from flask import jsonify
from preprocessing import clean_RNN

import global_variables

from utils.comment_scrapping import get_certain_comments
from utils.prediction_utils import run_model_prediction


def get_Comment_Analysis_RNN(comments: list):
    """
    Analyze YouTube comments using RNN sentiment analysis model.

    Args:
        comments (list): A list of comments to be analyzed.

    Returns:
        JSON response containing comments and their sentiment scores.
    """

    df_predict = pd.DataFrame(
        columns=["comment", "type", "negative_score", "neutral_score", "positive_score"]
    )
    try:
        if comments is None or len(comments) == 0:
            return (
                jsonify({"error": "(Comment Analysis RNN) No comments provided"}),
                400,
            )

        for comment in comments:
            initComment = comment
            comment = clean_RNN(comment)
            if comment and comment != "" and comment != ".":
                # Call the run_model_prediction function
                sentiment_type, scores = run_model_prediction(
                    global_variables.global_tokenizer_RNN,
                    global_variables.global_model_RNN,
                    comment,
                    maxlen=100,
                )

                # Create a new row for the DataFrame
                new_row = {
                    "comment": initComment,
                    "type": sentiment_type,
                    "negative_score": round(scores[0] * 100, 2),
                    "neutral_score": round(scores[1] * 100, 2),
                    "positive_score": round(scores[2] * 100, 2),
                }

                df_predict.loc[len(df_predict)] = new_row

        # # Convert DataFrame to JSON
        json_result = df_predict.to_json(orient="records")

        # Load JSON string back to Python object and return as JSON
        return jsonify({"comments": json.loads(json_result)})
    except Exception as e:
        return jsonify({"error": f"(Comment Analysis RNN) {str(e)}"}), 500


def get_Comment_Analysis_pagination_RNN(page_number):
    """
    Analyze YouTube comments in paginated manner using Roberta model.

    Args:
        page_number (int): The current page number of comments.

    Returns:
        JSON response containing comments and their sentiment scores.
    """
    df_predict = pd.DataFrame(
        columns=["comment", "type", "negative_score", "neutral_score", "positive_score"]
    )
    try:
        page_number = int(page_number)
        # Fetch paginated comments
        comments = get_certain_comments(
            comment_list=global_variables.global_comment_list, page_number=page_number
        )

        if comments is None or len(comments) == 0:
            return (
                jsonify(
                    {"error": "(Comment Analysis RNN Pagination) No comments provided"}
                ),
                400,
            )

        for comment in comments:
            if not isinstance(comment, str):
                continue

            initComment = comment
            comment = clean_RNN(comment)

            if comment and comment != "" and comment != ".":
                # Call the run_model_prediction function
                sentiment_type, scores = run_model_prediction(
                    global_variables.global_tokenizer_RNN,
                    global_variables.global_model_RNN,
                    comment,
                    maxlen=100,
                )
                # Append the comment and its sentiment scores to the DataFrame
                new_row = {
                    "comment": initComment,
                    "type": sentiment_type,
                    "negative_score": round(scores[0] * 100, 2),
                    "neutral_score": round(scores[1] * 100, 2),
                    "positive_score": round(scores[2] * 100, 2),
                }

                df_predict.loc[len(df_predict)] = new_row

        # # Convert DataFrame to JSON
        json_result = df_predict.to_json(orient="records")

        # Load JSON string back to Python object and return as JSON
        return jsonify({"comments": json.loads(json_result)})
    except Exception as e:
        return (
            jsonify({"error": f"(Comment Analysis RNN Pagination) {str(e)}"}),
            500,
        )

