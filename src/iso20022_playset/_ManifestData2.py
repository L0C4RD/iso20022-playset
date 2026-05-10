from . import base_types
from ._Number import Number
from ._Max35Text import Max35Text

class ManifestData2(base_types._BaseFieldType):

	__slots__ = ["_DocTp", "_NbOfDocs"]
	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if type(value) != base_types.auto else self.make_default("DocTp")

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = None

	@property
	def NbOfDocs(self):
		return self._NbOfDocs

	@NbOfDocs.setter
	def NbOfDocs(self, value):
		self._NbOfDocs = value if type(value) != base_types.auto else self.make_default("NbOfDocs")

	@NbOfDocs.deleter
	def NbOfDocs(self):
		del self._NbOfDocs
		self._NbOfDocs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocTp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDocs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

