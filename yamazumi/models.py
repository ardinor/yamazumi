from yamazumi import db

tags = db.Table('tags',
    db.Column('tag.id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('tagged.id', db.Integer, db.ForeignKey('bookmark.id'))
    )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(150), index=True, unique=True)
    password = db.Column(db.String(250))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    url = db.Column(db.String(400), index=True)
    tags = db.reationship('Tag', secondary=tags,
        backref=db.backref('bookmarks', lazy=dynamic))

    def __repr__(self):
        return '<URL %r>' % (self.url)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(120))

    def __repr__(self):
        return '<Tag %r>' % (self.tag)
