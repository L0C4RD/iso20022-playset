from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._SettlementTotalData1 import SettlementTotalData1

class SettlementFailsCurrency2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Data"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != base_types.auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
	))

