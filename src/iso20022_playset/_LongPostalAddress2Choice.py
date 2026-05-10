from . import base_types
from ._Max350Text import Max350Text
from ._PostalAddress1 import PostalAddress1

class LongPostalAddress2Choice(base_types._BaseFieldType):

	__slots__ = ["_Strd", "_Ustrd"]
	@property
	def Strd(self):
		return self._Strd

	@Strd.setter
	def Strd(self, value):
		self._Strd = value if type(value) != base_types.auto else self.make_default("Strd")

	@Strd.deleter
	def Strd(self):
		del self._Strd
		self._Strd = None

	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if type(value) != base_types.auto else self.make_default("Ustrd")

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Strd', type=PostalAddress1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ustrd', type=Max350Text, min=0, max=1, mutex_group=1, array=False),
	))

