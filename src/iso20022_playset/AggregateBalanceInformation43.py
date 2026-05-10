from . import base_types
from .SafeKeepingPlace4 import SafeKeepingPlace4
from .Number import Number
from .QuantityBreakdown70 import QuantityBreakdown70
from .AdditionalBalanceInformation23 import AdditionalBalanceInformation23
from .CorporateActionOption5Code import CorporateActionOption5Code
from .SubBalanceInformation23 import SubBalanceInformation23
from .FinancialInstrument22 import FinancialInstrument22
from .PriceInformation22 import PriceInformation22
from .FinancialInstrumentAttributes122 import FinancialInstrumentAttributes122
from .SecurityIdentification20 import SecurityIdentification20
from .Balance22 import Balance22
from .RestrictedFINXMax350Text import RestrictedFINXMax350Text
from .SupplementaryData1 import SupplementaryData1
from .AggregateBalancePerSafekeepingPlace40 import AggregateBalancePerSafekeepingPlace40
from .DerivativeBasicAttributes2 import DerivativeBasicAttributes2
from .ForeignExchangeTerms35 import ForeignExchangeTerms35
from .BalanceAmounts5 import BalanceAmounts5

class AggregateBalanceInformation43(base_types._BaseFieldType):

	__slots__ = ["_PricDtls", "_QtyBrkdwn", "_AcctBaseCcyAmts", "_AltrnRptgCcyAmts", "_AddtlDerivAttrbts", "_AggtBal", "_InvstmtFndsFinInstrmAttrbts", "_AddtlBalBrkdwn", "_FXDtls", "_DaysAcrd", "_FinInstrmAttrbts", "_SplmtryData", "_BalBrkdwn", "_InstrmCcyAmts", "_SfkpgPlc", "_HldgAddtlDtls", "_BalAtSfkpgPlc", "_CorpActnOptnTp", "_FinInstrmId"]
	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != base_types.auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

	@property
	def AcctBaseCcyAmts(self):
		return self._AcctBaseCcyAmts

	@AcctBaseCcyAmts.setter
	def AcctBaseCcyAmts(self, value):
		self._AcctBaseCcyAmts = value if type(value) != base_types.auto else self.make_default("AcctBaseCcyAmts")

	@AcctBaseCcyAmts.deleter
	def AcctBaseCcyAmts(self):
		del self._AcctBaseCcyAmts
		self._AcctBaseCcyAmts = None

	@property
	def AltrnRptgCcyAmts(self):
		return self._AltrnRptgCcyAmts

	@AltrnRptgCcyAmts.setter
	def AltrnRptgCcyAmts(self, value):
		self._AltrnRptgCcyAmts = value if type(value) != base_types.auto else self.make_default("AltrnRptgCcyAmts")

	@AltrnRptgCcyAmts.deleter
	def AltrnRptgCcyAmts(self):
		del self._AltrnRptgCcyAmts
		self._AltrnRptgCcyAmts = None

	@property
	def AddtlDerivAttrbts(self):
		return self._AddtlDerivAttrbts

	@AddtlDerivAttrbts.setter
	def AddtlDerivAttrbts(self, value):
		self._AddtlDerivAttrbts = value if type(value) != base_types.auto else self.make_default("AddtlDerivAttrbts")

	@AddtlDerivAttrbts.deleter
	def AddtlDerivAttrbts(self):
		del self._AddtlDerivAttrbts
		self._AddtlDerivAttrbts = None

	@property
	def AggtBal(self):
		return self._AggtBal

	@AggtBal.setter
	def AggtBal(self, value):
		self._AggtBal = value if type(value) != base_types.auto else self.make_default("AggtBal")

	@AggtBal.deleter
	def AggtBal(self):
		del self._AggtBal
		self._AggtBal = None

	@property
	def InvstmtFndsFinInstrmAttrbts(self):
		return self._InvstmtFndsFinInstrmAttrbts

	@InvstmtFndsFinInstrmAttrbts.setter
	def InvstmtFndsFinInstrmAttrbts(self, value):
		self._InvstmtFndsFinInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("InvstmtFndsFinInstrmAttrbts")

	@InvstmtFndsFinInstrmAttrbts.deleter
	def InvstmtFndsFinInstrmAttrbts(self):
		del self._InvstmtFndsFinInstrmAttrbts
		self._InvstmtFndsFinInstrmAttrbts = None

	@property
	def AddtlBalBrkdwn(self):
		return self._AddtlBalBrkdwn

	@AddtlBalBrkdwn.setter
	def AddtlBalBrkdwn(self, value):
		self._AddtlBalBrkdwn = value if type(value) != base_types.auto else self.make_default("AddtlBalBrkdwn")

	@AddtlBalBrkdwn.deleter
	def AddtlBalBrkdwn(self):
		del self._AddtlBalBrkdwn
		self._AddtlBalBrkdwn = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != base_types.auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def DaysAcrd(self):
		return self._DaysAcrd

	@DaysAcrd.setter
	def DaysAcrd(self, value):
		self._DaysAcrd = value if type(value) != base_types.auto else self.make_default("DaysAcrd")

	@DaysAcrd.deleter
	def DaysAcrd(self):
		del self._DaysAcrd
		self._DaysAcrd = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def BalBrkdwn(self):
		return self._BalBrkdwn

	@BalBrkdwn.setter
	def BalBrkdwn(self, value):
		self._BalBrkdwn = value if type(value) != base_types.auto else self.make_default("BalBrkdwn")

	@BalBrkdwn.deleter
	def BalBrkdwn(self):
		del self._BalBrkdwn
		self._BalBrkdwn = None

	@property
	def InstrmCcyAmts(self):
		return self._InstrmCcyAmts

	@InstrmCcyAmts.setter
	def InstrmCcyAmts(self, value):
		self._InstrmCcyAmts = value if type(value) != base_types.auto else self.make_default("InstrmCcyAmts")

	@InstrmCcyAmts.deleter
	def InstrmCcyAmts(self):
		del self._InstrmCcyAmts
		self._InstrmCcyAmts = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def HldgAddtlDtls(self):
		return self._HldgAddtlDtls

	@HldgAddtlDtls.setter
	def HldgAddtlDtls(self, value):
		self._HldgAddtlDtls = value if type(value) != base_types.auto else self.make_default("HldgAddtlDtls")

	@HldgAddtlDtls.deleter
	def HldgAddtlDtls(self):
		del self._HldgAddtlDtls
		self._HldgAddtlDtls = None

	@property
	def BalAtSfkpgPlc(self):
		return self._BalAtSfkpgPlc

	@BalAtSfkpgPlc.setter
	def BalAtSfkpgPlc(self, value):
		self._BalAtSfkpgPlc = value if type(value) != base_types.auto else self.make_default("BalAtSfkpgPlc")

	@BalAtSfkpgPlc.deleter
	def BalAtSfkpgPlc(self):
		del self._BalAtSfkpgPlc
		self._BalAtSfkpgPlc = None

	@property
	def CorpActnOptnTp(self):
		return self._CorpActnOptnTp

	@CorpActnOptnTp.setter
	def CorpActnOptnTp(self, value):
		self._CorpActnOptnTp = value if type(value) != base_types.auto else self.make_default("CorpActnOptnTp")

	@CorpActnOptnTp.deleter
	def CorpActnOptnTp(self):
		del self._CorpActnOptnTp
		self._CorpActnOptnTp = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricDtls', type=PriceInformation22, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown70, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnRptgCcyAmts', type=BalanceAmounts5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlDerivAttrbts', type=DerivativeBasicAttributes2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtBal', type=Balance22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndsFinInstrmAttrbts', type=FinancialInstrument22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwn', type=AdditionalBalanceInformation23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms35, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceInformation23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAtSfkpgPlc', type=AggregateBalancePerSafekeepingPlace40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnOptnTp', type=CorporateActionOption5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
	))

