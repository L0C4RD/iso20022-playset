from . import base_types
from ._Max35Text import Max35Text
from ._Max16Text import Max16Text
from ._IdentificationSource3Choice import IdentificationSource3Choice

class OtherIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Sfx", "_Id", "_Tp"]
	@property
	def Sfx(self):
		return self._Sfx

	@Sfx.setter
	def Sfx(self, value):
		self._Sfx = value if type(value) != base_types.auto else self.make_default("Sfx")

	@Sfx.deleter
	def Sfx(self):
		del self._Sfx
		self._Sfx = None

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
		base_types.FieldEntry(name='Sfx', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=IdentificationSource3Choice, min=1, max=1, mutex_group=None, array=False),
	))

