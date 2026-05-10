from . import base_types
from .BalanceDetails5 import BalanceDetails5
from .BalanceDetails6 import BalanceDetails6

class PortfolioBalance1(base_types._BaseFieldType):

	__slots__ = ["_DtldBal", "_SummryBal"]
	@property
	def DtldBal(self):
		return self._DtldBal

	@DtldBal.setter
	def DtldBal(self, value):
		self._DtldBal = value if type(value) != auto else self.make_default("DtldBal")

	@DtldBal.deleter
	def DtldBal(self):
		del self._DtldBal
		self._DtldBal = None

	@property
	def SummryBal(self):
		return self._SummryBal

	@SummryBal.setter
	def SummryBal(self, value):
		self._SummryBal = value if type(value) != auto else self.make_default("SummryBal")

	@SummryBal.deleter
	def SummryBal(self):
		del self._SummryBal
		self._SummryBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldBal', type=BalanceDetails6, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SummryBal', type=BalanceDetails5, min=1, max=None, mutex_group=1, array=True),
	))

