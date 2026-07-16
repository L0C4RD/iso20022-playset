# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICIdentifier
from . import SafekeepingPlace1Code

class SafekeepingPlaceTypeAndAnyBICIdentifier1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_SfkpgPlcTp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', AnyBICIdentifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', AnyBICIdentifier, False)

	@property
	def SfkpgPlcTp(self):
		return self._SfkpgPlcTp

	@SfkpgPlcTp.setter
	def SfkpgPlcTp(self, value):
		self._SfkpgPlcTp = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlcTp', SafekeepingPlace1Code, False)

	@SfkpgPlcTp.deleter
	def SfkpgPlcTp(self):
		del self._SfkpgPlcTp
		self._SfkpgPlcTp = base_types.UninitialisedField(self, 'SfkpgPlcTp', SafekeepingPlace1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=AnyBICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlcTp', type=SafekeepingPlace1Code, min=1, max=1, mutex_group=None, array=False),
	))