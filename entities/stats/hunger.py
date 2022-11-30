import logging

from entities.stats._base import Stat


class Hunger(Stat):
    _max_level = 100
    _increased_by = 1
    _harm_level = 5
    _critical_threshold = 75
    _logger = logging.getLogger(__name__)
