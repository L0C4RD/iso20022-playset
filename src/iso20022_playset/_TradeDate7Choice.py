# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime1Choice
from . import TradingDateCode2Choice

class TradeDate7Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_Val"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTime1Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTime1Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', TradingDateCode2Choice, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', TradingDateCode2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Val', type=TradingDateCode2Choice, min=0, max=1, mutex_group=1, array=False),
	))