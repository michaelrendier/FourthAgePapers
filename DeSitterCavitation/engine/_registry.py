"""
_registry.py — minimal standalone shim of ValaQuenta.engine.registry
===================================================================
The canonical engine lives at
`ValaQuenta/modules/desitter_cavitation/` and plugs into the full
EquationModule registry there. This shim vendors just enough of that
contract (EquationModule, Equation, CONFIDENCE) so the copied engine runs
self-contained inside this paper folder. All the physics is in `maths.py`,
which is pure stdlib and needs nothing from here.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

CONFIDENCE = {
    'ESTABLISHED': '✓',
    'THEORETICAL': '◈',
    'CONJECTURE':  '◇',
    'OPEN':        '?',
}


class Equation:
    def __init__(self, name, display, latex, radian_form,
                 confidence, code_verified, params,
                 compute=None, display_options=None):
        self.name = name
        self.display = display
        self.latex = latex
        self.radian_form = radian_form
        self.confidence = confidence
        self.code_verified = code_verified
        self.params = params
        self.compute = compute
        self.display_options = display_options or []

    def __repr__(self):
        return (f"[{CONFIDENCE.get(self.confidence, '?')}]"
                f"[{'✓' if self.code_verified else '○'}] "
                f"{self.name}: {self.display}")


class EquationModule(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...
    @property
    @abstractmethod
    def display_name(self) -> str: ...
    @property
    @abstractmethod
    def version(self) -> str: ...
    @property
    @abstractmethod
    def description(self) -> str: ...
    @property
    @abstractmethod
    def confidence_floor(self) -> str: ...
    @abstractmethod
    def formulary(self) -> List[Equation]: ...
    @abstractmethod
    def run(self, equation_name: str, params: Dict[str, Any]) -> Dict[str, Any]: ...
    @abstractmethod
    def viewer_data(self, equation_name: str, params: Dict[str, Any],
                    display_mode: str) -> Dict[str, Any]: ...

    def shell_commands(self) -> Dict[str, Any]:
        return {}

    def summary(self) -> str:
        lines = [f"Module: {self.display_name}", f"Version: {self.version}",
                 f"Confidence floor: {self.confidence_floor}",
                 f"Equations: {len(self.formulary())}"]
        for eq in self.formulary():
            lines.append(f"  {eq}")
        return "\n".join(lines)
