from . import base_types
from .DocumentIdentification4Choice import DocumentIdentification4Choice
from .DocumentNumber6Choice import DocumentNumber6Choice
from .ProcessingPosition10Choice import ProcessingPosition10Choice

class DocumentIdentification38(base_types._BaseFieldType):

	__slots__ = ["_DocNb", "_Id", "_LkgTp"]
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

	@property
	def LkgTp(self):
		return self._LkgTp

	@LkgTp.setter
	def LkgTp(self, value):
		self._LkgTp = value if type(value) != base_types.auto else self.make_default("LkgTp")

	@LkgTp.deleter
	def LkgTp(self):
		del self._LkgTp
		self._LkgTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocNb', type=DocumentNumber6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkgTp', type=ProcessingPosition10Choice, min=0, max=1, mutex_group=None, array=False),
	))

