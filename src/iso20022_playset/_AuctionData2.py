# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity25Choice
from . import Max50Text
from . import SecuritiesTransactionPrice21Choice

class AuctionData2(base_types._BaseFieldType):

	__slots__ = ["_IndctvAuctnPric", "_IndctvAuctnVol", "_TradgPhs"]
	@property
	def IndctvAuctnPric(self):
		return self._IndctvAuctnPric

	@IndctvAuctnPric.setter
	def IndctvAuctnPric(self, value):
		self._IndctvAuctnPric = value if value is not None else base_types.UninitialisedField(self, 'IndctvAuctnPric', SecuritiesTransactionPrice21Choice, False)

	@IndctvAuctnPric.deleter
	def IndctvAuctnPric(self):
		del self._IndctvAuctnPric
		self._IndctvAuctnPric = base_types.UninitialisedField(self, 'IndctvAuctnPric', SecuritiesTransactionPrice21Choice, False)

	@property
	def IndctvAuctnVol(self):
		return self._IndctvAuctnVol

	@IndctvAuctnVol.setter
	def IndctvAuctnVol(self, value):
		self._IndctvAuctnVol = value if value is not None else base_types.UninitialisedField(self, 'IndctvAuctnVol', FinancialInstrumentQuantity25Choice, False)

	@IndctvAuctnVol.deleter
	def IndctvAuctnVol(self):
		del self._IndctvAuctnVol
		self._IndctvAuctnVol = base_types.UninitialisedField(self, 'IndctvAuctnVol', FinancialInstrumentQuantity25Choice, False)

	@property
	def TradgPhs(self):
		return self._TradgPhs

	@TradgPhs.setter
	def TradgPhs(self, value):
		self._TradgPhs = value if value is not None else base_types.UninitialisedField(self, 'TradgPhs', Max50Text, False)

	@TradgPhs.deleter
	def TradgPhs(self):
		del self._TradgPhs
		self._TradgPhs = base_types.UninitialisedField(self, 'TradgPhs', Max50Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndctvAuctnPric', type=SecuritiesTransactionPrice21Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndctvAuctnVol', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPhs', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))