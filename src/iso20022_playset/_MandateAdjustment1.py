# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Frequency37Choice
from . import PercentageRate
from . import TrueFalseIndicator

class MandateAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ctgy", "_DtAdjstmntRuleInd", "_Rate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if value is not None else base_types.UninitialisedField(self, 'Ctgy', Frequency37Choice, False)

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = base_types.UninitialisedField(self, 'Ctgy', Frequency37Choice, False)

	@property
	def DtAdjstmntRuleInd(self):
		return self._DtAdjstmntRuleInd

	@DtAdjstmntRuleInd.setter
	def DtAdjstmntRuleInd(self, value):
		self._DtAdjstmntRuleInd = value if value is not None else base_types.UninitialisedField(self, 'DtAdjstmntRuleInd', TrueFalseIndicator, False)

	@DtAdjstmntRuleInd.deleter
	def DtAdjstmntRuleInd(self):
		del self._DtAdjstmntRuleInd
		self._DtAdjstmntRuleInd = base_types.UninitialisedField(self, 'DtAdjstmntRuleInd', TrueFalseIndicator, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=Frequency37Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAdjstmntRuleInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))