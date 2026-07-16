# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import ExchangeRateType1Code
from . import Max35Text

class ExchangeRateInformation1(base_types._BaseFieldType):

	__slots__ = ["_CtrctId", "_RateTp", "_XchgRate"]
	@property
	def CtrctId(self):
		return self._CtrctId

	@CtrctId.setter
	def CtrctId(self, value):
		self._CtrctId = value if value is not None else base_types.UninitialisedField(self, 'CtrctId', Max35Text, False)

	@CtrctId.deleter
	def CtrctId(self):
		del self._CtrctId
		self._CtrctId = base_types.UninitialisedField(self, 'CtrctId', Max35Text, False)

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', ExchangeRateType1Code, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', ExchangeRateType1Code, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=ExchangeRateType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))