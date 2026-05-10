from . import base_types
import Identification30
import DocumentNumber5Choice

class DocumentNumber20(base_types._BaseFieldType):

	__slots__ = ["_Nb", "_Refs"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=DocumentNumber5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Identification30, min=1, max=None, mutex_group=None, array=True),
	))

