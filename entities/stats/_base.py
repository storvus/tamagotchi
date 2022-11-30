import logging
import time

from entities.base import GameEntity


class Stat(GameEntity):

    def __init__(self, game, *arg, **kwargs) -> None:
        super().__init__(game, *arg, **kwargs)
        self._level = self._get_init_level()
        self._next_point_period = self._next_check_point_period_secs()  # shows how fast the stat grows (seconds)
        self._increase_await_time()

    def _increase_await_time(self):
        self.next_point = time.time() + self._next_point_period

    def update(self):
        if time.time() >= self.next_point:
            self._update()
            self._increase_await_time()
        return None

    def _update(self):
        if self._level < self._max_level:
            self.increase_level(self._increased_by)
            self._logger.debug(f"{self.__class__.__name__} level: {self._level}")

    def decrease_level(self, value: int):
        self._level -= value
        self._level = max(0, self._level)

    def increase_level(self, value: int):
        self._level += value
        self._level = min(self._max_level, self._level)

    def get_current_level(self) -> int:
        return self._level

    def get_max_level(self) -> int:
        return self._max_level

    def get_harm_level(self) -> int:
        return 0 if not self.is_critical_level() else self._harm_level

    def is_critical_level(self) -> bool:
        return self._level >= self._critical_threshold

    def _next_check_point_period_secs(self) -> int:
        return 5

    def _get_init_level(self) -> int:
        return 0

    @property
    def _max_level(self) -> int:
        raise NotImplementedError

    @property
    def _increased_by(self) -> int:
        raise NotImplementedError

    @property
    def _harm_level(self) -> int:
        raise NotImplementedError

    @property
    def _critical_threshold(self) -> int:
        raise NotImplementedError

    @property
    def _logger(self) -> logging.Logger:
        raise NotImplementedError
