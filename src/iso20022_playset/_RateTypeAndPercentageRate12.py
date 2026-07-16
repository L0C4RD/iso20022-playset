# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Percentage14Rate
from . import RateType42Choice

class RateTypeAndPercentageRate12(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_RateTp"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', Percentage14Rate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', Percentage14Rate, False)

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', RateType42Choice, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', RateType42Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType42Choice, min=1, max=1, mutex_group=None, array=False),
	))