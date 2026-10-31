import pytest

from travel_assistant.tools.culture_tools import get_local_culture_info


def test_known_destination_returns_all_sections():
    result = get_local_culture_info("Cusco")

    assert result["status"] == "success"
    assert len(result["dishes"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["phrases"]) >= 1


def test_phrases_have_phrase_and_meaning():
    result = get_local_culture_info("Paris")

    for item in result["phrases"]:
        assert item["phrase"]
        assert item["meaning"]


@pytest.mark.parametrize("name", ["París", "paris", "  PARIS  ", "Parìs"])
def test_destination_is_normalized(name):
    assert get_local_culture_info(name)["status"] == "success"


def test_destination_inside_longer_text():
    assert get_local_culture_info("Machu Picchu y Cusco")["status"] == "success"


def test_unknown_destination_is_not_found():
    result = get_local_culture_info("Tokio")

    assert result["status"] == "not_found"
    assert "verify" in result["message"].lower()


@pytest.mark.parametrize("value", ["", "   ", None, 123])
def test_invalid_destination_is_error(value):
    assert get_local_culture_info(value)["status"] == "error"
