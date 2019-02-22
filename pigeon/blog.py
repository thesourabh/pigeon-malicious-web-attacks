from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from pigeon.auth import login_required
from pigeon.db import get_db

bp = Blueprint('blog', __name__)

def get_user_id(username):
    db = get_db()
    id = db.execute(
        'SELECT id '
        ' FROM user u WHERE username = ?',
        (username,)
    ).fetchone()[0]

    return id

def get_user_relation(uid1, uid2):
    db = get_db()
    relation = db.execute(
        'SELECT type'
        ' FROM relation r WHERE user_id_1 = ? AND user_id_2 = ?',
        (str(uid1), str(uid2))
    ).fetchone()

    if relation:
        return relation[0]

    return '0'


def get_user_info(uid):
    db = get_db()
    info = db.execute(
        'SELECT * FROM user where id = ?',
        (str(uid),)
    ).fetchone()

    return info


@bp.route('/')
@login_required
def index():
    """Show all the posts, most recent first."""

    uid = g.user['id']

    db = get_db()
    posts = db.execute(
        'SELECT p.id, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.author_id in (SELECT user_id_2 from relation WHERE user_id_1 = ? AND type = 1)'
        ' ORDER BY created DESC',
        (str(uid), )
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = get_db().execute(
        'SELECT p.id, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == 'POST':
        body = request.form['body']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (body, author_id)'
                ' VALUES (?, ?)',
                (body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == 'POST':
        body = request.form['body']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET body = ? WHERE id = ?',
                (body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/user/<string:username>', methods=('GET', 'POST'))
@login_required
def user(username):
    db = get_db()
    posts = db.execute(
        'SELECT p.id, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id WHERE username = ?'
        ' ORDER BY created DESC',
        (username,)
    ).fetchall()

    my_id = g.user['id']
    their_id = get_user_id(username)
    relation = get_user_relation(my_id,their_id)

    info = get_user_info(their_id)

    return render_template('blog/user.html', posts=posts, relation=int(relation), info=info)


@bp.route('/user/<string:username>', methods=('GET', 'POST'))
@login_required
def follow(username):
    return user(username)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
