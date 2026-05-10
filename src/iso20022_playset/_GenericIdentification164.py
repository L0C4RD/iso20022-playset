from . import base_types
from ._Max35Text import Max35Text
from ._OtherIdentification3Choice import OtherIdentification3Choice

class GenericIdentification164(base_types._BaseFieldType):

	__slots__ = ["_IdTp", "_Issr", "_Id"]
	@property
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if type(value) != base_types.auto else self.make_default("IdTp")

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdTp', type=OtherIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

