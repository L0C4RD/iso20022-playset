# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceAdjustment1
from . import BillingBalance1
from . import BillingCompensation1
from . import BillingRate1
from . import BillingService2
from . import BillingServiceAdjustment1
from . import BillingStatementStatus1Code
from . import BillingTaxRegion3
from . import CashAccountCharacteristics5
from . import CurrencyExchange6
from . import DatePeriod1
from . import ISODateTime
from . import Max35Text

class BillingStatement5(base_types._BaseFieldType):

	__slots__ = ["_AcctChrtcs", "_Bal", "_BalAdjstmnt", "_CcyXchg", "_Compstn", "_CreDtTm", "_FrToDt", "_RateData", "_StmtId", "_Sts", "_Svc", "_SvcAdjstmnt", "_TaxRgn"]
	@property
	def AcctChrtcs(self):
		return self._AcctChrtcs

	@AcctChrtcs.setter
	def AcctChrtcs(self, value):
		self._AcctChrtcs = value if value is not None else base_types.UninitialisedField(self, 'AcctChrtcs', CashAccountCharacteristics5, False)

	@AcctChrtcs.deleter
	def AcctChrtcs(self):
		del self._AcctChrtcs
		self._AcctChrtcs = base_types.UninitialisedField(self, 'AcctChrtcs', CashAccountCharacteristics5, False)

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', BillingBalance1, True)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', BillingBalance1, True)

	@property
	def BalAdjstmnt(self):
		return self._BalAdjstmnt

	@BalAdjstmnt.setter
	def BalAdjstmnt(self, value):
		self._BalAdjstmnt = value if value is not None else base_types.UninitialisedField(self, 'BalAdjstmnt', BalanceAdjustment1, True)

	@BalAdjstmnt.deleter
	def BalAdjstmnt(self):
		del self._BalAdjstmnt
		self._BalAdjstmnt = base_types.UninitialisedField(self, 'BalAdjstmnt', BalanceAdjustment1, True)

	@property
	def CcyXchg(self):
		return self._CcyXchg

	@CcyXchg.setter
	def CcyXchg(self, value):
		self._CcyXchg = value if value is not None else base_types.UninitialisedField(self, 'CcyXchg', CurrencyExchange6, True)

	@CcyXchg.deleter
	def CcyXchg(self):
		del self._CcyXchg
		self._CcyXchg = base_types.UninitialisedField(self, 'CcyXchg', CurrencyExchange6, True)

	@property
	def Compstn(self):
		return self._Compstn

	@Compstn.setter
	def Compstn(self, value):
		self._Compstn = value if value is not None else base_types.UninitialisedField(self, 'Compstn', BillingCompensation1, True)

	@Compstn.deleter
	def Compstn(self):
		del self._Compstn
		self._Compstn = base_types.UninitialisedField(self, 'Compstn', BillingCompensation1, True)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if value is not None else base_types.UninitialisedField(self, 'FrToDt', DatePeriod1, False)

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = base_types.UninitialisedField(self, 'FrToDt', DatePeriod1, False)

	@property
	def RateData(self):
		return self._RateData

	@RateData.setter
	def RateData(self, value):
		self._RateData = value if value is not None else base_types.UninitialisedField(self, 'RateData', BillingRate1, True)

	@RateData.deleter
	def RateData(self):
		del self._RateData
		self._RateData = base_types.UninitialisedField(self, 'RateData', BillingRate1, True)

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if value is not None else base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', BillingStatementStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', BillingStatementStatus1Code, False)

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if value is not None else base_types.UninitialisedField(self, 'Svc', BillingService2, True)

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = base_types.UninitialisedField(self, 'Svc', BillingService2, True)

	@property
	def SvcAdjstmnt(self):
		return self._SvcAdjstmnt

	@SvcAdjstmnt.setter
	def SvcAdjstmnt(self, value):
		self._SvcAdjstmnt = value if value is not None else base_types.UninitialisedField(self, 'SvcAdjstmnt', BillingServiceAdjustment1, True)

	@SvcAdjstmnt.deleter
	def SvcAdjstmnt(self):
		del self._SvcAdjstmnt
		self._SvcAdjstmnt = base_types.UninitialisedField(self, 'SvcAdjstmnt', BillingServiceAdjustment1, True)

	@property
	def TaxRgn(self):
		return self._TaxRgn

	@TaxRgn.setter
	def TaxRgn(self, value):
		self._TaxRgn = value if value is not None else base_types.UninitialisedField(self, 'TaxRgn', BillingTaxRegion3, True)

	@TaxRgn.deleter
	def TaxRgn(self):
		del self._TaxRgn
		self._TaxRgn = base_types.UninitialisedField(self, 'TaxRgn', BillingTaxRegion3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctChrtcs', type=CashAccountCharacteristics5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=BillingBalance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalAdjstmnt', type=BalanceAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyXchg', type=CurrencyExchange6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Compstn', type=BillingCompensation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrToDt', type=DatePeriod1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateData', type=BillingRate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=BillingStatementStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=BillingService2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcAdjstmnt', type=BillingServiceAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRgn', type=BillingTaxRegion3, min=0, max=None, mutex_group=None, array=True),
	))