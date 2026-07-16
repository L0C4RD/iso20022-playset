# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BaseOneRate
from . import DecimalNumber

class ForeignExchange1(base_types._BaseFieldType):

	__slots__ = ["_FrgnCcy", "_XchgFwdPt", "_XchgSpotRate"]
	@property
	def FrgnCcy(self):
		return self._FrgnCcy

	@FrgnCcy.setter
	def FrgnCcy(self, value):
		self._FrgnCcy = value if value is not None else base_types.UninitialisedField(self, 'FrgnCcy', ActiveOrHistoricCurrencyCode, False)

	@FrgnCcy.deleter
	def FrgnCcy(self):
		del self._FrgnCcy
		self._FrgnCcy = base_types.UninitialisedField(self, 'FrgnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def XchgFwdPt(self):
		return self._XchgFwdPt

	@XchgFwdPt.setter
	def XchgFwdPt(self, value):
		self._XchgFwdPt = value if value is not None else base_types.UninitialisedField(self, 'XchgFwdPt', DecimalNumber, False)

	@XchgFwdPt.deleter
	def XchgFwdPt(self):
		del self._XchgFwdPt
		self._XchgFwdPt = base_types.UninitialisedField(self, 'XchgFwdPt', DecimalNumber, False)

	@property
	def XchgSpotRate(self):
		return self._XchgSpotRate

	@XchgSpotRate.setter
	def XchgSpotRate(self, value):
		self._XchgSpotRate = value if value is not None else base_types.UninitialisedField(self, 'XchgSpotRate', BaseOneRate, False)

	@XchgSpotRate.deleter
	def XchgSpotRate(self):
		del self._XchgSpotRate
		self._XchgSpotRate = base_types.UninitialisedField(self, 'XchgSpotRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrgnCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgFwdPt', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgSpotRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))