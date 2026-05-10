from . import base_types
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._PostalAddress1 import PostalAddress1

class NameAndAddress8(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_AltrntvIdr", "_Nm"]
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
	def AltrntvIdr(self):
		return self._AltrntvIdr

	@AltrntvIdr.setter
	def AltrntvIdr(self, value):
		self._AltrntvIdr = value if type(value) != base_types.auto else self.make_default("AltrntvIdr")

	@AltrntvIdr.deleter
	def AltrntvIdr(self):
		del self._AltrntvIdr
		self._AltrntvIdr = None

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
		base_types.FieldEntry(name='Adr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrntvIdr', type=Max35Text, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

