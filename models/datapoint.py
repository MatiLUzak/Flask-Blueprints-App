from . import db
from sqlalchemy.orm import Mapped, mapped_column
class DataPoint(db.Model):
    __tablename__ = 'datapoints'
    id: Mapped[int] = mapped_column(primary_key=True)
    feature1: Mapped[float] = mapped_column(nullable=False)
    feature2: Mapped[float] = mapped_column(nullable=False)
    category: Mapped[int] = mapped_column(nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'feature1': self.feature1,
            'feature2': self.feature2,
            'category': self.category,
        }