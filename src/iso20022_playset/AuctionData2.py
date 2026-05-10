from . import base_types
from .SecuritiesTransactionPrice21Choice import SecuritiesTransactionPrice21Choice
from .FinancialInstrumentQuantity25Choice import FinancialInstrumentQuantity25Choice
from .Max50Text import Max50Text

class AuctionData2(base_types._BaseFieldType):

	__slots__ = ["_IndctvAuctnVol", "_TradgPhs", "_IndctvAuctnPric"]
	@property
	def IndctvAuctnVol(self):
		return self._IndctvAuctnVol

	@IndctvAuctnVol.setter
	def IndctvAuctnVol(self, value):
		self._IndctvAuctnVol = value if type(value) != base_types.auto else self.make_default("IndctvAuctnVol")

	@IndctvAuctnVol.deleter
	def IndctvAuctnVol(self):
		del self._IndctvAuctnVol
		self._IndctvAuctnVol = None

	@property
	def TradgPhs(self):
		return self._TradgPhs

	@TradgPhs.setter
	def TradgPhs(self, value):
		self._TradgPhs = value if type(value) != base_types.auto else self.make_default("TradgPhs")

	@TradgPhs.deleter
	def TradgPhs(self):
		del self._TradgPhs
		self._TradgPhs = None

	@property
	def IndctvAuctnPric(self):
		return self._IndctvAuctnPric

	@IndctvAuctnPric.setter
	def IndctvAuctnPric(self, value):
		self._IndctvAuctnPric = value if type(value) != base_types.auto else self.make_default("IndctvAuctnPric")

	@IndctvAuctnPric.deleter
	def IndctvAuctnPric(self):
		del self._IndctvAuctnPric
		self._IndctvAuctnPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndctvAuctnVol', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPhs', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndctvAuctnPric', type=SecuritiesTransactionPrice21Choice, min=0, max=1, mutex_group=None, array=False),
	))

