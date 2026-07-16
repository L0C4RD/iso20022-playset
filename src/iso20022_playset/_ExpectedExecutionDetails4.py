# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeChoice
from . import ISODate

class ExpectedExecutionDetails4(base_types._BaseFieldType):

	__slots__ = ["_XpctdCshSttlmDt", "_XpctdTradDtTm"]
	@property
	def XpctdCshSttlmDt(self):
		return self._XpctdCshSttlmDt

	@XpctdCshSttlmDt.setter
	def XpctdCshSttlmDt(self, value):
		self._XpctdCshSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdCshSttlmDt', ISODate, False)

	@XpctdCshSttlmDt.deleter
	def XpctdCshSttlmDt(self):
		del self._XpctdCshSttlmDt
		self._XpctdCshSttlmDt = base_types.UninitialisedField(self, 'XpctdCshSttlmDt', ISODate, False)

	@property
	def XpctdTradDtTm(self):
		return self._XpctdTradDtTm

	@XpctdTradDtTm.setter
	def XpctdTradDtTm(self, value):
		self._XpctdTradDtTm = value if value is not None else base_types.UninitialisedField(self, 'XpctdTradDtTm', DateAndDateTimeChoice, False)

	@XpctdTradDtTm.deleter
	def XpctdTradDtTm(self):
		del self._XpctdTradDtTm
		self._XpctdTradDtTm = base_types.UninitialisedField(self, 'XpctdTradDtTm', DateAndDateTimeChoice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpctdCshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
	))