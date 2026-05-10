from . import base_types
import Max350Text
import PostalAddress26

class PersonName2(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Nm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=PostalAddress26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

