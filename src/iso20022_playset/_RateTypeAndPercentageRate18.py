# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Percentage14Rate import Percentage14Rate
from ._RateType46Choice import RateType46Choice

class RateTypeAndPercentageRate18(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_RateTp"]
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

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType46Choice, min=1, max=1, mutex_group=None, array=False),
	))