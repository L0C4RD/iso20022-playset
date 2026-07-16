# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeRate3
from . import ISODate
from . import PenaltyAmountBreakdown1
from . import PenaltyFinancialInstrumentIdentification1
from . import PriceRateOrAmount4Choice
from . import TrueFalseIndicator

class PenaltyCalculationRecord1(base_types._BaseFieldType):

	__slots__ = ["_DscntRate", "_Dt", "_FXData", "_FinInstrmAttrbts", "_MssngRefData", "_SubAmtPnltyBrkdwn"]
	@property
	def DscntRate(self):
		return self._DscntRate

	@DscntRate.setter
	def DscntRate(self, value):
		self._DscntRate = value if value is not None else base_types.UninitialisedField(self, 'DscntRate', PriceRateOrAmount4Choice, False)

	@DscntRate.deleter
	def DscntRate(self):
		del self._DscntRate
		self._DscntRate = base_types.UninitialisedField(self, 'DscntRate', PriceRateOrAmount4Choice, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def FXData(self):
		return self._FXData

	@FXData.setter
	def FXData(self, value):
		self._FXData = value if value is not None else base_types.UninitialisedField(self, 'FXData', ForeignExchangeRate3, True)

	@FXData.deleter
	def FXData(self):
		del self._FXData
		self._FXData = base_types.UninitialisedField(self, 'FXData', ForeignExchangeRate3, True)

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', PenaltyFinancialInstrumentIdentification1, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', PenaltyFinancialInstrumentIdentification1, False)

	@property
	def MssngRefData(self):
		return self._MssngRefData

	@MssngRefData.setter
	def MssngRefData(self, value):
		self._MssngRefData = value if value is not None else base_types.UninitialisedField(self, 'MssngRefData', TrueFalseIndicator, False)

	@MssngRefData.deleter
	def MssngRefData(self):
		del self._MssngRefData
		self._MssngRefData = base_types.UninitialisedField(self, 'MssngRefData', TrueFalseIndicator, False)

	@property
	def SubAmtPnltyBrkdwn(self):
		return self._SubAmtPnltyBrkdwn

	@SubAmtPnltyBrkdwn.setter
	def SubAmtPnltyBrkdwn(self, value):
		self._SubAmtPnltyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'SubAmtPnltyBrkdwn', PenaltyAmountBreakdown1, True)

	@SubAmtPnltyBrkdwn.deleter
	def SubAmtPnltyBrkdwn(self):
		del self._SubAmtPnltyBrkdwn
		self._SubAmtPnltyBrkdwn = base_types.UninitialisedField(self, 'SubAmtPnltyBrkdwn', PenaltyAmountBreakdown1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntRate', type=PriceRateOrAmount4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXData', type=ForeignExchangeRate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=PenaltyFinancialInstrumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MssngRefData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAmtPnltyBrkdwn', type=PenaltyAmountBreakdown1, min=0, max=None, mutex_group=None, array=True),
	))