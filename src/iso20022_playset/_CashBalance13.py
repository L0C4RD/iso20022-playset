from . import base_types
from .Number import Number
from .CreditDebitCode import CreditDebitCode
from .BalanceStatus1Code import BalanceStatus1Code
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .BalanceType11Choice import BalanceType11Choice
from .BalanceRestrictionType1 import BalanceRestrictionType1

class CashBalance13(base_types._BaseFieldType):

	__slots__ = ["_NbOfPmts", "_ValDt", "_CdtDbtInd", "_Amt", "_RstrctnTp", "_Tp", "_Sts", "_PrcgDt"]
	@property
	def NbOfPmts(self):
		return self._NbOfPmts

	@NbOfPmts.setter
	def NbOfPmts(self, value):
		self._NbOfPmts = value if type(value) != base_types.auto else self.make_default("NbOfPmts")

	@NbOfPmts.deleter
	def NbOfPmts(self):
		del self._NbOfPmts
		self._NbOfPmts = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if type(value) != base_types.auto else self.make_default("RstrctnTp")

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if type(value) != base_types.auto else self.make_default("PrcgDt")

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnTp', type=BalanceRestrictionType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceType11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=BalanceStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

