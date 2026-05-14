# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Exact1NumericText import Exact1NumericText
from ._ISODate import ISODate
from ._Number import Number
from ._YesNoIndicator import YesNoIndicator

class LoanContractTranche1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DrtnCd", "_DueDt", "_LastTrchInd", "_TrchNb", "_XpctdDt"]
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
	def DrtnCd(self):
		return self._DrtnCd

	@DrtnCd.setter
	def DrtnCd(self, value):
		self._DrtnCd = value if type(value) != base_types.auto else self.make_default("DrtnCd")

	@DrtnCd.deleter
	def DrtnCd(self):
		del self._DrtnCd
		self._DrtnCd = None

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if type(value) != base_types.auto else self.make_default("DueDt")

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = None

	@property
	def LastTrchInd(self):
		return self._LastTrchInd

	@LastTrchInd.setter
	def LastTrchInd(self, value):
		self._LastTrchInd = value if type(value) != base_types.auto else self.make_default("LastTrchInd")

	@LastTrchInd.deleter
	def LastTrchInd(self):
		del self._LastTrchInd
		self._LastTrchInd = None

	@property
	def TrchNb(self):
		return self._TrchNb

	@TrchNb.setter
	def TrchNb(self, value):
		self._TrchNb = value if type(value) != base_types.auto else self.make_default("TrchNb")

	@TrchNb.deleter
	def TrchNb(self):
		del self._TrchNb
		self._TrchNb = None

	@property
	def XpctdDt(self):
		return self._XpctdDt

	@XpctdDt.setter
	def XpctdDt(self, value):
		self._XpctdDt = value if type(value) != base_types.auto else self.make_default("XpctdDt")

	@XpctdDt.deleter
	def XpctdDt(self):
		del self._XpctdDt
		self._XpctdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrtnCd', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTrchInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrchNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))