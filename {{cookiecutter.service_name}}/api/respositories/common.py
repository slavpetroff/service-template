from sqlalchemy.orm import Session


class BaseRepository:
    """
    Base repository class that implements common CRUD operations
    """

    def __init__(self, model_class, session: Session):
        self.model_class = model_class
        self.session = session

    def create(self, **kwargs):
        instance = self.model_class(**kwargs)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get(self, pk):
        return self.session.query(self.model_class).get(pk)

    def update(self, instance_id, **kwargs):
        instance = self.session.query(self.model_class).get(instance_id)
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        self.session.commit()
        return instance

    def delete(self, instance_id):
        instance = self.session.query(self.model_class).get(instance_id)
        self.session.delete(instance)
        self.session.commit()

    def filter(self, **kwargs):
        return self.session.query(self.model_class).filter_by(**kwargs).all()
