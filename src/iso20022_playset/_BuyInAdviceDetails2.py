# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection102
from . import BuyInDeferral1Code
from . import BuyInState1Code
from . import DateAndDateTime2Choice
from . import FinancialInstrumentQuantity1Choice
from . import RateAndAmountFormat39Choice
from . import References31
from . import SecurityIdentification19

class BuyInAdviceDetails2(base_types._BaseFieldType):

	__slots__ = ["_BuyInDfrrl", "_BuyInPric", "_BuyInStat", "_BuyInSttlmDt", "_CshCompstnAmt", "_FinInstrmId", "_Qty", "_Ref"]
	@property
	def BuyInDfrrl(self):
		return self._BuyInDfrrl

	@BuyInDfrrl.setter
	def BuyInDfrrl(self, value):
		self._BuyInDfrrl = value if value is not None else base_types.UninitialisedField(self, 'BuyInDfrrl', BuyInDeferral1Code, False)

	@BuyInDfrrl.deleter
	def BuyInDfrrl(self):
		del self._BuyInDfrrl
		self._BuyInDfrrl = base_types.UninitialisedField(self, 'BuyInDfrrl', BuyInDeferral1Code, False)

	@property
	def BuyInPric(self):
		return self._BuyInPric

	@BuyInPric.setter
	def BuyInPric(self, value):
		self._BuyInPric = value if value is not None else base_types.UninitialisedField(self, 'BuyInPric', RateAndAmountFormat39Choice, False)

	@BuyInPric.deleter
	def BuyInPric(self):
		del self._BuyInPric
		self._BuyInPric = base_types.UninitialisedField(self, 'BuyInPric', RateAndAmountFormat39Choice, False)

	@property
	def BuyInStat(self):
		return self._BuyInStat

	@BuyInStat.setter
	def BuyInStat(self, value):
		self._BuyInStat = value if value is not None else base_types.UninitialisedField(self, 'BuyInStat', BuyInState1Code, False)

	@BuyInStat.deleter
	def BuyInStat(self):
		del self._BuyInStat
		self._BuyInStat = base_types.UninitialisedField(self, 'BuyInStat', BuyInState1Code, False)

	@property
	def BuyInSttlmDt(self):
		return self._BuyInSttlmDt

	@BuyInSttlmDt.setter
	def BuyInSttlmDt(self, value):
		self._BuyInSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'BuyInSttlmDt', DateAndDateTime2Choice, False)

	@BuyInSttlmDt.deleter
	def BuyInSttlmDt(self):
		del self._BuyInSttlmDt
		self._BuyInSttlmDt = base_types.UninitialisedField(self, 'BuyInSttlmDt', DateAndDateTime2Choice, False)

	@property
	def CshCompstnAmt(self):
		return self._CshCompstnAmt

	@CshCompstnAmt.setter
	def CshCompstnAmt(self, value):
		self._CshCompstnAmt = value if value is not None else base_types.UninitialisedField(self, 'CshCompstnAmt', AmountAndDirection102, False)

	@CshCompstnAmt.deleter
	def CshCompstnAmt(self):
		del self._CshCompstnAmt
		self._CshCompstnAmt = base_types.UninitialisedField(self, 'CshCompstnAmt', AmountAndDirection102, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References31, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References31, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyInDfrrl', type=BuyInDeferral1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInPric', type=RateAndAmountFormat39Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInStat', type=BuyInState1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCompstnAmt', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References31, min=1, max=1, mutex_group=None, array=False),
	))