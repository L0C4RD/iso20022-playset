# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification3Choice
from . import DocumentNumber5Choice

class DocumentIdentification33(base_types._BaseFieldType):

	__slots__ = ["_DocNb", "_Id"]
	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if value is not None else base_types.UninitialisedField(self, 'DocNb', DocumentNumber5Choice, False)

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = base_types.UninitialisedField(self, 'DocNb', DocumentNumber5Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DocumentIdentification3Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DocumentIdentification3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocNb', type=DocumentNumber5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
	))