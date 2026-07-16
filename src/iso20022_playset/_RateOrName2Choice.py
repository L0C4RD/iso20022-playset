# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Rate2
from . import RateName2

class RateOrName2Choice(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_RateNm"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', Rate2, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', Rate2, False)

	@property
	def RateNm(self):
		return self._RateNm

	@RateNm.setter
	def RateNm(self, value):
		self._RateNm = value if value is not None else base_types.UninitialisedField(self, 'RateNm', RateName2, False)

	@RateNm.deleter
	def RateNm(self):
		del self._RateNm
		self._RateNm = base_types.UninitialisedField(self, 'RateNm', RateName2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=Rate2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateNm', type=RateName2, min=0, max=1, mutex_group=1, array=False),
	))