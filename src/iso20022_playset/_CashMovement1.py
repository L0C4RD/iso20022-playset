from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Charges1 import Charges1
from ._Max35Text import Max35Text
from ._CashAccount18 import CashAccount18

class CashMovement1(base_types._BaseFieldType):

	__slots__ = ["_TaxAmt", "_AcctDtls", "_Chrgs", "_MvmntId", "_Amt"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

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
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != base_types.auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def MvmntId(self):
		return self._MvmntId

	@MvmntId.setter
	def MvmntId(self, value):
		self._MvmntId = value if type(value) != base_types.auto else self.make_default("MvmntId")

	@MvmntId.deleter
	def MvmntId(self):
		del self._MvmntId
		self._MvmntId = None

	@property
	def TaxAmt(self):
		return self._TaxAmt

	@TaxAmt.setter
	def TaxAmt(self, value):
		self._TaxAmt = value if type(value) != base_types.auto else self.make_default("TaxAmt")

	@TaxAmt.deleter
	def TaxAmt(self):
		del self._TaxAmt
		self._TaxAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=CashAccount18, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

