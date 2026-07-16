# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max6NumericText
from . import TotalNumber2

class NumberCount2Choice(base_types._BaseFieldType):

	__slots__ = ["_CurInstrNb", "_TtlNb"]
	@property
	def CurInstrNb(self):
		return self._CurInstrNb

	@CurInstrNb.setter
	def CurInstrNb(self, value):
		self._CurInstrNb = value if value is not None else base_types.UninitialisedField(self, 'CurInstrNb', Max6NumericText, False)

	@CurInstrNb.deleter
	def CurInstrNb(self):
		del self._CurInstrNb
		self._CurInstrNb = base_types.UninitialisedField(self, 'CurInstrNb', Max6NumericText, False)

	@property
	def TtlNb(self):
		return self._TtlNb

	@TtlNb.setter
	def TtlNb(self, value):
		self._TtlNb = value if value is not None else base_types.UninitialisedField(self, 'TtlNb', TotalNumber2, False)

	@TtlNb.deleter
	def TtlNb(self):
		del self._TtlNb
		self._TtlNb = base_types.UninitialisedField(self, 'TtlNb', TotalNumber2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurInstrNb', type=Max6NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlNb', type=TotalNumber2, min=0, max=1, mutex_group=1, array=False),
	))