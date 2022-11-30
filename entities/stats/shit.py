import logging

from entities.stats._base import Stat


class Shit(Stat):
    _max_level = 100
    _increased_by = 25
    _critical_threshold = 3
    _harm_level = 3
    _logger = logging.getLogger(__name__)

    def __init__(self, game, next_point_period: int = 5, *arg, **kwargs) -> None:
        super().__init__(game, next_point_period, *arg, **kwargs)
        self._shit_expected = 0
        self._current_shit_count = 0

    def is_critical_level(self) -> bool:
        return self._current_shit_count >= self._critical_threshold

    def _update(self):
        if self._shit_expected and self._level < self._max_level:
            self.increase_level(self._increased_by)
            self._logger.debug(f"{self.__class__.__name__} level: {self._level}")
        if self._level >= self._max_level:
            self._logger.debug("Let's shit!")
            self.shit()
        # ToDo: make pet to sick
        # if self.is_critical_level():
        #     pass

    def shit(self):
        self._logger.debug("Shitting...")
        self._level = 0
        self._current_shit_count += 1
        self._shit_expected -= 1

    def add_expected_shit(self, shit_count: int = 1):
        """
        We don't expect any shit until anything is eaten.
        We also don't expect any shit if anything was eaten and the toilet was already attended after that
        :return:
        """
        self._shit_expected += shit_count
        self._logger.debug(f"Preparing to shit... Expected times: {self._shit_expected}")

    def clear_shit(self):
        self._current_shit_count -= 1
