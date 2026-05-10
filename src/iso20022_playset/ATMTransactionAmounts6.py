from . import base_types
from .ActiveCurrencyCode import ActiveCurrencyCode
from .ATMTransactionAmounts7 import ATMTransactionAmounts7
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class ATMTransactionAmounts6(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_AddtlAmt", "_MaxPssblAmt", "_MinPssblAmt"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if type(value) != auto else self.make_default("AddtlAmt")

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = None

	@property
	def MaxPssblAmt(self):
		return self._MaxPssblAmt

	@MaxPssblAmt.setter
	def MaxPssblAmt(self, value):
		self._MaxPssblAmt = value if type(value) != auto else self.make_default("MaxPssblAmt")

	@MaxPssblAmt.deleter
	def MaxPssblAmt(self):
		del self._MaxPssblAmt
		self._MaxPssblAmt = None

	@property
	def MinPssblAmt(self):
		return self._MinPssblAmt

	@MinPssblAmt.setter
	def MinPssblAmt(self, value):
		self._MinPssblAmt = value if type(value) != auto else self.make_default("MinPssblAmt")

	@MinPssblAmt.deleter
	def MinPssblAmt(self):
		del self._MinPssblAmt
		self._MinPssblAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAmt', type=ATMTransactionAmounts7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxPssblAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPssblAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

