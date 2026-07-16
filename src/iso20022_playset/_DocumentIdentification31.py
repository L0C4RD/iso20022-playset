# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ProcessingPosition7Choice

class DocumentIdentification31(base_types._BaseFieldType):

	__slots__ = ["_Id", "_LkgTp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def LkgTp(self):
		return self._LkgTp

	@LkgTp.setter
	def LkgTp(self, value):
		self._LkgTp = value if value is not None else base_types.UninitialisedField(self, 'LkgTp', ProcessingPosition7Choice, False)

	@LkgTp.deleter
	def LkgTp(self):
		del self._LkgTp
		self._LkgTp = base_types.UninitialisedField(self, 'LkgTp', ProcessingPosition7Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkgTp', type=ProcessingPosition7Choice, min=0, max=1, mutex_group=None, array=False),
	))