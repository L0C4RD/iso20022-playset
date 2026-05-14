# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RestrictedFINXMax30Text import RestrictedFINXMax30Text
from ._SafekeepingPlace3Code import SafekeepingPlace3Code

class SafekeepingPlaceTypeAndText15(base_types._BaseFieldType):

	__slots__ = ["_Id", "_SfkpgPlcTp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def SfkpgPlcTp(self):
		return self._SfkpgPlcTp

	@SfkpgPlcTp.setter
	def SfkpgPlcTp(self, value):
		self._SfkpgPlcTp = value if type(value) != base_types.auto else self.make_default("SfkpgPlcTp")

	@SfkpgPlcTp.deleter
	def SfkpgPlcTp(self):
		del self._SfkpgPlcTp
		self._SfkpgPlcTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax30Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlcTp', type=SafekeepingPlace3Code, min=1, max=1, mutex_group=None, array=False),
	))