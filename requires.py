from charms.reactive import (
    RelationBase,
    scopes,
    hook
)

class ProvidesBenchmarkCollector(RelationBase):
    scope = scopes.UNIT
    
    @hook('{requires:benchmark-collector}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')
