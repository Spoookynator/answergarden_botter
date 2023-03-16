import cloudscraper


def fill_out(word, session_id, base_url):
    url = base_url + session_id

    data = {"answer": word,
            "action": "websubmit",
            "id": "3084077"}

    # construct the POST request
    with cloudscraper.session() as s:  # Use a Session object.
        try:
            s.post(url, data=data)
        except Exception as e:
            print(str(e))
