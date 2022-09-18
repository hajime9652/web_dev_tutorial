from neomodel import config
from neomodel import StructuredNode, RelationshipTo, RelationshipFrom
from neomodel import StringProperty, BooleanProperty, UniqueIdProperty
from neomodel.cardinality import ZeroOrOne, ZeroOrMore

config.DATABASE_URL = 'bolt://neo4j:password@main-store:7687'

#Models
class User(StructuredNode):
    #Attributes
    uid = UniqueIdProperty()
    email = StringProperty(unique_index=True, required=True)
    hashed_password = StringProperty(unique_index=True, required=True)
    username = StringProperty()
    is_active = BooleanProperty(dedault=True)

    # Relationships
    items = RelationshipTo('Item', 'HAS', cardinality=ZeroOrMore)

    def to_json(self):
        props = self.__properties__
        del props['id']
        items = [item.__properties__ for item in self.items.all()]
        if len(items) == 0:
            return props
        for item in items:
            del item['id']
        props['items'] = items
        return props

class Item(StructuredNode):
    #Attributes
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)

    #Relationships
    owner = RelationshipFrom('User', 'HAS', cardinality=ZeroOrOne)

    def to_json(self):
        props = self.__properties__
        del props['id']
        owner = self.owner.single()
        if owner is None:
            return props
        owner = owner.__properties__
        del owner['id']
        props['owner'] = owner
        return props

