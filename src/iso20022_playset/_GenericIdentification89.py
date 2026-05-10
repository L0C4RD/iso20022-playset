from . import base_types
from ._RestrictedFINXMax30Text import RestrictedFINXMax30Text
from ._GenericIdentification47 import GenericIdentification47

class GenericIdentification89(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Id"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax30Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GenericIdentification47, min=1, max=1, mutex_group=None, array=False),
	))

