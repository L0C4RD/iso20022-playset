# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Exact1NumericText
from . import ISODate
from . import Number
from . import YesNoIndicator

class LoanContractTranche1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DrtnCd", "_DueDt", "_LastTrchInd", "_TrchNb", "_XpctdDt"]
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
	def DrtnCd(self):
		return self._DrtnCd

	@DrtnCd.setter
	def DrtnCd(self, value):
		self._DrtnCd = value if value is not None else base_types.UninitialisedField(self, 'DrtnCd', Exact1NumericText, False)

	@DrtnCd.deleter
	def DrtnCd(self):
		del self._DrtnCd
		self._DrtnCd = base_types.UninitialisedField(self, 'DrtnCd', Exact1NumericText, False)

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if value is not None else base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@property
	def LastTrchInd(self):
		return self._LastTrchInd

	@LastTrchInd.setter
	def LastTrchInd(self, value):
		self._LastTrchInd = value if value is not None else base_types.UninitialisedField(self, 'LastTrchInd', YesNoIndicator, False)

	@LastTrchInd.deleter
	def LastTrchInd(self):
		del self._LastTrchInd
		self._LastTrchInd = base_types.UninitialisedField(self, 'LastTrchInd', YesNoIndicator, False)

	@property
	def TrchNb(self):
		return self._TrchNb

	@TrchNb.setter
	def TrchNb(self, value):
		self._TrchNb = value if value is not None else base_types.UninitialisedField(self, 'TrchNb', Number, False)

	@TrchNb.deleter
	def TrchNb(self):
		del self._TrchNb
		self._TrchNb = base_types.UninitialisedField(self, 'TrchNb', Number, False)

	@property
	def XpctdDt(self):
		return self._XpctdDt

	@XpctdDt.setter
	def XpctdDt(self, value):
		self._XpctdDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	@XpctdDt.deleter
	def XpctdDt(self):
		del self._XpctdDt
		self._XpctdDt = base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrtnCd', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTrchInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrchNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))