from app import db

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    one = db.Column(db.String(120), index=True)
    two = db.Column(db.String(120), index=True)
    three = db.Column(db.String(120), index=True)
    four = db.Column(db.String(120), index=True)
    five = db.Column(db.String(120), index=True)
    six = db.Column(db.String(120), index=True)
    seven = db.Column(db.String(120), index=True)
    eight = db.Column(db.String(120), index=True)
    nine = db.Column(db.String(120), index=True)
    ten = db.Column(db.String(120), index=True)
    eleven = db.Column(db.String(120), index=True)
    twelve = db.Column(db.String(120), index=True)
    thirteen = db.Column(db.String(120), index=True)
    fourteen = db.Column(db.String(120), index=True)
    sixteen = db.Column(db.String(120), index=True)
    seventeen = db.Column(db.String(120), index=True)
    eighteen = db.Column(db.String(120), index=True)
    nineteen = db.Column(db.String(120), index=True)
    twenty = db.Column(db.String(120), index=True)
    tags = db.Column(db.String(500))


    def __repr__(self):
        return '<Table {}>'.format(self.name)
