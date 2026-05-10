from . import base_types
from ._FinancialInstrumentQuantity18Choice import FinancialInstrumentQuantity18Choice
from ._Max35Text import Max35Text
from ._ProceedsQuantityBreakdown1 import ProceedsQuantityBreakdown1
from ._TransferOfProceedsType1Code import TransferOfProceedsType1Code

class RelatedSettlementInstruction2(base_types._BaseFieldType):

	__slots__ = ["_PrcdsQtyBrkdwn", "_RltdSttlmInstrId", "_RltdSttlmQty", "_TrfOfPrcdsTpInd"]
	@property
	def PrcdsQtyBrkdwn(self):
		return self._PrcdsQtyBrkdwn

	@PrcdsQtyBrkdwn.setter
	def PrcdsQtyBrkdwn(self, value):
		self._PrcdsQtyBrkdwn = value if type(value) != base_types.auto else self.make_default("PrcdsQtyBrkdwn")

	@PrcdsQtyBrkdwn.deleter
	def PrcdsQtyBrkdwn(self):
		del self._PrcdsQtyBrkdwn
		self._PrcdsQtyBrkdwn = None

	@property
	def RltdSttlmInstrId(self):
		return self._RltdSttlmInstrId

	@RltdSttlmInstrId.setter
	def RltdSttlmInstrId(self, value):
		self._RltdSttlmInstrId = value if type(value) != base_types.auto else self.make_default("RltdSttlmInstrId")

	@RltdSttlmInstrId.deleter
	def RltdSttlmInstrId(self):
		del self._RltdSttlmInstrId
		self._RltdSttlmInstrId = None

	@property
	def RltdSttlmQty(self):
		return self._RltdSttlmQty

	@RltdSttlmQty.setter
	def RltdSttlmQty(self, value):
		self._RltdSttlmQty = value if type(value) != base_types.auto else self.make_default("RltdSttlmQty")

	@RltdSttlmQty.deleter
	def RltdSttlmQty(self):
		del self._RltdSttlmQty
		self._RltdSttlmQty = None

	@property
	def TrfOfPrcdsTpInd(self):
		return self._TrfOfPrcdsTpInd

	@TrfOfPrcdsTpInd.setter
	def TrfOfPrcdsTpInd(self, value):
		self._TrfOfPrcdsTpInd = value if type(value) != base_types.auto else self.make_default("TrfOfPrcdsTpInd")

	@TrfOfPrcdsTpInd.deleter
	def TrfOfPrcdsTpInd(self):
		del self._TrfOfPrcdsTpInd
		self._TrfOfPrcdsTpInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcdsQtyBrkdwn', type=ProceedsQuantityBreakdown1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfOfPrcdsTpInd', type=TransferOfProceedsType1Code, min=0, max=1, mutex_group=None, array=False),
	))

