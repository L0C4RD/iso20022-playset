from . import base_types
import ProductCategory1Code
import Max35Text

class ProductCategory1(base_types._BaseFieldType):

	__slots__ = ["_Ctgy", "_Tp"]
	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if type(value) != auto else self.make_default("Ctgy")

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctgy', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ProductCategory1Code, min=1, max=1, mutex_group=None, array=False),
	))

