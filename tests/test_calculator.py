from unittest.mock import MagicMock, Mock, patch

import pytest

from src.type_calculator import TypeCalculator

# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def type_calculator():
    return TypeCalculator()


# ============================================================================
# Tests for TypeCalculator
# ============================================================================


class TestTypeCalculator:

    def test_initialization(self, type_calculator):
        assert len(type_calculator.type_chart) == 0
