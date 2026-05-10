from . import base_types
from .DocumentNumber6Choice import DocumentNumber6Choice

class DocumentNumber14(base_types._BaseFieldType):

	__slots__ = ["_Nb"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=DocumentNumber6Choice, min=1, max=1, mutex_group=None, array=False),
	))

