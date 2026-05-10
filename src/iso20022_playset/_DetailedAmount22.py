from . import base_types
from ._Max70Text import Max70Text
from ._Max35Text import Max35Text
from ._ISO8583AmountTypeCode import ISO8583AmountTypeCode
from ._CreditDebit3Code import CreditDebit3Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class DetailedAmount22(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_RcncltnAmt", "_Amt", "_CrdhldrBllgAmt", "_CdtDbt", "_OthrTp", "_Tp"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def RcncltnAmt(self):
		return self._RcncltnAmt

	@RcncltnAmt.setter
	def RcncltnAmt(self, value):
		self._RcncltnAmt = value if type(value) != base_types.auto else self.make_default("RcncltnAmt")

	@RcncltnAmt.deleter
	def RcncltnAmt(self):
		del self._RcncltnAmt
		self._RcncltnAmt = None

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
	def CrdhldrBllgAmt(self):
		return self._CrdhldrBllgAmt

	@CrdhldrBllgAmt.setter
	def CrdhldrBllgAmt(self, value):
		self._CrdhldrBllgAmt = value if type(value) != base_types.auto else self.make_default("CrdhldrBllgAmt")

	@CrdhldrBllgAmt.deleter
	def CrdhldrBllgAmt(self):
		del self._CrdhldrBllgAmt
		self._CrdhldrBllgAmt = None

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != base_types.auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ISO8583AmountTypeCode, min=1, max=1, mutex_group=None, array=False),
	))

