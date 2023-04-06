from .models import Card


class CardService:
    def get_objects(self):
        """Returns a queryset of all Card records in the database"""
        return Card.objects.all()
    
    def get_object_by_id(self, id):
        """Returns a single Card record by id"""
        return Card.objects.get(id=id)
    
    def create_object(self, data):
        """Creates a new Card record in the database"""
        return Card.objects.create(**data)
    
    def update_object(self, id, data):
        """Updates an existing Card record in the database"""
        object = Card.objects.get(id=id)

        for key, value in data.items():
            setattr(object, key, value)

        object.save()

        return object

    def delete_object(self, id):
        """Deletes an existing Card record in the database"""
        object = Card.objects.get(id=id)
        object.delete()
