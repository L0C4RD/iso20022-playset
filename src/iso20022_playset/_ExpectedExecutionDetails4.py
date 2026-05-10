from . import base_types
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._ISODate import ISODate

class ExpectedExecutionDetails4(base_types._BaseFieldType):

	__slots__ = ["_XpctdTradDtTm", "_XpctdCshSttlmDt"]
	@property
	def XpctdCshSttlmDt(self):
		return self._XpctdCshSttlmDt

	@XpctdCshSttlmDt.setter
	def XpctdCshSttlmDt(self, value):
		self._XpctdCshSttlmDt = value if type(value) != base_types.auto else self.make_default("XpctdCshSttlmDt")

	@XpctdCshSttlmDt.deleter
	def XpctdCshSttlmDt(self):
		del self._XpctdCshSttlmDt
		self._XpctdCshSttlmDt = None

	@property
	def XpctdTradDtTm(self):
		return self._XpctdTradDtTm

	@XpctdTradDtTm.setter
	def XpctdTradDtTm(self, value):
		self._XpctdTradDtTm = value if type(value) != base_types.auto else self.make_default("XpctdTradDtTm")

	@XpctdTradDtTm.deleter
	def XpctdTradDtTm(self):
		del self._XpctdTradDtTm
		self._XpctdTradDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpctdCshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
	))

