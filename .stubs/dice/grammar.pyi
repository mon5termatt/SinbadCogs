# These stubs are possibly wrong.
# They were generated with monkeytype and are "good enough"
# After some minor corrections
from pyparsing import Forward, MatchFirst, Or, Suppress, _WordRegex
from typing import Callable, List, Tuple, Union

def operatorPrecedence(
    base: _WordRegex,
    operators: List[
        Union[
            Tuple[Or, int, object, Callable, MatchFirst],
            Tuple[Suppress, int, object, Callable],
        ]
    ],
) -> Forward: ...
