from . import base_types
from ._BalanceDetails6 import BalanceDetails6
from ._Unrealised1Code import Unrealised1Code
from ._AmountAndDirection31 import AmountAndDirection31
from ._BalanceType6Choice import BalanceType6Choice

class BalanceDetails5(base_types._BaseFieldType):

	__slots__ = ["_DtldBal", "_Tp", "_Amt", "_Urlsd"]
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
	def DtldBal(self):
		return self._DtldBal

	@DtldBal.setter
	def DtldBal(self, value):
		self._DtldBal = value if type(value) != base_types.auto else self.make_default("DtldBal")

	@DtldBal.deleter
	def DtldBal(self):
		del self._DtldBal
		self._DtldBal = None

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
	def Urlsd(self):
		return self._Urlsd

	@Urlsd.setter
	def Urlsd(self, value):
		self._Urlsd = value if type(value) != base_types.auto else self.make_default("Urlsd")

	@Urlsd.deleter
	def Urlsd(self):
		del self._Urlsd
		self._Urlsd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountAndDirection31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldBal', type=BalanceDetails6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=BalanceType6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Urlsd', type=Unrealised1Code, min=0, max=1, mutex_group=None, array=False),
	))

