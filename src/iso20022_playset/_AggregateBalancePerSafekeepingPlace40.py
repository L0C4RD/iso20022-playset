# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBalanceInformation23
from . import Balance22
from . import BalanceAmounts5
from . import ExposureType24Choice
from . import ForeignExchangeTerms35
from . import MarketIdentification4Choice
from . import Number
from . import Pledgee4
from . import PriceInformation22
from . import QuantityBreakdown70
from . import RestrictedFINXMax350Text
from . import SafeKeepingPlace4
from . import SubBalanceInformation23

class AggregateBalancePerSafekeepingPlace40(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyAmts", "_AddtlBalBrkdwn", "_AggtBal", "_AltrnRptgCcyAmts", "_BalBrkdwn", "_DaysAcrd", "_FXDtls", "_HldgAddtlDtls", "_InstrmCcyAmts", "_PlcOfListg", "_Pldgee", "_PricDtls", "_QtyBrkdwn", "_SfkpgPlc", "_XpsrTp"]
	@property
	def AcctBaseCcyAmts(self):
		return self._AcctBaseCcyAmts

	@AcctBaseCcyAmts.setter
	def AcctBaseCcyAmts(self, value):
		self._AcctBaseCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts5, False)

	@AcctBaseCcyAmts.deleter
	def AcctBaseCcyAmts(self):
		del self._AcctBaseCcyAmts
		self._AcctBaseCcyAmts = base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts5, False)

	@property
	def AddtlBalBrkdwn(self):
		return self._AddtlBalBrkdwn

	@AddtlBalBrkdwn.setter
	def AddtlBalBrkdwn(self, value):
		self._AddtlBalBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'AddtlBalBrkdwn', AdditionalBalanceInformation23, True)

	@AddtlBalBrkdwn.deleter
	def AddtlBalBrkdwn(self):
		del self._AddtlBalBrkdwn
		self._AddtlBalBrkdwn = base_types.UninitialisedField(self, 'AddtlBalBrkdwn', AdditionalBalanceInformation23, True)

	@property
	def AggtBal(self):
		return self._AggtBal

	@AggtBal.setter
	def AggtBal(self, value):
		self._AggtBal = value if value is not None else base_types.UninitialisedField(self, 'AggtBal', Balance22, False)

	@AggtBal.deleter
	def AggtBal(self):
		del self._AggtBal
		self._AggtBal = base_types.UninitialisedField(self, 'AggtBal', Balance22, False)

	@property
	def AltrnRptgCcyAmts(self):
		return self._AltrnRptgCcyAmts

	@AltrnRptgCcyAmts.setter
	def AltrnRptgCcyAmts(self, value):
		self._AltrnRptgCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts5, False)

	@AltrnRptgCcyAmts.deleter
	def AltrnRptgCcyAmts(self):
		del self._AltrnRptgCcyAmts
		self._AltrnRptgCcyAmts = base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts5, False)

	@property
	def BalBrkdwn(self):
		return self._BalBrkdwn

	@BalBrkdwn.setter
	def BalBrkdwn(self, value):
		self._BalBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceInformation23, True)

	@BalBrkdwn.deleter
	def BalBrkdwn(self):
		del self._BalBrkdwn
		self._BalBrkdwn = base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceInformation23, True)

	@property
	def DaysAcrd(self):
		return self._DaysAcrd

	@DaysAcrd.setter
	def DaysAcrd(self, value):
		self._DaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'DaysAcrd', Number, False)

	@DaysAcrd.deleter
	def DaysAcrd(self):
		del self._DaysAcrd
		self._DaysAcrd = base_types.UninitialisedField(self, 'DaysAcrd', Number, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms35, True)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms35, True)

	@property
	def HldgAddtlDtls(self):
		return self._HldgAddtlDtls

	@HldgAddtlDtls.setter
	def HldgAddtlDtls(self, value):
		self._HldgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'HldgAddtlDtls', RestrictedFINXMax350Text, False)

	@HldgAddtlDtls.deleter
	def HldgAddtlDtls(self):
		del self._HldgAddtlDtls
		self._HldgAddtlDtls = base_types.UninitialisedField(self, 'HldgAddtlDtls', RestrictedFINXMax350Text, False)

	@property
	def InstrmCcyAmts(self):
		return self._InstrmCcyAmts

	@InstrmCcyAmts.setter
	def InstrmCcyAmts(self, value):
		self._InstrmCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts5, False)

	@InstrmCcyAmts.deleter
	def InstrmCcyAmts(self):
		del self._InstrmCcyAmts
		self._InstrmCcyAmts = base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts5, False)

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if value is not None else base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification4Choice, False)

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification4Choice, False)

	@property
	def Pldgee(self):
		return self._Pldgee

	@Pldgee.setter
	def Pldgee(self, value):
		self._Pldgee = value if value is not None else base_types.UninitialisedField(self, 'Pldgee', Pledgee4, False)

	@Pldgee.deleter
	def Pldgee(self):
		del self._Pldgee
		self._Pldgee = base_types.UninitialisedField(self, 'Pldgee', Pledgee4, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', PriceInformation22, True)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', PriceInformation22, True)

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown70, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown70, True)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace4, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace4, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType24Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType24Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwn', type=AdditionalBalanceInformation23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AggtBal', type=Balance22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnRptgCcyAmts', type=BalanceAmounts5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceInformation23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms35, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HldgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pldgee', type=Pledgee4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation22, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown70, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType24Choice, min=0, max=1, mutex_group=None, array=False),
	))