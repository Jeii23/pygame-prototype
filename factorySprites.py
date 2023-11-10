import pygame


class FactorySprites:
    def __init__(self, prototype, period, event_type):
        self._prototypes = prototype
        self._periods = period
        self.event_types = [event_type + i for i in range(len(prototype))]
        for prototype, frequency, event_type in zip(self._prototypes, self._periods, self.event_types):
            pygame.time.set_timer(event_type, frequency)

    def make(self, event_type):
        return self._prototypes[event_type - self.event_types[0]].clone()
