# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OwnershipType3Choice
from . import PercentageRate

class Ownership1(base_types._BaseFieldType):

	__slots__ = ["_OwnrshPctg", "_OwnrshTp", "_UsfrctPctg"]
	@property
	def OwnrshPctg(self):
		return self._OwnrshPctg

	@OwnrshPctg.setter
	def OwnrshPctg(self, value):
		self._OwnrshPctg = value if value is not None else base_types.UninitialisedField(self, 'OwnrshPctg', PercentageRate, False)

	@OwnrshPctg.deleter
	def OwnrshPctg(self):
		del self._OwnrshPctg
		self._OwnrshPctg = base_types.UninitialisedField(self, 'OwnrshPctg', PercentageRate, False)

	@property
	def OwnrshTp(self):
		return self._OwnrshTp

	@OwnrshTp.setter
	def OwnrshTp(self, value):
		self._OwnrshTp = value if value is not None else base_types.UninitialisedField(self, 'OwnrshTp', OwnershipType3Choice, False)

	@OwnrshTp.deleter
	def OwnrshTp(self):
		del self._OwnrshTp
		self._OwnrshTp = base_types.UninitialisedField(self, 'OwnrshTp', OwnershipType3Choice, False)

	@property
	def UsfrctPctg(self):
		return self._UsfrctPctg

	@UsfrctPctg.setter
	def UsfrctPctg(self, value):
		self._UsfrctPctg = value if value is not None else base_types.UninitialisedField(self, 'UsfrctPctg', PercentageRate, False)

	@UsfrctPctg.deleter
	def UsfrctPctg(self):
		del self._UsfrctPctg
		self._UsfrctPctg = base_types.UninitialisedField(self, 'UsfrctPctg', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OwnrshPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrshTp', type=OwnershipType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsfrctPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))