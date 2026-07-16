# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity25Choice
from . import Max50Text
from . import Max52Text
from . import PassiveOrAgressiveType1Code
from . import SecuritiesTransactionPrice4Choice

class TransactionData3(base_types._BaseFieldType):

	__slots__ = ["_PssvOrAggrssvInd", "_StrtgyLkdOrdrId", "_TraddQty", "_TxId", "_TxPric"]
	@property
	def PssvOrAggrssvInd(self):
		return self._PssvOrAggrssvInd

	@PssvOrAggrssvInd.setter
	def PssvOrAggrssvInd(self, value):
		self._PssvOrAggrssvInd = value if value is not None else base_types.UninitialisedField(self, 'PssvOrAggrssvInd', PassiveOrAgressiveType1Code, False)

	@PssvOrAggrssvInd.deleter
	def PssvOrAggrssvInd(self):
		del self._PssvOrAggrssvInd
		self._PssvOrAggrssvInd = base_types.UninitialisedField(self, 'PssvOrAggrssvInd', PassiveOrAgressiveType1Code, False)

	@property
	def StrtgyLkdOrdrId(self):
		return self._StrtgyLkdOrdrId

	@StrtgyLkdOrdrId.setter
	def StrtgyLkdOrdrId(self, value):
		self._StrtgyLkdOrdrId = value if value is not None else base_types.UninitialisedField(self, 'StrtgyLkdOrdrId', Max50Text, False)

	@StrtgyLkdOrdrId.deleter
	def StrtgyLkdOrdrId(self):
		del self._StrtgyLkdOrdrId
		self._StrtgyLkdOrdrId = base_types.UninitialisedField(self, 'StrtgyLkdOrdrId', Max50Text, False)

	@property
	def TraddQty(self):
		return self._TraddQty

	@TraddQty.setter
	def TraddQty(self, value):
		self._TraddQty = value if value is not None else base_types.UninitialisedField(self, 'TraddQty', FinancialInstrumentQuantity25Choice, False)

	@TraddQty.deleter
	def TraddQty(self):
		del self._TraddQty
		self._TraddQty = base_types.UninitialisedField(self, 'TraddQty', FinancialInstrumentQuantity25Choice, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max52Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max52Text, False)

	@property
	def TxPric(self):
		return self._TxPric

	@TxPric.setter
	def TxPric(self, value):
		self._TxPric = value if value is not None else base_types.UninitialisedField(self, 'TxPric', SecuritiesTransactionPrice4Choice, False)

	@TxPric.deleter
	def TxPric(self):
		del self._TxPric
		self._TxPric = base_types.UninitialisedField(self, 'TxPric', SecuritiesTransactionPrice4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PssvOrAggrssvInd', type=PassiveOrAgressiveType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtgyLkdOrdrId', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TraddQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxPric', type=SecuritiesTransactionPrice4Choice, min=0, max=1, mutex_group=None, array=False),
	))