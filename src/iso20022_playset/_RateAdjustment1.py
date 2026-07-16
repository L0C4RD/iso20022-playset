# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import PercentageRate

class RateAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_AdjstmntDt", "_Rate"]
	@property
	def AdjstmntDt(self):
		return self._AdjstmntDt

	@AdjstmntDt.setter
	def AdjstmntDt(self, value):
		self._AdjstmntDt = value if value is not None else base_types.UninitialisedField(self, 'AdjstmntDt', ISODate, False)

	@AdjstmntDt.deleter
	def AdjstmntDt(self):
		del self._AdjstmntDt
		self._AdjstmntDt = base_types.UninitialisedField(self, 'AdjstmntDt', ISODate, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstmntDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))