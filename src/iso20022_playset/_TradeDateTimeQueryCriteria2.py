# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateOrBlankQuery2Choice
from . import DateTimePeriod1

class TradeDateTimeQueryCriteria2(base_types._BaseFieldType):

	__slots__ = ["_ExctnDtTm", "_MtrtyDt", "_RptgDtTm", "_TermntnDt"]
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
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', DateOrBlankQuery2Choice, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', DateOrBlankQuery2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExctnDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=DateOrBlankQuery2Choice, min=0, max=1, mutex_group=None, array=False),
	))