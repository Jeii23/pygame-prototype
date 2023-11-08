
class FactorySprites:
    def __init__(self, event_type, period, pygame):
        self._prototypes
        self._periods = period
        self._event_types = event_type

    def _make(self):
        return self._prototypes[event_type - self.event_types[0]].clone()
