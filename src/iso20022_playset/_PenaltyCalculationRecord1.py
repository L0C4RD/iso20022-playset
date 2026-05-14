# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeRate3 import ForeignExchangeRate3
from ._ISODate import ISODate
from ._PenaltyAmountBreakdown1 import PenaltyAmountBreakdown1
from ._PenaltyFinancialInstrumentIdentification1 import PenaltyFinancialInstrumentIdentification1
from ._PriceRateOrAmount4Choice import PriceRateOrAmount4Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class PenaltyCalculationRecord1(base_types._BaseFieldType):

	__slots__ = ["_DscntRate", "_Dt", "_FXData", "_FinInstrmAttrbts", "_MssngRefData", "_SubAmtPnltyBrkdwn"]
	@property
	def DscntRate(self):
		return self._DscntRate

	@DscntRate.setter
	def DscntRate(self, value):
		self._DscntRate = value if type(value) != base_types.auto else self.make_default("DscntRate")

	@DscntRate.deleter
	def DscntRate(self):
		del self._DscntRate
		self._DscntRate = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def FXData(self):
		return self._FXData

	@FXData.setter
	def FXData(self, value):
		self._FXData = value if type(value) != base_types.auto else self.make_default("FXData")

	@FXData.deleter
	def FXData(self):
		del self._FXData
		self._FXData = None

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("FinInstrmAttrbts")

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = None

	@property
	def MssngRefData(self):
		return self._MssngRefData

	@MssngRefData.setter
	def MssngRefData(self, value):
		self._MssngRefData = value if type(value) != base_types.auto else self.make_default("MssngRefData")

	@MssngRefData.deleter
	def MssngRefData(self):
		del self._MssngRefData
		self._MssngRefData = None

	@property
	def SubAmtPnltyBrkdwn(self):
		return self._SubAmtPnltyBrkdwn

	@SubAmtPnltyBrkdwn.setter
	def SubAmtPnltyBrkdwn(self, value):
		self._SubAmtPnltyBrkdwn = value if type(value) != base_types.auto else self.make_default("SubAmtPnltyBrkdwn")

	@SubAmtPnltyBrkdwn.deleter
	def SubAmtPnltyBrkdwn(self):
		del self._SubAmtPnltyBrkdwn
		self._SubAmtPnltyBrkdwn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntRate', type=PriceRateOrAmount4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXData', type=ForeignExchangeRate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=PenaltyFinancialInstrumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MssngRefData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAmtPnltyBrkdwn', type=PenaltyAmountBreakdown1, min=0, max=None, mutex_group=None, array=True),
	))