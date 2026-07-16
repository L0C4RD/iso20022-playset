# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Number

class ManifestData2(base_types._BaseFieldType):

	__slots__ = ["_DocTp", "_NbOfDocs"]
	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if value is not None else base_types.UninitialisedField(self, 'DocTp', Max35Text, False)

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = base_types.UninitialisedField(self, 'DocTp', Max35Text, False)

	@property
	def NbOfDocs(self):
		return self._NbOfDocs

	@NbOfDocs.setter
	def NbOfDocs(self, value):
		self._NbOfDocs = value if value is not None else base_types.UninitialisedField(self, 'NbOfDocs', Number, False)

	@NbOfDocs.deleter
	def NbOfDocs(self):
		del self._NbOfDocs
		self._NbOfDocs = base_types.UninitialisedField(self, 'NbOfDocs', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocTp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDocs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))