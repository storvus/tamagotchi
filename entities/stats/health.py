import logging

from entities.stats._base import Stat


class Health(Stat):
    _max_level = 100
    _increased_by = 1
    _critical_threshold = 25
    _logger = logging.getLogger(__name__)

    def __init__(self, game, *arg, **kwargs) -> None:
        super().__init__(game, *arg, **kwargs)
        self.__harm_level = 0

    def _update(self):
        if self._harm_level:
            self.decrease_level(self._harm_level)
        elif self._level < self._max_level:
            self.increase_level(self._increased_by)
        self._logger.debug(f"Health level: {self._level}")

        if self._level <= 0:
            self._logger.debug("Killing the pet!")
            self._game.kill_pet()

    def is_critical_level(self) -> bool:
        return self._level <= self._critical_threshold

    def _next_check_point_period_secs(self) -> int:
        return 1

    def _get_init_level(self) -> int:
        return 100

    def set_harm_level(self, value):
        self.__harm_level = value

    @property
    def _harm_level(self) -> int:
        return self.__harm_level
