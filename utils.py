from newspaper import Article
import sqlite3
import newspaper


def get_all(query):
    conn = sqlite3.connect("data/newsdb.db")
    data = conn.execute(query).fetchall()
    conn.close()
    return data


def get_news_by_id(news_id):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    SELECT N.subject, N.description, N.image, N.original_url, C.Name, C.url 
    FROM news N Inner Join category C On N.category_id = C.id 
    WHERE N.id=?
    '''
    data = conn.execute(sql, (news_id, )).fetchone()
    conn.close()
    return data


def get_news_url():
    cats = get_all("SELECT * FROM category")
    conn = sqlite3.connect("data/newsdb.db")
    for cat in cats:
        print(cat[1])
        cat_id = cat[0]
        url = cat[2]
        cat_paper = newspaper.build(url)
        for article in cat_paper.articles:
            try:
                print("===", article.url)
                add_news(conn, article.url, cat_id)
            except Exception as ex:
                print("ERROR: " + str(ex))
    conn.close()


def add_comment(news_id, content):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    INSERT INTO comment(content, news_id) VALUES(?, ?)
    '''
    conn.execute(sql, (content, news_id))
    conn.commit()
    conn.close()


def add_news(conn, url, category_id):
    sql = '''
    INSERT INTO news(subject, description, image, original_url, category_id)
    VALUES (?, ?, ?, ?, ?)
    '''
    article = Article(url)
    article.download()
    article.parse()

    conn.execute(sql, (article.title, article.text, article.top_img, article.url, category_id))
    conn.commit()


if __name__ == "__main__":
    get_news_url()
