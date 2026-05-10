from . import base_types
from .FinancialAssetTypeCategory1Code import FinancialAssetTypeCategory1Code
from .BalanceType7Choice import BalanceType7Choice
from .Unrealised1Code import Unrealised1Code
from .AmountAndDirection31 import AmountAndDirection31

class BalanceDetails6(base_types._BaseFieldType):

	__slots__ = ["_Urlsd", "_Tp", "_Ctgy", "_Amt"]
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
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if type(value) != base_types.auto else self.make_default("Ctgy")

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Urlsd', type=Unrealised1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceType7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=FinancialAssetTypeCategory1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountAndDirection31, min=1, max=1, mutex_group=None, array=False),
	))

