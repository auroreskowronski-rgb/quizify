"""Quizifytimer module"""

import time

__author__ = "skowro_j"


class Timer:
    """Minuteur simple."""

    def __init__(self, duration: int = 5):
        """Initialise le minuteur avec une durée en secondes."""
        self.duration = duration
        self._start = None

    def start(self):
        """Démarre le minuteur."""
        # Monotonic time est utilisé pour 
        # éviter les problèmes liés aux changements d'heure système.
        self._start = time.monotonic()

    def remaining(self) -> float:
        """Retourne le temps restant en secondes."""
        if self._start is None:
            return float(self.duration)
        return max(0.0, self.duration - (time.monotonic() - self._start))

    def is_finished(self) -> bool:
        """Indique si le temps est écoulé."""
        return self.remaining() <= 0
