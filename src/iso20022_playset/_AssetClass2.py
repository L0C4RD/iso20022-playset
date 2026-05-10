from . import base_types
from ._DerivativeCommodity2 import DerivativeCommodity2
from ._DerivativeInterest3 import DerivativeInterest3
from ._DerivativeForeignExchange3 import DerivativeForeignExchange3

class AssetClass2(base_types._BaseFieldType):

	__slots__ = ["_FX", "_Intrst", "_Cmmdty"]
	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if type(value) != base_types.auto else self.make_default("FX")

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = None

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if type(value) != base_types.auto else self.make_default("Intrst")

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = None

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != base_types.auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FX', type=DerivativeForeignExchange3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=DerivativeInterest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmmdty', type=DerivativeCommodity2, min=0, max=1, mutex_group=None, array=False),
	))

