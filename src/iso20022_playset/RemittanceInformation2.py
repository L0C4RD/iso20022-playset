from . import base_types
import Max140Text

class RemittanceInformation2(base_types._BaseFieldType):

	__slots__ = ["_Ustrd"]
	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if type(value) != auto else self.make_default("Ustrd")

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ustrd', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
	))

