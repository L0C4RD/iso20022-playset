from . import base_types
from ._CreditDebitAmount1 import CreditDebitAmount1

class LimitAmount1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AvlblAmt", "_UtlstnAmt"]
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
	def AvlblAmt(self):
		return self._AvlblAmt

	@AvlblAmt.setter
	def AvlblAmt(self, value):
		self._AvlblAmt = value if type(value) != base_types.auto else self.make_default("AvlblAmt")

	@AvlblAmt.deleter
	def AvlblAmt(self):
		del self._AvlblAmt
		self._AvlblAmt = None

	@property
	def UtlstnAmt(self):
		return self._UtlstnAmt

	@UtlstnAmt.setter
	def UtlstnAmt(self, value):
		self._UtlstnAmt = value if type(value) != base_types.auto else self.make_default("UtlstnAmt")

	@UtlstnAmt.deleter
	def UtlstnAmt(self):
		del self._UtlstnAmt
		self._UtlstnAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CreditDebitAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblAmt', type=CreditDebitAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UtlstnAmt', type=CreditDebitAmount1, min=1, max=1, mutex_group=None, array=False),
	))

