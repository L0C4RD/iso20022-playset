# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max6NumericText import Max6NumericText
from ._TotalNumber2 import TotalNumber2

class NumberCount2Choice(base_types._BaseFieldType):

	__slots__ = ["_CurInstrNb", "_TtlNb"]
	@property
	def CurInstrNb(self):
		return self._CurInstrNb

	@CurInstrNb.setter
	def CurInstrNb(self, value):
		self._CurInstrNb = value if type(value) != base_types.auto else self.make_default("CurInstrNb")

	@CurInstrNb.deleter
	def CurInstrNb(self):
		del self._CurInstrNb
		self._CurInstrNb = None

	@property
	def TtlNb(self):
		return self._TtlNb

	@TtlNb.setter
	def TtlNb(self, value):
		self._TtlNb = value if type(value) != base_types.auto else self.make_default("TtlNb")

	@TtlNb.deleter
	def TtlNb(self):
		del self._TtlNb
		self._TtlNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurInstrNb', type=Max6NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlNb', type=TotalNumber2, min=0, max=1, mutex_group=1, array=False),
	))