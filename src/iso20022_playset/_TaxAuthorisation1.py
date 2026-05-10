from . import base_types
from ._Max35Text import Max35Text
from ._Max140Text import Max140Text

class TaxAuthorisation1(base_types._BaseFieldType):

	__slots__ = ["_Titl", "_Nm"]
	@property
	def Titl(self):
		return self._Titl

	@Titl.setter
	def Titl(self, value):
		self._Titl = value if type(value) != base_types.auto else self.make_default("Titl")

	@Titl.deleter
	def Titl(self):
		del self._Titl
		self._Titl = None

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
		base_types.FieldEntry(name='Titl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

