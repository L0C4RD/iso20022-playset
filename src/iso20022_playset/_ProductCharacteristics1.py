from . import base_types
from ._Max35Text import Max35Text
from ._ProductCharacteristics1Code import ProductCharacteristics1Code

class ProductCharacteristics1(base_types._BaseFieldType):

	__slots__ = ["_Chrtcs", "_Tp"]
	@property
	def Chrtcs(self):
		return self._Chrtcs

	@Chrtcs.setter
	def Chrtcs(self, value):
		self._Chrtcs = value if type(value) != base_types.auto else self.make_default("Chrtcs")

	@Chrtcs.deleter
	def Chrtcs(self):
		del self._Chrtcs
		self._Chrtcs = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chrtcs', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ProductCharacteristics1Code, min=1, max=1, mutex_group=None, array=False),
	))

