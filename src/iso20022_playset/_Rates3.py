from . import base_types
from ._SecuritiesTransactionPrice18Choice import SecuritiesTransactionPrice18Choice
from ._PercentageRate import PercentageRate

class Rates3(base_types._BaseFieldType):

	__slots__ = ["_BuySellBck", "_Fltg", "_Fxd"]
	@property
	def BuySellBck(self):
		return self._BuySellBck

	@BuySellBck.setter
	def BuySellBck(self, value):
		self._BuySellBck = value if type(value) != base_types.auto else self.make_default("BuySellBck")

	@BuySellBck.deleter
	def BuySellBck(self):
		del self._BuySellBck
		self._BuySellBck = None

	@property
	def Fltg(self):
		return self._Fltg

	@Fltg.setter
	def Fltg(self, value):
		self._Fltg = value if type(value) != base_types.auto else self.make_default("Fltg")

	@Fltg.deleter
	def Fltg(self):
		del self._Fltg
		self._Fltg = None

	@property
	def Fxd(self):
		return self._Fxd

	@Fxd.setter
	def Fxd(self, value):
		self._Fxd = value if type(value) != base_types.auto else self.make_default("Fxd")

	@Fxd.deleter
	def Fxd(self):
		del self._Fxd
		self._Fxd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuySellBck', type=SecuritiesTransactionPrice18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fltg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fxd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

