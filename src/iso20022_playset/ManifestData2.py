import base_types
import Max35Text
import Number

class ManifestData2(base_types._BaseFieldType):

	__slots__ = ["_NbOfDocs", "_DocTp"]
	@property
	def NbOfDocs(self):
		return self._NbOfDocs

	@NbOfDocs.setter
	def NbOfDocs(self, value):
		self._NbOfDocs = value if type(value) != auto else self.make_default("NbOfDocs")

	@NbOfDocs.deleter
	def NbOfDocs(self):
		del self._NbOfDocs
		self._NbOfDocs = None

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if type(value) != auto else self.make_default("DocTp")

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfDocs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocTp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

