# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import SettlementTotalData1

class SettlementFailsCurrency2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Data"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', SettlementTotalData1, False)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', SettlementTotalData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
	))