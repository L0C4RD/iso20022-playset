from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .Max35Text import Max35Text
from .CarRentalServiceType2Code import CarRentalServiceType2Code
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .CreditDebit3Code import CreditDebit3Code

class Amount21(base_types._BaseFieldType):

	__slots__ = ["_CdtDbt", "_Amt", "_Tp", "_CstmrNtfd", "_OthrTp"]
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
	def CstmrNtfd(self):
		return self._CstmrNtfd

	@CstmrNtfd.setter
	def CstmrNtfd(self, value):
		self._CstmrNtfd = value if type(value) != base_types.auto else self.make_default("CstmrNtfd")

	@CstmrNtfd.deleter
	def CstmrNtfd(self):
		del self._CstmrNtfd
		self._CstmrNtfd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CarRentalServiceType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNtfd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

