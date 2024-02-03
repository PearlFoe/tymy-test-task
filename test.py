import pytest

from main import parse


@pytest.mark.parametrize(
    "inp,outp",
    [
        (
            {"a": "1"},
            {"a": "1"},
        ),
        (
            {"a": {"b": "1"}},
            {"a_b": "1"},  
        ),
        (
            ["1", "2"],
            {"0": "1", "1": "2"},  
        ),
        (
            ["a", {"s": "1"}],
            {"0": "a", "1_s": "1"},
        ),
        (
            {"a": ["1","2"]},
            {"a_0": "1", "a_1": "2"},    
        ),
        (
            {"a": [{"b": "1"}, {"c": "2"}]},
            {"a_0_b": "1", "a_1_c": "2"},
        ),
        (
            {"qwerty": {"ewq": "aaaaaa"}},
            {"qwerty_ewq": "aaaaaa"},  
        ),
        (
            {"a": [{"b": "1"}, {"c": "2"}, [{"ddd": {"eee": "3"}}]]},
            {"a_0_b": "1", "a_1_c": "2", "a_2_0_ddd_eee": "3"},
        ),
    ]
)
def test_parse(inp, outp):
    assert parse(inp) == outp
