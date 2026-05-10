from . import base_types
from .ISODateTime import ISODateTime
from .BillingRate1 import BillingRate1
from .CurrencyExchange6 import CurrencyExchange6
from .BillingService2 import BillingService2
from .CashAccountCharacteristics5 import CashAccountCharacteristics5
from .BillingTaxRegion3 import BillingTaxRegion3
from .BalanceAdjustment1 import BalanceAdjustment1
from .Max35Text import Max35Text
from .BillingStatementStatus1Code import BillingStatementStatus1Code
from .DatePeriod1 import DatePeriod1
from .BillingBalance1 import BillingBalance1
from .BillingServiceAdjustment1 import BillingServiceAdjustment1
from .BillingCompensation1 import BillingCompensation1

class BillingStatement5(base_types._BaseFieldType):

	__slots__ = ["_SvcAdjstmnt", "_StmtId", "_CcyXchg", "_TaxRgn", "_AcctChrtcs", "_Sts", "_FrToDt", "_Bal", "_BalAdjstmnt", "_Compstn", "_CreDtTm", "_RateData", "_Svc"]
	@property
	def SvcAdjstmnt(self):
		return self._SvcAdjstmnt

	@SvcAdjstmnt.setter
	def SvcAdjstmnt(self, value):
		self._SvcAdjstmnt = value if type(value) != base_types.auto else self.make_default("SvcAdjstmnt")

	@SvcAdjstmnt.deleter
	def SvcAdjstmnt(self):
		del self._SvcAdjstmnt
		self._SvcAdjstmnt = None

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != base_types.auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	@property
	def CcyXchg(self):
		return self._CcyXchg

	@CcyXchg.setter
	def CcyXchg(self, value):
		self._CcyXchg = value if type(value) != base_types.auto else self.make_default("CcyXchg")

	@CcyXchg.deleter
	def CcyXchg(self):
		del self._CcyXchg
		self._CcyXchg = None

	@property
	def TaxRgn(self):
		return self._TaxRgn

	@TaxRgn.setter
	def TaxRgn(self, value):
		self._TaxRgn = value if type(value) != base_types.auto else self.make_default("TaxRgn")

	@TaxRgn.deleter
	def TaxRgn(self):
		del self._TaxRgn
		self._TaxRgn = None

	@property
	def AcctChrtcs(self):
		return self._AcctChrtcs

	@AcctChrtcs.setter
	def AcctChrtcs(self, value):
		self._AcctChrtcs = value if type(value) != base_types.auto else self.make_default("AcctChrtcs")

	@AcctChrtcs.deleter
	def AcctChrtcs(self):
		del self._AcctChrtcs
		self._AcctChrtcs = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if type(value) != base_types.auto else self.make_default("FrToDt")

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def BalAdjstmnt(self):
		return self._BalAdjstmnt

	@BalAdjstmnt.setter
	def BalAdjstmnt(self, value):
		self._BalAdjstmnt = value if type(value) != base_types.auto else self.make_default("BalAdjstmnt")

	@BalAdjstmnt.deleter
	def BalAdjstmnt(self):
		del self._BalAdjstmnt
		self._BalAdjstmnt = None

	@property
	def Compstn(self):
		return self._Compstn

	@Compstn.setter
	def Compstn(self, value):
		self._Compstn = value if type(value) != base_types.auto else self.make_default("Compstn")

	@Compstn.deleter
	def Compstn(self):
		del self._Compstn
		self._Compstn = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def RateData(self):
		return self._RateData

	@RateData.setter
	def RateData(self, value):
		self._RateData = value if type(value) != base_types.auto else self.make_default("RateData")

	@RateData.deleter
	def RateData(self):
		del self._RateData
		self._RateData = None

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if type(value) != base_types.auto else self.make_default("Svc")

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcAdjstmnt', type=BillingServiceAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchg', type=CurrencyExchange6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRgn', type=BillingTaxRegion3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctChrtcs', type=CashAccountCharacteristics5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=BillingStatementStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrToDt', type=DatePeriod1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=BillingBalance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalAdjstmnt', type=BalanceAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Compstn', type=BillingCompensation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateData', type=BillingRate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Svc', type=BillingService2, min=0, max=None, mutex_group=None, array=True),
	))

