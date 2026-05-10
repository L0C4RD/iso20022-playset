from . import base_types
from ._DerivativeForeignExchange2 import DerivativeForeignExchange2
from ._DerivativeInterest2 import DerivativeInterest2
from ._AssetClassAttributes1 import AssetClassAttributes1

class AssetClassAttributes1Choice(base_types._BaseFieldType):

	__slots__ = ["_FX", "_Both", "_Intrst"]
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
	def Both(self):
		return self._Both

	@Both.setter
	def Both(self, value):
		self._Both = value if type(value) != base_types.auto else self.make_default("Both")

	@Both.deleter
	def Both(self):
		del self._Both
		self._Both = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FX', type=DerivativeForeignExchange2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Both', type=AssetClassAttributes1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Intrst', type=DerivativeInterest2, min=0, max=1, mutex_group=1, array=False),
	))

