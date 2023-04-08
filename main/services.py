from .models import Card, CardHistory
from typing import List, Dict


class CardService:
    def get_objects(self) -> List[Card]:
        """Returns a queryset of all Card records in the database"""
        return Card.objects.all()
    
    def get_object_by_id(self, id: int) -> Card:
        """Returns a single Card record by id"""
        return Card.objects.get(id=id)
    
    def create_object(self, **data: Dict) -> Card:
        """Creates a new Card record in the database"""
        return Card.objects.create(**data)
    
    def update_object(self, id: int, **data: Dict) -> Card:
        """Updates an existing Card record in the database"""
        object = Card.objects.get(id=id)

        for key, value in data.items():
            setattr(object, key, value)

        object.save()

        return object

    def delete_object(self, id: int) -> None:
        """Deletes an existing Card record in the database"""
        object = Card.objects.get(id=id)
        object.delete()


class CardHistoryService:
    def get_objects(self) -> List[CardHistory]:
        """Returns a queryset of all Card records in the database"""
        return CardHistory.objects.all()
    
    def filter_object_by_id(self, id: int) -> CardHistory:
        """Returns a single Card record by id"""
        return CardHistory.objects.filter(card_id=id)
    
    def create_object(self, **data: Dict) -> CardHistory:
        """Creates a new Card record in the database"""
        return CardHistory.objects.create(**data)
    
    def update_object(self, id: int, data: Dict) -> CardHistory:
        """Updates an existing Card record in the database"""
        object = CardHistory.objects.get(id=id)

        for key, value in data.items():
            setattr(object, key, value)

        object.save()

        return object

    def delete_object(self, id: int) -> None:
        """Deletes an existing Card record in the database"""
        object = CardHistory.objects.get(id=id)
        object.delete()
