from . import base_types
from ._DocumentNumber5Choice import DocumentNumber5Choice

class DocumentNumber13(base_types._BaseFieldType):

	__slots__ = ["_Nb"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=DocumentNumber5Choice, min=1, max=1, mutex_group=None, array=False),
	))

