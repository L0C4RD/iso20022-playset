from . import base_types
from ._Max35Text import Max35Text
from ._IdentificationSource1Choice import IdentificationSource1Choice

class AlternateIdentification1(base_types._BaseFieldType):

	__slots__ = ["_IdSrc", "_Id"]
	@property
	def IdSrc(self):
		return self._IdSrc

	@IdSrc.setter
	def IdSrc(self, value):
		self._IdSrc = value if type(value) != base_types.auto else self.make_default("IdSrc")

	@IdSrc.deleter
	def IdSrc(self):
		del self._IdSrc
		self._IdSrc = None

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
		base_types.FieldEntry(name='IdSrc', type=IdentificationSource1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

