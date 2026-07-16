# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBalanceInformation20
from . import Balance17
from . import Balance18
from . import BalanceAmounts3
from . import BalanceQuantity14Choice
from . import ExposureType25Choice
from . import ForeignExchangeTerms34
from . import MarketIdentification3Choice
from . import Max350Text
from . import Number
from . import Pledgee3
from . import PriceInformation29
from . import QuantityBreakdown57
from . import SafeKeepingPlace5
from . import SubBalanceInformation20

class AggregateBalancePerSafekeepingPlace43(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyAmts", "_AddtlBalBrkdwn", "_AggtBal", "_AvlblBal", "_BalBrkdwn", "_DaysAcrd", "_FXDtls", "_HldgAddtlDtls", "_InstrmCcyAmts", "_NotAvlblBal", "_PlcOfListg", "_Pldgee", "_PricDtls", "_QtyBrkdwn", "_SfkpgPlc", "_XpsrTp"]
	@property
	def AcctBaseCcyAmts(self):
		return self._AcctBaseCcyAmts

	@AcctBaseCcyAmts.setter
	def AcctBaseCcyAmts(self, value):
		self._AcctBaseCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts3, False)

	@AcctBaseCcyAmts.deleter
	def AcctBaseCcyAmts(self):
		del self._AcctBaseCcyAmts
		self._AcctBaseCcyAmts = base_types.UninitialisedField(self, 'AcctBaseCcyAmts', BalanceAmounts3, False)

	@property
	def AddtlBalBrkdwn(self):
		return self._AddtlBalBrkdwn

	@AddtlBalBrkdwn.setter
	def AddtlBalBrkdwn(self, value):
		self._AddtlBalBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'AddtlBalBrkdwn', AdditionalBalanceInformation20, True)

	@AddtlBalBrkdwn.deleter
	def AddtlBalBrkdwn(self):
		del self._AddtlBalBrkdwn
		self._AddtlBalBrkdwn = base_types.UninitialisedField(self, 'AddtlBalBrkdwn', AdditionalBalanceInformation20, True)

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
	def AvlblBal(self):
		return self._AvlblBal

	@AvlblBal.setter
	def AvlblBal(self, value):
		self._AvlblBal = value if value is not None else base_types.UninitialisedField(self, 'AvlblBal', Balance18, False)

	@AvlblBal.deleter
	def AvlblBal(self):
		del self._AvlblBal
		self._AvlblBal = base_types.UninitialisedField(self, 'AvlblBal', Balance18, False)

	@property
	def BalBrkdwn(self):
		return self._BalBrkdwn

	@BalBrkdwn.setter
	def BalBrkdwn(self, value):
		self._BalBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceInformation20, True)

	@BalBrkdwn.deleter
	def BalBrkdwn(self):
		del self._BalBrkdwn
		self._BalBrkdwn = base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceInformation20, True)

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
		self._InstrmCcyAmts = value if value is not None else base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts3, False)

	@InstrmCcyAmts.deleter
	def InstrmCcyAmts(self):
		del self._InstrmCcyAmts
		self._InstrmCcyAmts = base_types.UninitialisedField(self, 'InstrmCcyAmts', BalanceAmounts3, False)

	@property
	def NotAvlblBal(self):
		return self._NotAvlblBal

	@NotAvlblBal.setter
	def NotAvlblBal(self, value):
		self._NotAvlblBal = value if value is not None else base_types.UninitialisedField(self, 'NotAvlblBal', BalanceQuantity14Choice, False)

	@NotAvlblBal.deleter
	def NotAvlblBal(self):
		del self._NotAvlblBal
		self._NotAvlblBal = base_types.UninitialisedField(self, 'NotAvlblBal', BalanceQuantity14Choice, False)

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if value is not None else base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification3Choice, False)

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification3Choice, False)

	@property
	def Pldgee(self):
		return self._Pldgee

	@Pldgee.setter
	def Pldgee(self, value):
		self._Pldgee = value if value is not None else base_types.UninitialisedField(self, 'Pldgee', Pledgee3, False)

	@Pldgee.deleter
	def Pldgee(self):
		del self._Pldgee
		self._Pldgee = base_types.UninitialisedField(self, 'Pldgee', Pledgee3, False)

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
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown57, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown57, True)

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
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType25Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType25Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyAmts', type=BalanceAmounts3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwn', type=AdditionalBalanceInformation20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AggtBal', type=Balance17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblBal', type=Balance18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceInformation20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms34, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HldgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmCcyAmts', type=BalanceAmounts3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotAvlblBal', type=BalanceQuantity14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pldgee', type=Pledgee3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation29, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType25Choice, min=0, max=1, mutex_group=None, array=False),
	))