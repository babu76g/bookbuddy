from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

books = []

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added!"}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return {"message": "Book updated!"}
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted!"}
    raise HTTPException(status_code=404, detail="Book not found")