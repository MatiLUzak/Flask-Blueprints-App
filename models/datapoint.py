from . import db
class DataPoint(db.Model):
    __tablename__ = 'datapoints'
    id = db.Column(db.Integer, primary_key=True)
    feature1 = db.Column(db.Float, nullable=False)
    feature2 = db.Column(db.Float, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'feature1': self.feature1,
            'feature2': self.feature2,
            'category': self.category,
        }