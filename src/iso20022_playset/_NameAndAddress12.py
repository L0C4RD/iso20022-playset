from . import base_types
from ._RestrictedFINXMax140Text import RestrictedFINXMax140Text

class NameAndAddress12(base_types._BaseFieldType):

	__slots__ = ["_Nm"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=RestrictedFINXMax140Text, min=1, max=1, mutex_group=None, array=False),
	))

