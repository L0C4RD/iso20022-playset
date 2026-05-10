import base_types
import DerivativeForeignExchange2
import DerivativeInterest2

class AssetClassAttributes1(base_types._BaseFieldType):

	__slots__ = ["_Intrst", "_FX"]
	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if type(value) != auto else self.make_default("Intrst")

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = None

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if type(value) != auto else self.make_default("FX")

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Intrst', type=DerivativeInterest2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FX', type=DerivativeForeignExchange2, min=1, max=1, mutex_group=None, array=False),
	))

