# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BaseOne14Rate import BaseOne14Rate
from ._RateType5Code import RateType5Code

class RateFormat12Choice(base_types._BaseFieldType):

	__slots__ = ["_NotSpcfdRate", "_Rate"]
	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if type(value) != base_types.auto else self.make_default("NotSpcfdRate")

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotSpcfdRate', type=RateType5Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=BaseOne14Rate, min=0, max=1, mutex_group=1, array=False),
	))