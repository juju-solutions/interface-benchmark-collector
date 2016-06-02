from charms.reactive import (
    RelationBase,
    scopes,
    hook
)

class RequiresBenchmarkCollector(RelationBase):
    scope = scopes.UNIT
    
    @hook('{requires:benchmark-collector}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')

    @hook('{requires:benchmark-collector}-relation-{broken,departed}')
    def departed(self):
        self.remove_state('{relation_name}.connected')
        