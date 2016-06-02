from charms.reactive import (
    RelationBase,
    scopes,
    hook
)

class ProvidesBenchmarkCollector(RelationBase):
    scope = scopes.GLOBAL
    
    @hook('{provides:benchmark-collector}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')
    
    @hook('{provides:benchmark-collector}-relation-{broken,departed}')
    def departed(self):
        self.remove_state('{relation_name}.connected')
