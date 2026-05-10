from . import base_types
from .CashAccount19 import CashAccount19
from .Max350Text import Max350Text
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class CashProceeds1(base_types._BaseFieldType):

	__slots__ = ["_RcncltnDtls", "_PstngAmt", "_AcctDtls"]
	@property
	def RcncltnDtls(self):
		return self._RcncltnDtls

	@RcncltnDtls.setter
	def RcncltnDtls(self, value):
		self._RcncltnDtls = value if type(value) != auto else self.make_default("RcncltnDtls")

	@RcncltnDtls.deleter
	def RcncltnDtls(self):
		del self._RcncltnDtls
		self._RcncltnDtls = None

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if type(value) != auto else self.make_default("PstngAmt")

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=CashAccount19, min=1, max=2, mutex_group=None, array=False),
	))

