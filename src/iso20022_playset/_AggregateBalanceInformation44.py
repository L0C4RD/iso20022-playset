from . import base_types
from ._FinancialInstrumentAttributes122 import FinancialInstrumentAttributes122
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text
from ._AggregateBalancePerSafekeepingPlace41 import AggregateBalancePerSafekeepingPlace41
from ._Balance25 import Balance25
from ._Number import Number
from ._CorporateActionOption5Code import CorporateActionOption5Code
from ._FinancialInstrument22 import FinancialInstrument22
from ._SecurityIdentification20 import SecurityIdentification20
from ._AdditionalBalanceInformation24 import AdditionalBalanceInformation24
from ._BasicCollateralValuation1Details import BasicCollateralValuation1Details
from ._SupplementaryData1 import SupplementaryData1
from ._SafeKeepingPlace4 import SafeKeepingPlace4
from ._SubBalanceInformation24 import SubBalanceInformation24
from ._PriceInformation22 import PriceInformation22
from ._QuantityBreakdown71 import QuantityBreakdown71
from ._BalanceQuantity17Choice import BalanceQuantity17Choice
from ._BalanceAmounts4 import BalanceAmounts4
from ._ForeignExchangeTerms35 import ForeignExchangeTerms35
from ._Balance22 import Balance22

class AggregateBalanceInformation44(base_types._BaseFieldType):

	__slots__ = ["_InvstmtFndsFinInstrmAttrbts", "_SfkpgPlc", "_AggtBal", "_NotAvlblBal", "_BalBrkdwn", "_InstrmCcyAmts", "_AddtlBalBrkdwn", "_BalAtSfkpgPlc", "_FinInstrmAttrbts", "_DaysAcrd", "_PricDtls", "_QtyBrkdwn", "_AvlblBal", "_AcctBaseCcyAmts", "_CorpActnOptnTp", "_ValtnHrcutDtls", "_FinInstrmId", "_FXDtls", "_HldgAddtlDtls", "_SplmtryData"]
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
	def AvlblBal(self):
		return self._AvlblBal

	@AvlblBal.setter
	def AvlblBal(self, value):
		self._AvlblBal = value if type(value) != base_types.auto else self.make_default("AvlblBal")

	@AvlblBal.deleter
	def AvlblBal(self):
		del self._AvlblBal
		self._AvlblBal = None

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
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

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
	def NotAvlblBal(self):
		return self._NotAvlblBal

	@NotAvlblBal.setter
	def NotAvlblBal(self, value):
		self._NotAvlblBal = value if type(value) != base_types.auto else self.make_default("NotAvlblBal")

	@NotAvlblBal.deleter
	def NotAvlblBal(self):
		del self._NotAvlblBal
		self._NotAvlblBal = None

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
	def ValtnHrcutDtls(self):
		return self._ValtnHrcutDtls

	@ValtnHrcutDtls.setter
	def ValtnHrcutDtls(self, value):
		self._ValtnHrcutDtls = value if type(value) != base_types.auto else self.make_default("ValtnHrcutDtls")

	@ValtnHrcutDtls.deleter
	def ValtnHrcutDtls(self):
		del self._ValtnHrcutDtls
		self._ValtnHrcutDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwn', type=AdditionalBalanceInformation24, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AggtBal', type=Balance22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblBal', type=Balance25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAtSfkpgPlc', type=AggregateBalancePerSafekeepingPlace41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceInformation24, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnOptnTp', type=CorporateActionOption5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms35, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndsFinInstrmAttrbts', type=FinancialInstrument22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotAvlblBal', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown71, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValtnHrcutDtls', type=BasicCollateralValuation1Details, min=0, max=1, mutex_group=None, array=False),
	))

