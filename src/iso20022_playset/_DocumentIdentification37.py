# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProcessingPosition10Choice
from . import RestrictedFINXMax16Text

class DocumentIdentification37(base_types._BaseFieldType):

	__slots__ = ["_Id", "_LkgTp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', RestrictedFINXMax16Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', RestrictedFINXMax16Text, False)

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
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkgTp', type=ProcessingPosition10Choice, min=0, max=1, mutex_group=None, array=False),
	))