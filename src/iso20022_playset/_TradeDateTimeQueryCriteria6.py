# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateOrBlankQuery2Choice
from . import DatePeriod1
from . import DateTimeOrBlankQuery1Choice
from . import DateTimePeriod1
from . import ISODate

class TradeDateTimeQueryCriteria6(base_types._BaseFieldType):

	__slots__ = ["_CollTmStmp", "_EarlyTermntnDt", "_ExctnDtTm", "_FctvDt", "_HstrclAsOfDt", "_MtrtyDt", "_RptgDtTm", "_ValtnDtTm", "_XprtnDt"]
	@property
	def CollTmStmp(self):
		return self._CollTmStmp

	@CollTmStmp.setter
	def CollTmStmp(self, value):
		self._CollTmStmp = value if value is not None else base_types.UninitialisedField(self, 'CollTmStmp', DateTimeOrBlankQuery1Choice, False)

	@CollTmStmp.deleter
	def CollTmStmp(self):
		del self._CollTmStmp
		self._CollTmStmp = base_types.UninitialisedField(self, 'CollTmStmp', DateTimeOrBlankQuery1Choice, False)

	@property
	def EarlyTermntnDt(self):
		return self._EarlyTermntnDt

	@EarlyTermntnDt.setter
	def EarlyTermntnDt(self, value):
		self._EarlyTermntnDt = value if value is not None else base_types.UninitialisedField(self, 'EarlyTermntnDt', DatePeriod1, False)

	@EarlyTermntnDt.deleter
	def EarlyTermntnDt(self):
		del self._EarlyTermntnDt
		self._EarlyTermntnDt = base_types.UninitialisedField(self, 'EarlyTermntnDt', DatePeriod1, False)

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ExctnDtTm', DateTimePeriod1, False)

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = base_types.UninitialisedField(self, 'ExctnDtTm', DateTimePeriod1, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', DatePeriod1, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', DatePeriod1, False)

	@property
	def HstrclAsOfDt(self):
		return self._HstrclAsOfDt

	@HstrclAsOfDt.setter
	def HstrclAsOfDt(self, value):
		self._HstrclAsOfDt = value if value is not None else base_types.UninitialisedField(self, 'HstrclAsOfDt', ISODate, False)

	@HstrclAsOfDt.deleter
	def HstrclAsOfDt(self):
		del self._HstrclAsOfDt
		self._HstrclAsOfDt = base_types.UninitialisedField(self, 'HstrclAsOfDt', ISODate, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', DateOrBlankQuery2Choice, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', DateOrBlankQuery2Choice, False)

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if value is not None else base_types.UninitialisedField(self, 'RptgDtTm', DateTimePeriod1, False)

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = base_types.UninitialisedField(self, 'RptgDtTm', DateTimePeriod1, False)

	@property
	def ValtnDtTm(self):
		return self._ValtnDtTm

	@ValtnDtTm.setter
	def ValtnDtTm(self, value):
		self._ValtnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ValtnDtTm', DateTimePeriod1, False)

	@ValtnDtTm.deleter
	def ValtnDtTm(self):
		del self._ValtnDtTm
		self._ValtnDtTm = base_types.UninitialisedField(self, 'ValtnDtTm', DateTimePeriod1, False)

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if value is not None else base_types.UninitialisedField(self, 'XprtnDt', DateOrBlankQuery2Choice, False)

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = base_types.UninitialisedField(self, 'XprtnDt', DateOrBlankQuery2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollTmStmp', type=DateTimeOrBlankQuery1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyTermntnDt', type=DatePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=DatePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstrclAsOfDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
	))