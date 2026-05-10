from . import base_types
from .FinancialInstrumentQuantity25Choice import FinancialInstrumentQuantity25Choice
from .PassiveOrAgressiveType1Code import PassiveOrAgressiveType1Code
from .SecuritiesTransactionPrice4Choice import SecuritiesTransactionPrice4Choice
from .Max50Text import Max50Text
from .Max52Text import Max52Text

class TransactionData3(base_types._BaseFieldType):

	__slots__ = ["_TraddQty", "_StrtgyLkdOrdrId", "_TxId", "_PssvOrAggrssvInd", "_TxPric"]
	@property
	def TraddQty(self):
		return self._TraddQty

	@TraddQty.setter
	def TraddQty(self, value):
		self._TraddQty = value if type(value) != base_types.auto else self.make_default("TraddQty")

	@TraddQty.deleter
	def TraddQty(self):
		del self._TraddQty
		self._TraddQty = None

	@property
	def StrtgyLkdOrdrId(self):
		return self._StrtgyLkdOrdrId

	@StrtgyLkdOrdrId.setter
	def StrtgyLkdOrdrId(self, value):
		self._StrtgyLkdOrdrId = value if type(value) != base_types.auto else self.make_default("StrtgyLkdOrdrId")

	@StrtgyLkdOrdrId.deleter
	def StrtgyLkdOrdrId(self):
		del self._StrtgyLkdOrdrId
		self._StrtgyLkdOrdrId = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def PssvOrAggrssvInd(self):
		return self._PssvOrAggrssvInd

	@PssvOrAggrssvInd.setter
	def PssvOrAggrssvInd(self, value):
		self._PssvOrAggrssvInd = value if type(value) != base_types.auto else self.make_default("PssvOrAggrssvInd")

	@PssvOrAggrssvInd.deleter
	def PssvOrAggrssvInd(self):
		del self._PssvOrAggrssvInd
		self._PssvOrAggrssvInd = None

	@property
	def TxPric(self):
		return self._TxPric

	@TxPric.setter
	def TxPric(self, value):
		self._TxPric = value if type(value) != base_types.auto else self.make_default("TxPric")

	@TxPric.deleter
	def TxPric(self):
		del self._TxPric
		self._TxPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TraddQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtgyLkdOrdrId', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssvOrAggrssvInd', type=PassiveOrAgressiveType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxPric', type=SecuritiesTransactionPrice4Choice, min=0, max=1, mutex_group=None, array=False),
	))

