# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Rate2 import Rate2
from ._RateName1 import RateName1

class RateOrName1Choice(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_RateNm"]
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
	def RateNm(self):
		return self._RateNm

	@RateNm.setter
	def RateNm(self, value):
		self._RateNm = value if type(value) != base_types.auto else self.make_default("RateNm")

	@RateNm.deleter
	def RateNm(self):
		del self._RateNm
		self._RateNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=Rate2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateNm', type=RateName1, min=0, max=1, mutex_group=1, array=False),
	))