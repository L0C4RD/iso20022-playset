# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PercentageRate import PercentageRate

class ComparePercentageRate3(base_types._BaseFieldType):

	__slots__ = ["_Val1", "_Val2"]
	@property
	def Val1(self):
		return self._Val1

	@Val1.setter
	def Val1(self, value):
		self._Val1 = value if type(value) != base_types.auto else self.make_default("Val1")

	@Val1.deleter
	def Val1(self):
		del self._Val1
		self._Val1 = None

	@property
	def Val2(self):
		return self._Val2

	@Val2.setter
	def Val2(self, value):
		self._Val2 = value if type(value) != base_types.auto else self.make_default("Val2")

	@Val2.deleter
	def Val2(self):
		del self._Val2
		self._Val2 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val1', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val2', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))