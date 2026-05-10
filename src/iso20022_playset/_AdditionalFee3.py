from . import base_types
from .TypeOfAmount21Code import TypeOfAmount21Code
from .Max35Text import Max35Text
from .BaseOne25Rate import BaseOne25Rate
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .PartyType32Code import PartyType32Code
from .Max140Text import Max140Text
from .ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from .CreditDebit3Code import CreditDebit3Code

class AdditionalFee3(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Tp", "_Prgm", "_OthrTp", "_Amt", "_CdtDbt", "_RcncltnFctvXchgRate", "_RcncltnAmt", "_Assgnr", "_Dscrptr", "_OthrAssgnr", "_Desc", "_RcncltnCcy"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

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
	def Prgm(self):
		return self._Prgm

	@Prgm.setter
	def Prgm(self, value):
		self._Prgm = value if type(value) != base_types.auto else self.make_default("Prgm")

	@Prgm.deleter
	def Prgm(self):
		del self._Prgm
		self._Prgm = None

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
	def RcncltnFctvXchgRate(self):
		return self._RcncltnFctvXchgRate

	@RcncltnFctvXchgRate.setter
	def RcncltnFctvXchgRate(self, value):
		self._RcncltnFctvXchgRate = value if type(value) != base_types.auto else self.make_default("RcncltnFctvXchgRate")

	@RcncltnFctvXchgRate.deleter
	def RcncltnFctvXchgRate(self):
		del self._RcncltnFctvXchgRate
		self._RcncltnFctvXchgRate = None

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
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def Dscrptr(self):
		return self._Dscrptr

	@Dscrptr.setter
	def Dscrptr(self, value):
		self._Dscrptr = value if type(value) != base_types.auto else self.make_default("Dscrptr")

	@Dscrptr.deleter
	def Dscrptr(self):
		del self._Dscrptr
		self._Dscrptr = None

	@property
	def OthrAssgnr(self):
		return self._OthrAssgnr

	@OthrAssgnr.setter
	def OthrAssgnr(self, value):
		self._OthrAssgnr = value if type(value) != base_types.auto else self.make_default("OthrAssgnr")

	@OthrAssgnr.deleter
	def OthrAssgnr(self):
		del self._OthrAssgnr
		self._OthrAssgnr = None

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
	def RcncltnCcy(self):
		return self._RcncltnCcy

	@RcncltnCcy.setter
	def RcncltnCcy(self, value):
		self._RcncltnCcy = value if type(value) != base_types.auto else self.make_default("RcncltnCcy")

	@RcncltnCcy.deleter
	def RcncltnCcy(self):
		del self._RcncltnCcy
		self._RcncltnCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfAmount21Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFctvXchgRate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=PartyType32Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dscrptr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

