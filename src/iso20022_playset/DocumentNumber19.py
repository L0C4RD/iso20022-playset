from . import base_types
import DocumentNumber6Choice
import Identification29

class DocumentNumber19(base_types._BaseFieldType):

	__slots__ = ["_Refs", "_Nb"]
	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

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
		base_types.FieldEntry(name='Refs', type=Identification29, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nb', type=DocumentNumber6Choice, min=1, max=1, mutex_group=None, array=False),
	))

