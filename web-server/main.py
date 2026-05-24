import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,]

@app.get("/categories")
def get_categories():
    return store.get_categories()

@app.get("/contact", response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Contact</h1>
        <p>This is the contact page.
            lilseniorj
        </p>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()