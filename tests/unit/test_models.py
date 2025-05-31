from app.models import User, Book

def test_user_creation(db):
    user = User(username='test_user', role='reader')
    user.password = 'password'
    db.session.add(user)
    db.session.commit()
    
    assert user.id is not None
    assert user.verify_password('password') is True
    assert user.verify_password('wrong') is False

def test_book_creation(db):
    user = User.query.first()
    book = Book(title='New Book', author='Author', year=2023, added_by=user.id)
    db.session.add(book)
    db.session.commit()
    
    assert book.id is not None
    assert book.added_by == user.id