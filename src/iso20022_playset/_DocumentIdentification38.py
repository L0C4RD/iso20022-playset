# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification4Choice
from . import DocumentNumber6Choice
from . import ProcessingPosition10Choice

class DocumentIdentification38(base_types._BaseFieldType):

	__slots__ = ["_DocNb", "_Id", "_LkgTp"]
	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if value is not None else base_types.UninitialisedField(self, 'DocNb', DocumentNumber6Choice, False)

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = base_types.UninitialisedField(self, 'DocNb', DocumentNumber6Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DocumentIdentification4Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DocumentIdentification4Choice, False)

	@property
	def LkgTp(self):
		return self._LkgTp

	@LkgTp.setter
	def LkgTp(self, value):
		self._LkgTp = value if value is not None else base_types.UninitialisedField(self, 'LkgTp', ProcessingPosition10Choice, False)

	@LkgTp.deleter
	def LkgTp(self):
		del self._LkgTp
		self._LkgTp = base_types.UninitialisedField(self, 'LkgTp', ProcessingPosition10Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocNb', type=DocumentNumber6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkgTp', type=ProcessingPosition10Choice, min=0, max=1, mutex_group=None, array=False),
	))