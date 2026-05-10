from . import base_types
from .Number import Number
from .PriceInformation22 import PriceInformation22
from .ExposureType24Choice import ExposureType24Choice
from .QuantityBreakdown71 import QuantityBreakdown71
from .Balance25 import Balance25
from .Pledgee4 import Pledgee4
from .Balance22 import Balance22
from .BalanceAmounts4 import BalanceAmounts4
from .AdditionalBalanceInformation24 import AdditionalBalanceInformation24
from .ForeignExchangeTerms35 import ForeignExchangeTerms35
from .BalanceQuantity17Choice import BalanceQuantity17Choice
from .RestrictedFINXMax350Text import RestrictedFINXMax350Text
from .SafeKeepingPlace4 import SafeKeepingPlace4
from .SubBalanceInformation24 import SubBalanceInformation24
from .MarketIdentification4Choice import MarketIdentification4Choice

class AggregateBalancePerSafekeepingPlace41(base_types._BaseFieldType):

	__slots__ = ["_QtyBrkdwn", "_AggtBal", "_NotAvlblBal", "_PlcOfListg", "_FXDtls", "_DaysAcrd", "_AvlblBal", "_InstrmCcyAmts", "_AcctBaseCcyAmts", "_PricDtls", "_XpsrTp", "_BalBrkdwn", "_HldgAddtlDtls", "_Pldgee", "_AddtlBalBrkdwn", "_SfkpgPlc"]
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
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if type(value) != base_types.auto else self.make_default("PlcOfListg")

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = None

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
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

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
	def Pldgee(self):
		return self._Pldgee

	@Pldgee.setter
	def Pldgee(self, value):
		self._Pldgee = value if type(value) != base_types.auto else self.make_default("Pldgee")

	@Pldgee.deleter
	def Pldgee(self):
		del self._Pldgee
		self._Pldgee = None

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
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown71, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AggtBal', type=Balance22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotAvlblBal', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms35, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblBal', type=Balance25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceInformation24, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HldgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pldgee', type=Pledgee4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwn', type=AdditionalBalanceInformation24, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=1, max=1, mutex_group=None, array=False),
	))

