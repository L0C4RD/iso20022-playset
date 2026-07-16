# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max6NumericText

class TotalNumber2(base_types._BaseFieldType):

	__slots__ = ["_CurInstrNb", "_TtlOfLkdInstrs"]
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
	def TtlOfLkdInstrs(self):
		return self._TtlOfLkdInstrs

	@TtlOfLkdInstrs.setter
	def TtlOfLkdInstrs(self, value):
		self._TtlOfLkdInstrs = value if value is not None else base_types.UninitialisedField(self, 'TtlOfLkdInstrs', Max6NumericText, False)

	@TtlOfLkdInstrs.deleter
	def TtlOfLkdInstrs(self):
		del self._TtlOfLkdInstrs
		self._TtlOfLkdInstrs = base_types.UninitialisedField(self, 'TtlOfLkdInstrs', Max6NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurInstrNb', type=Max6NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOfLkdInstrs', type=Max6NumericText, min=1, max=1, mutex_group=None, array=False),
	))