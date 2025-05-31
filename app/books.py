from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .decorators import role_required
from .models import db, Book
from .forms import BookForm

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/')
@login_required
def index():
    books = Book.query.all()
    return render_template('books/index.html', books=books)

@books_bp.route('/create', methods=['GET', 'POST'])
@login_required
@role_required('create')
def create():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            year=form.year.data,
            added_by=current_user.id
        )
        db.session.add(book)
        db.session.commit()
        flash('Книга успешно добавлена!', 'success')
        return redirect(url_for('books.index'))
    return render_template('books/create.html', form=form)

# Аналогичные обработчики для edit, delete, detail