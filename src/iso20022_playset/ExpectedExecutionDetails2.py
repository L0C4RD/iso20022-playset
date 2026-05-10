import base_types
import ISODate
import DateAndDateTimeChoice

class ExpectedExecutionDetails2(base_types._BaseFieldType):

	__slots__ = ["_XpctdTradDtTm", "_XpctdCshSttlmDt"]
	@property
	def XpctdTradDtTm(self):
		return self._XpctdTradDtTm

	@XpctdTradDtTm.setter
	def XpctdTradDtTm(self, value):
		self._XpctdTradDtTm = value if type(value) != auto else self.make_default("XpctdTradDtTm")

	@XpctdTradDtTm.deleter
	def XpctdTradDtTm(self):
		del self._XpctdTradDtTm
		self._XpctdTradDtTm = None

	@property
	def XpctdCshSttlmDt(self):
		return self._XpctdCshSttlmDt

	@XpctdCshSttlmDt.setter
	def XpctdCshSttlmDt(self, value):
		self._XpctdCshSttlmDt = value if type(value) != auto else self.make_default("XpctdCshSttlmDt")

	@XpctdCshSttlmDt.deleter
	def XpctdCshSttlmDt(self):
		del self._XpctdCshSttlmDt
		self._XpctdCshSttlmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpctdTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

