from . import base_types
from .DateOrBlankQuery2Choice import DateOrBlankQuery2Choice
from .ISODate import ISODate
from .DatePeriod1 import DatePeriod1
from .DateTimeOrBlankQuery1Choice import DateTimeOrBlankQuery1Choice
from .DateTimePeriod1 import DateTimePeriod1

class TradeDateTimeQueryCriteria6(base_types._BaseFieldType):

	__slots__ = ["_XprtnDt", "_ExctnDtTm", "_ValtnDtTm", "_MtrtyDt", "_CollTmStmp", "_RptgDtTm", "_EarlyTermntnDt", "_HstrclAsOfDt", "_FctvDt"]
	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if type(value) != auto else self.make_default("XprtnDt")

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = None

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if type(value) != auto else self.make_default("ExctnDtTm")

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = None

	@property
	def ValtnDtTm(self):
		return self._ValtnDtTm

	@ValtnDtTm.setter
	def ValtnDtTm(self, value):
		self._ValtnDtTm = value if type(value) != auto else self.make_default("ValtnDtTm")

	@ValtnDtTm.deleter
	def ValtnDtTm(self):
		del self._ValtnDtTm
		self._ValtnDtTm = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def CollTmStmp(self):
		return self._CollTmStmp

	@CollTmStmp.setter
	def CollTmStmp(self, value):
		self._CollTmStmp = value if type(value) != auto else self.make_default("CollTmStmp")

	@CollTmStmp.deleter
	def CollTmStmp(self):
		del self._CollTmStmp
		self._CollTmStmp = None

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if type(value) != auto else self.make_default("RptgDtTm")

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = None

	@property
	def EarlyTermntnDt(self):
		return self._EarlyTermntnDt

	@EarlyTermntnDt.setter
	def EarlyTermntnDt(self, value):
		self._EarlyTermntnDt = value if type(value) != auto else self.make_default("EarlyTermntnDt")

	@EarlyTermntnDt.deleter
	def EarlyTermntnDt(self):
		del self._EarlyTermntnDt
		self._EarlyTermntnDt = None

	@property
	def HstrclAsOfDt(self):
		return self._HstrclAsOfDt

	@HstrclAsOfDt.setter
	def HstrclAsOfDt(self, value):
		self._HstrclAsOfDt = value if type(value) != auto else self.make_default("HstrclAsOfDt")

	@HstrclAsOfDt.deleter
	def HstrclAsOfDt(self):
		del self._HstrclAsOfDt
		self._HstrclAsOfDt = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XprtnDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTmStmp', type=DateTimeOrBlankQuery1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyTermntnDt', type=DatePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstrclAsOfDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DatePeriod1, min=0, max=1, mutex_group=None, array=False),
	))

