import base_types
import RateAndAmountFormat39Choice
import DateAndDateTime2Choice
import BuyInDeferral1Code
import FinancialInstrumentQuantity1Choice
import AmountAndDirection102
import SecurityIdentification19
import BuyInState1Code
import References31

class BuyInAdviceDetails2(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_Qty", "_BuyInStat", "_Ref", "_BuyInSttlmDt", "_CshCompstnAmt", "_BuyInPric", "_BuyInDfrrl"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def BuyInStat(self):
		return self._BuyInStat

	@BuyInStat.setter
	def BuyInStat(self, value):
		self._BuyInStat = value if type(value) != auto else self.make_default("BuyInStat")

	@BuyInStat.deleter
	def BuyInStat(self):
		del self._BuyInStat
		self._BuyInStat = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def BuyInSttlmDt(self):
		return self._BuyInSttlmDt

	@BuyInSttlmDt.setter
	def BuyInSttlmDt(self, value):
		self._BuyInSttlmDt = value if type(value) != auto else self.make_default("BuyInSttlmDt")

	@BuyInSttlmDt.deleter
	def BuyInSttlmDt(self):
		del self._BuyInSttlmDt
		self._BuyInSttlmDt = None

	@property
	def CshCompstnAmt(self):
		return self._CshCompstnAmt

	@CshCompstnAmt.setter
	def CshCompstnAmt(self, value):
		self._CshCompstnAmt = value if type(value) != auto else self.make_default("CshCompstnAmt")

	@CshCompstnAmt.deleter
	def CshCompstnAmt(self):
		del self._CshCompstnAmt
		self._CshCompstnAmt = None

	@property
	def BuyInPric(self):
		return self._BuyInPric

	@BuyInPric.setter
	def BuyInPric(self, value):
		self._BuyInPric = value if type(value) != auto else self.make_default("BuyInPric")

	@BuyInPric.deleter
	def BuyInPric(self):
		del self._BuyInPric
		self._BuyInPric = None

	@property
	def BuyInDfrrl(self):
		return self._BuyInDfrrl

	@BuyInDfrrl.setter
	def BuyInDfrrl(self, value):
		self._BuyInDfrrl = value if type(value) != auto else self.make_default("BuyInDfrrl")

	@BuyInDfrrl.deleter
	def BuyInDfrrl(self):
		del self._BuyInDfrrl
		self._BuyInDfrrl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInStat', type=BuyInState1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCompstnAmt', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInPric', type=RateAndAmountFormat39Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInDfrrl', type=BuyInDeferral1Code, min=1, max=1, mutex_group=None, array=False),
	))

