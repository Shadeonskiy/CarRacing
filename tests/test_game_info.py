import sys
import os
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from gameInfo import GameInfo


@pytest.fixture
def gameInfo():
    """
    Return an object of type GameInfo
    """
    gameInfo = GameInfo()
    return gameInfo


@pytest.mark.information
class TestInformation:

    @pytest.mark.parametrize(["level", "expected_level"],
                             [(1, 2),
                              (2, 3)])
    def test_next_level(self, gameInfo, level, expected_level):
        gameInfo.level = level
        gameInfo.next_level()
        assert gameInfo.level == expected_level
        assert not gameInfo.started

    @pytest.mark.parametrize(["level", "expected_level"],
                             [(1, 1),
                              (2, 1),
                              (3, 1),
                              (4, 1)])
    def test_reset(self, gameInfo, level, expected_level):
        gameInfo.level = level
        gameInfo.reset()
        assert gameInfo.level == expected_level
        assert gameInfo.level_start_time == 0
        assert not gameInfo.started


@pytest.mark.events
class TestEvents:

    @pytest.mark.parametrize(["level", "expected_outcome"],
                             [(11, True),
                              (10, False),
                              (13, True)])
    def test_game_finished(self, gameInfo, level, expected_outcome):
        gameInfo.level = level
        assert gameInfo.game_finished() is expected_outcome
