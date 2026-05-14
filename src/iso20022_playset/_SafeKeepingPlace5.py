# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._SafekeepingPlaceFormat41Choice import SafekeepingPlaceFormat41Choice

class SafeKeepingPlace5(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_SfkpgPlcFrmt"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def SfkpgPlcFrmt(self):
		return self._SfkpgPlcFrmt

	@SfkpgPlcFrmt.setter
	def SfkpgPlcFrmt(self, value):
		self._SfkpgPlcFrmt = value if type(value) != base_types.auto else self.make_default("SfkpgPlcFrmt")

	@SfkpgPlcFrmt.deleter
	def SfkpgPlcFrmt(self):
		del self._SfkpgPlcFrmt
		self._SfkpgPlcFrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlcFrmt', type=SafekeepingPlaceFormat41Choice, min=0, max=1, mutex_group=None, array=False),
	))