# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity33Choice
from . import ISODate
from . import InstructionProcessingStatus56Choice
from . import Max15Text
from . import Max350Text
from . import Max3NumericText
from . import Max50Text
from . import PriceFormat74Choice
from . import ProtectTransactionType2Code

class OptionInstructionDetails11(base_types._BaseFieldType):

	__slots__ = ["_BidPric", "_CondlQty", "_CoverPrtctDt", "_CstmrRef", "_InstrDt", "_InstrId", "_InstrNrrtv", "_InstrQty", "_InstrSeqNb", "_InstrSts", "_PrtctDt", "_PrtctInd"]
	@property
	def BidPric(self):
		return self._BidPric

	@BidPric.setter
	def BidPric(self, value):
		self._BidPric = value if value is not None else base_types.UninitialisedField(self, 'BidPric', PriceFormat74Choice, False)

	@BidPric.deleter
	def BidPric(self):
		del self._BidPric
		self._BidPric = base_types.UninitialisedField(self, 'BidPric', PriceFormat74Choice, False)

	@property
	def CondlQty(self):
		return self._CondlQty

	@CondlQty.setter
	def CondlQty(self, value):
		self._CondlQty = value if value is not None else base_types.UninitialisedField(self, 'CondlQty', FinancialInstrumentQuantity33Choice, False)

	@CondlQty.deleter
	def CondlQty(self):
		del self._CondlQty
		self._CondlQty = base_types.UninitialisedField(self, 'CondlQty', FinancialInstrumentQuantity33Choice, False)

	@property
	def CoverPrtctDt(self):
		return self._CoverPrtctDt

	@CoverPrtctDt.setter
	def CoverPrtctDt(self, value):
		self._CoverPrtctDt = value if value is not None else base_types.UninitialisedField(self, 'CoverPrtctDt', ISODate, False)

	@CoverPrtctDt.deleter
	def CoverPrtctDt(self):
		del self._CoverPrtctDt
		self._CoverPrtctDt = base_types.UninitialisedField(self, 'CoverPrtctDt', ISODate, False)

	@property
	def CstmrRef(self):
		return self._CstmrRef

	@CstmrRef.setter
	def CstmrRef(self, value):
		self._CstmrRef = value if value is not None else base_types.UninitialisedField(self, 'CstmrRef', Max50Text, False)

	@CstmrRef.deleter
	def CstmrRef(self):
		del self._CstmrRef
		self._CstmrRef = base_types.UninitialisedField(self, 'CstmrRef', Max50Text, False)

	@property
	def InstrDt(self):
		return self._InstrDt

	@InstrDt.setter
	def InstrDt(self, value):
		self._InstrDt = value if value is not None else base_types.UninitialisedField(self, 'InstrDt', ISODate, False)

	@InstrDt.deleter
	def InstrDt(self):
		del self._InstrDt
		self._InstrDt = base_types.UninitialisedField(self, 'InstrDt', ISODate, False)

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if value is not None else base_types.UninitialisedField(self, 'InstrId', Max15Text, False)

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = base_types.UninitialisedField(self, 'InstrId', Max15Text, False)

	@property
	def InstrNrrtv(self):
		return self._InstrNrrtv

	@InstrNrrtv.setter
	def InstrNrrtv(self, value):
		self._InstrNrrtv = value if value is not None else base_types.UninitialisedField(self, 'InstrNrrtv', Max350Text, False)

	@InstrNrrtv.deleter
	def InstrNrrtv(self):
		del self._InstrNrrtv
		self._InstrNrrtv = base_types.UninitialisedField(self, 'InstrNrrtv', Max350Text, False)

	@property
	def InstrQty(self):
		return self._InstrQty

	@InstrQty.setter
	def InstrQty(self, value):
		self._InstrQty = value if value is not None else base_types.UninitialisedField(self, 'InstrQty', FinancialInstrumentQuantity33Choice, False)

	@InstrQty.deleter
	def InstrQty(self):
		del self._InstrQty
		self._InstrQty = base_types.UninitialisedField(self, 'InstrQty', FinancialInstrumentQuantity33Choice, False)

	@property
	def InstrSeqNb(self):
		return self._InstrSeqNb

	@InstrSeqNb.setter
	def InstrSeqNb(self, value):
		self._InstrSeqNb = value if value is not None else base_types.UninitialisedField(self, 'InstrSeqNb', Max3NumericText, False)

	@InstrSeqNb.deleter
	def InstrSeqNb(self):
		del self._InstrSeqNb
		self._InstrSeqNb = base_types.UninitialisedField(self, 'InstrSeqNb', Max3NumericText, False)

	@property
	def InstrSts(self):
		return self._InstrSts

	@InstrSts.setter
	def InstrSts(self, value):
		self._InstrSts = value if value is not None else base_types.UninitialisedField(self, 'InstrSts', InstructionProcessingStatus56Choice, False)

	@InstrSts.deleter
	def InstrSts(self):
		del self._InstrSts
		self._InstrSts = base_types.UninitialisedField(self, 'InstrSts', InstructionProcessingStatus56Choice, False)

	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if value is not None else base_types.UninitialisedField(self, 'PrtctDt', ISODate, False)

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = base_types.UninitialisedField(self, 'PrtctDt', ISODate, False)

	@property
	def PrtctInd(self):
		return self._PrtctInd

	@PrtctInd.setter
	def PrtctInd(self, value):
		self._PrtctInd = value if value is not None else base_types.UninitialisedField(self, 'PrtctInd', ProtectTransactionType2Code, False)

	@PrtctInd.deleter
	def PrtctInd(self):
		del self._PrtctInd
		self._PrtctInd = base_types.UninitialisedField(self, 'PrtctInd', ProtectTransactionType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BidPric', type=PriceFormat74Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CondlQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoverPrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrRef', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrId', type=Max15Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrNrrtv', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrSeqNb', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrSts', type=InstructionProcessingStatus56Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctInd', type=ProtectTransactionType2Code, min=0, max=1, mutex_group=None, array=False),
	))