from . import base_types
from ._DateOrBlankQuery2Choice import DateOrBlankQuery2Choice
from ._DateTimePeriod1 import DateTimePeriod1

class TradeDateTimeQueryCriteria2(base_types._BaseFieldType):

	__slots__ = ["_TermntnDt", "_MtrtyDt", "_ExctnDtTm", "_RptgDtTm"]
	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if type(value) != base_types.auto else self.make_default("ExctnDtTm")

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if type(value) != base_types.auto else self.make_default("RptgDtTm")

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != base_types.auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExctnDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
	))

