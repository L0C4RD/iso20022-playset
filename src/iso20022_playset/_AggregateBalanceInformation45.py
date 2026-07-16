# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBalanceInformation22
from . import AggregateBalancePerSafekeepingPlace42
from . import Balance17
from . import BalanceAmounts1
from . import CorporateActionOption5Code
from . import DerivativeBasicAttributes1
from . import FinancialInstrument21
from . import FinancialInstrumentAttributes111
from . import ForeignExchangeTerms34
from . import Max350Text
from . import Number
from . import PriceInformation29
from . import QuantityBreakdown58
from . import SafeKeepingPlace5
from . import SecurityIdentification19
from . import SubBalanceInformation22
from . import SupplementaryData1

class AggregateBalanceInformation45(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyAmts", "_AddtlBalBrkdwn", "_AddtlDerivAttrbts", "_AggtBal", "_AltrnRptgCcyAmts", "_BalAtSfkpgPlc", "_BalBrkdwn", "_CorpActnOptnTp", "_DaysAcrd", "_FXDtls", "_FinInstrmAttrbts", "_FinInstrmId", "_HldgAddtlDtls", "_InstrmCcyAmts", "_InvstmtFndsFinInstrmAttrbts", "_PricDtls", "_QtyBrkdwn", "_SfkpgPlc", "_SplmtryData"]
	@property
	def AcctBaseCcyAmts(self):
		return self._AcctBaseCcyAmts

	@AcctBaseCcyAmts.setter
	def AcctBaseCcyAmts(self, value):
		self._AcctBaseCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts1, False)

	@AcctBaseCcyAmts.deleter
	def AcctBaseCcyAmts(self):
		del self._AcctBaseCcyAmts
		self._AcctBaseCcyAmts = base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts1, False)

	@property
	def AddtlBalBrkdwn(self):
		return self._AddtlBalBrkdwn

	@AddtlBalBrkdwn.setter
	def AddtlBalBrkdwn(self, value):
		self._AddtlBalBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'AddtlBalBrkdwn', AdditionalBalanceInformation22, True)

	@AddtlBalBrkdwn.deleter
	def AddtlBalBrkdwn(self):
		del self._AddtlBalBrkdwn
		self._AddtlBalBrkdwn = base_types.UninitialisedField(self, 'AddtlBalBrkdwn', AdditionalBalanceInformation22, True)

	@property
	def AddtlDerivAttrbts(self):
		return self._AddtlDerivAttrbts

	@AddtlDerivAttrbts.setter
	def AddtlDerivAttrbts(self, value):
		self._AddtlDerivAttrbts = value if value is not None else base_types.UninitialisedField(self, 'AddtlDerivAttrbts', DerivativeBasicAttributes1, False)

	@AddtlDerivAttrbts.deleter
	def AddtlDerivAttrbts(self):
		del self._AddtlDerivAttrbts
		self._AddtlDerivAttrbts = base_types.UninitialisedField(self, 'AddtlDerivAttrbts', DerivativeBasicAttributes1, False)

	@property
	def AggtBal(self):
		return self._AggtBal

	@AggtBal.setter
	def AggtBal(self, value):
		self._AggtBal = value if value is not None else base_types.UninitialisedField(self, 'AggtBal', Balance17, False)

	@AggtBal.deleter
	def AggtBal(self):
		del self._AggtBal
		self._AggtBal = base_types.UninitialisedField(self, 'AggtBal', Balance17, False)

	@property
	def AltrnRptgCcyAmts(self):
		return self._AltrnRptgCcyAmts

	@AltrnRptgCcyAmts.setter
	def AltrnRptgCcyAmts(self, value):
		self._AltrnRptgCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts1, False)

	@AltrnRptgCcyAmts.deleter
	def AltrnRptgCcyAmts(self):
		del self._AltrnRptgCcyAmts
		self._AltrnRptgCcyAmts = base_types.UninitialisedField(self, 'AltrnRptgCcyAmts', BalanceAmounts1, False)

	@property
	def BalAtSfkpgPlc(self):
		return self._BalAtSfkpgPlc

	@BalAtSfkpgPlc.setter
	def BalAtSfkpgPlc(self, value):
		self._BalAtSfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'BalAtSfkpgPlc', AggregateBalancePerSafekeepingPlace42, True)

	@BalAtSfkpgPlc.deleter
	def BalAtSfkpgPlc(self):
		del self._BalAtSfkpgPlc
		self._BalAtSfkpgPlc = base_types.UninitialisedField(self, 'BalAtSfkpgPlc', AggregateBalancePerSafekeepingPlace42, True)

	@property
	def BalBrkdwn(self):
		return self._BalBrkdwn

	@BalBrkdwn.setter
	def BalBrkdwn(self, value):
		self._BalBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceInformation22, True)

	@BalBrkdwn.deleter
	def BalBrkdwn(self):
		del self._BalBrkdwn
		self._BalBrkdwn = base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceInformation22, True)

	@property
	def CorpActnOptnTp(self):
		return self._CorpActnOptnTp

	@CorpActnOptnTp.setter
	def CorpActnOptnTp(self, value):
		self._CorpActnOptnTp = value if value is not None else base_types.UninitialisedField(self, 'CorpActnOptnTp', CorporateActionOption5Code, False)

	@CorpActnOptnTp.deleter
	def CorpActnOptnTp(self):
		del self._CorpActnOptnTp
		self._CorpActnOptnTp = base_types.UninitialisedField(self, 'CorpActnOptnTp', CorporateActionOption5Code, False)

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
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms34, True)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms34, True)

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

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
	def HldgAddtlDtls(self):
		return self._HldgAddtlDtls

	@HldgAddtlDtls.setter
	def HldgAddtlDtls(self, value):
		self._HldgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'HldgAddtlDtls', Max350Text, False)

	@HldgAddtlDtls.deleter
	def HldgAddtlDtls(self):
		del self._HldgAddtlDtls
		self._HldgAddtlDtls = base_types.UninitialisedField(self, 'HldgAddtlDtls', Max350Text, False)

	@property
	def InstrmCcyAmts(self):
		return self._InstrmCcyAmts

	@InstrmCcyAmts.setter
	def InstrmCcyAmts(self, value):
		self._InstrmCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts1, False)

	@InstrmCcyAmts.deleter
	def InstrmCcyAmts(self):
		del self._InstrmCcyAmts
		self._InstrmCcyAmts = base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts1, False)

	@property
	def InvstmtFndsFinInstrmAttrbts(self):
		return self._InvstmtFndsFinInstrmAttrbts

	@InvstmtFndsFinInstrmAttrbts.setter
	def InvstmtFndsFinInstrmAttrbts(self, value):
		self._InvstmtFndsFinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'InvstmtFndsFinInstrmAttrbts', FinancialInstrument21, False)

	@InvstmtFndsFinInstrmAttrbts.deleter
	def InvstmtFndsFinInstrmAttrbts(self):
		del self._InvstmtFndsFinInstrmAttrbts
		self._InvstmtFndsFinInstrmAttrbts = base_types.UninitialisedField(self, 'InvstmtFndsFinInstrmAttrbts', FinancialInstrument21, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', PriceInformation29, True)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', PriceInformation29, True)

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown58, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown58, True)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace5, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace5, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwn', type=AdditionalBalanceInformation22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlDerivAttrbts', type=DerivativeBasicAttributes1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtBal', type=Balance17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnRptgCcyAmts', type=BalanceAmounts1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAtSfkpgPlc', type=AggregateBalancePerSafekeepingPlace42, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceInformation22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnOptnTp', type=CorporateActionOption5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms34, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndsFinInstrmAttrbts', type=FinancialInstrument21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation29, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown58, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))