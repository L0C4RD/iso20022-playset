from . import base_types
from ._Exact3NumericText import Exact3NumericText
from ._Exact5NumericText import Exact5NumericText

class Number3Choice(base_types._BaseFieldType):

	__slots__ = ["_Lng", "_Shrt"]
	@property
	def Lng(self):
		return self._Lng

	@Lng.setter
	def Lng(self, value):
		self._Lng = value if type(value) != base_types.auto else self.make_default("Lng")

	@Lng.deleter
	def Lng(self):
		del self._Lng
		self._Lng = None

	@property
	def Shrt(self):
		return self._Shrt

	@Shrt.setter
	def Shrt(self, value):
		self._Shrt = value if type(value) != base_types.auto else self.make_default("Shrt")

	@Shrt.deleter
	def Shrt(self):
		del self._Shrt
		self._Shrt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lng', type=Exact5NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Shrt', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
	))

