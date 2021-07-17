import requests
from flask import Flask, jsonify, request
import utils

app = Flask(__name__)


@app.route("/categories", methods=["GET"])
def get_categories():
    rows = utils.get_all("SELECT * FROM category")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "url": r[2],
        })
    return jsonify({"categories": data})


@app.route("/news", methods=["GET"])
def get_news():
    rows = utils.get_all("SELECT * FROM news")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "original_ulr": r[4]
        })
    return jsonify({"news": data})


@app.route("/news/<int:new_id>", methods=["GET"])
def get_news_by_id(new_id):
    r = utils.get_news_by_id(new_id)
    d = {
        "subject": r[0],
        "description": r[1],
        "image": r[2],
        "original_ulr": r[3],
        "category_name": r[4],
        "category_url": r[5]
    }
    return jsonify({"news": d})


@app.route("/news/<int:news_id>", methods=["POST"])
def insert_comment(news_id):
    # import pdb
    # pdb.set_trace()
    if request.form.get("content"):
        utils.add_comment(news_id, request.form["content"])
        return jsonify({"status": 1, "message": "Completed"})

    return jsonify({"status": -1, "message": "Need new content"})


@app.route("/news/add", methods=["POST"])
def insert_news():
    pass


if __name__ == "__main__":
    app.run()
