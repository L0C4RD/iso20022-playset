from . import base_types
from ._PostalAddress7 import PostalAddress7
from ._RestrictedFINMax35Text import RestrictedFINMax35Text

class NameAndAddress11(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Adr"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

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
		base_types.FieldEntry(name='Adr', type=PostalAddress7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=RestrictedFINMax35Text, min=1, max=1, mutex_group=None, array=False),
	))

