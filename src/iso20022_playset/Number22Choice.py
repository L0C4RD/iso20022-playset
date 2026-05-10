from . import base_types
import GenericIdentification1
import Exact3NumericText

class Number22Choice(base_types._BaseFieldType):

	__slots__ = ["_Shrt", "_Lng"]
	@property
	def Shrt(self):
		return self._Shrt

	@Shrt.setter
	def Shrt(self, value):
		self._Shrt = value if type(value) != auto else self.make_default("Shrt")

	@Shrt.deleter
	def Shrt(self):
		del self._Shrt
		self._Shrt = None

	@property
	def Lng(self):
		return self._Lng

	@Lng.setter
	def Lng(self, value):
		self._Lng = value if type(value) != auto else self.make_default("Lng")

	@Lng.deleter
	def Lng(self):
		del self._Lng
		self._Lng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Shrt', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Lng', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

