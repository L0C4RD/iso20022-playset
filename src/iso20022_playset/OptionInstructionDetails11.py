from . import base_types
from .ProtectTransactionType2Code import ProtectTransactionType2Code
from .ISODate import ISODate
from .Max50Text import Max50Text
from .Max350Text import Max350Text
from .Max15Text import Max15Text
from .Max3NumericText import Max3NumericText
from .FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from .InstructionProcessingStatus56Choice import InstructionProcessingStatus56Choice
from .PriceFormat74Choice import PriceFormat74Choice

class OptionInstructionDetails11(base_types._BaseFieldType):

	__slots__ = ["_CoverPrtctDt", "_InstrId", "_InstrSeqNb", "_PrtctDt", "_InstrSts", "_PrtctInd", "_CondlQty", "_InstrQty", "_InstrDt", "_CstmrRef", "_InstrNrrtv", "_BidPric"]
	@property
	def CoverPrtctDt(self):
		return self._CoverPrtctDt

	@CoverPrtctDt.setter
	def CoverPrtctDt(self, value):
		self._CoverPrtctDt = value if type(value) != auto else self.make_default("CoverPrtctDt")

	@CoverPrtctDt.deleter
	def CoverPrtctDt(self):
		del self._CoverPrtctDt
		self._CoverPrtctDt = None

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if type(value) != auto else self.make_default("InstrId")

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = None

	@property
	def InstrSeqNb(self):
		return self._InstrSeqNb

	@InstrSeqNb.setter
	def InstrSeqNb(self, value):
		self._InstrSeqNb = value if type(value) != auto else self.make_default("InstrSeqNb")

	@InstrSeqNb.deleter
	def InstrSeqNb(self):
		del self._InstrSeqNb
		self._InstrSeqNb = None

	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if type(value) != auto else self.make_default("PrtctDt")

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = None

	@property
	def InstrSts(self):
		return self._InstrSts

	@InstrSts.setter
	def InstrSts(self, value):
		self._InstrSts = value if type(value) != auto else self.make_default("InstrSts")

	@InstrSts.deleter
	def InstrSts(self):
		del self._InstrSts
		self._InstrSts = None

	@property
	def PrtctInd(self):
		return self._PrtctInd

	@PrtctInd.setter
	def PrtctInd(self, value):
		self._PrtctInd = value if type(value) != auto else self.make_default("PrtctInd")

	@PrtctInd.deleter
	def PrtctInd(self):
		del self._PrtctInd
		self._PrtctInd = None

	@property
	def CondlQty(self):
		return self._CondlQty

	@CondlQty.setter
	def CondlQty(self, value):
		self._CondlQty = value if type(value) != auto else self.make_default("CondlQty")

	@CondlQty.deleter
	def CondlQty(self):
		del self._CondlQty
		self._CondlQty = None

	@property
	def InstrQty(self):
		return self._InstrQty

	@InstrQty.setter
	def InstrQty(self, value):
		self._InstrQty = value if type(value) != auto else self.make_default("InstrQty")

	@InstrQty.deleter
	def InstrQty(self):
		del self._InstrQty
		self._InstrQty = None

	@property
	def InstrDt(self):
		return self._InstrDt

	@InstrDt.setter
	def InstrDt(self, value):
		self._InstrDt = value if type(value) != auto else self.make_default("InstrDt")

	@InstrDt.deleter
	def InstrDt(self):
		del self._InstrDt
		self._InstrDt = None

	@property
	def CstmrRef(self):
		return self._CstmrRef

	@CstmrRef.setter
	def CstmrRef(self, value):
		self._CstmrRef = value if type(value) != auto else self.make_default("CstmrRef")

	@CstmrRef.deleter
	def CstmrRef(self):
		del self._CstmrRef
		self._CstmrRef = None

	@property
	def InstrNrrtv(self):
		return self._InstrNrrtv

	@InstrNrrtv.setter
	def InstrNrrtv(self, value):
		self._InstrNrrtv = value if type(value) != auto else self.make_default("InstrNrrtv")

	@InstrNrrtv.deleter
	def InstrNrrtv(self):
		del self._InstrNrrtv
		self._InstrNrrtv = None

	@property
	def BidPric(self):
		return self._BidPric

	@BidPric.setter
	def BidPric(self, value):
		self._BidPric = value if type(value) != auto else self.make_default("BidPric")

	@BidPric.deleter
	def BidPric(self):
		del self._BidPric
		self._BidPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CoverPrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrId', type=Max15Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrSeqNb', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrSts', type=InstructionProcessingStatus56Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctInd', type=ProtectTransactionType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CondlQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrRef', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrNrrtv', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BidPric', type=PriceFormat74Choice, min=0, max=1, mutex_group=None, array=False),
	))

