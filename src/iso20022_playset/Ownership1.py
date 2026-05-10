from . import base_types
from .PercentageRate import PercentageRate
from .OwnershipType3Choice import OwnershipType3Choice

class Ownership1(base_types._BaseFieldType):

	__slots__ = ["_UsfrctPctg", "_OwnrshPctg", "_OwnrshTp"]
	@property
	def UsfrctPctg(self):
		return self._UsfrctPctg

	@UsfrctPctg.setter
	def UsfrctPctg(self, value):
		self._UsfrctPctg = value if type(value) != auto else self.make_default("UsfrctPctg")

	@UsfrctPctg.deleter
	def UsfrctPctg(self):
		del self._UsfrctPctg
		self._UsfrctPctg = None

	@property
	def OwnrshPctg(self):
		return self._OwnrshPctg

	@OwnrshPctg.setter
	def OwnrshPctg(self, value):
		self._OwnrshPctg = value if type(value) != auto else self.make_default("OwnrshPctg")

	@OwnrshPctg.deleter
	def OwnrshPctg(self):
		del self._OwnrshPctg
		self._OwnrshPctg = None

	@property
	def OwnrshTp(self):
		return self._OwnrshTp

	@OwnrshTp.setter
	def OwnrshTp(self, value):
		self._OwnrshTp = value if type(value) != auto else self.make_default("OwnrshTp")

	@OwnrshTp.deleter
	def OwnrshTp(self):
		del self._OwnrshTp
		self._OwnrshTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UsfrctPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrshPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrshTp', type=OwnershipType3Choice, min=0, max=1, mutex_group=None, array=False),
	))

