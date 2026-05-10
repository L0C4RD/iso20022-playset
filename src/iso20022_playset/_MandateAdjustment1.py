from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Frequency37Choice import Frequency37Choice
from ._PercentageRate import PercentageRate
from ._TrueFalseIndicator import TrueFalseIndicator

class MandateAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ctgy", "_DtAdjstmntRuleInd", "_Rate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if type(value) != base_types.auto else self.make_default("Ctgy")

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = None

	@property
	def DtAdjstmntRuleInd(self):
		return self._DtAdjstmntRuleInd

	@DtAdjstmntRuleInd.setter
	def DtAdjstmntRuleInd(self, value):
		self._DtAdjstmntRuleInd = value if type(value) != base_types.auto else self.make_default("DtAdjstmntRuleInd")

	@DtAdjstmntRuleInd.deleter
	def DtAdjstmntRuleInd(self):
		del self._DtAdjstmntRuleInd
		self._DtAdjstmntRuleInd = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=Frequency37Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAdjstmntRuleInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

