from . import base_types
from .DocumentIdentification4Choice import DocumentIdentification4Choice
from .DocumentNumber6Choice import DocumentNumber6Choice

class DocumentIdentification34(base_types._BaseFieldType):

	__slots__ = ["_DocNb", "_Id"]
	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if type(value) != base_types.auto else self.make_default("DocNb")

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = None

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
		base_types.FieldEntry(name='DocNb', type=DocumentNumber6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
	))

