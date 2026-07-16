# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import DateAndDateTime2Choice
from . import EventFrequency6Code
from . import ISODateTime
from . import Max35Text

class ReportParameters6(base_types._BaseFieldType):

	__slots__ = ["_ClctnDt", "_Frqcy", "_RptCcy", "_RptDtAndTm", "_RptId"]
	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if value is not None else base_types.UninitialisedField(self, 'ClctnDt', ISODateTime, False)

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = base_types.UninitialisedField(self, 'ClctnDt', ISODateTime, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', EventFrequency6Code, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', EventFrequency6Code, False)

	@property
	def RptCcy(self):
		return self._RptCcy

	@RptCcy.setter
	def RptCcy(self, value):
		self._RptCcy = value if value is not None else base_types.UninitialisedField(self, 'RptCcy', ActiveCurrencyCode, False)

	@RptCcy.deleter
	def RptCcy(self):
		del self._RptCcy
		self._RptCcy = base_types.UninitialisedField(self, 'RptCcy', ActiveCurrencyCode, False)

	@property
	def RptDtAndTm(self):
		return self._RptDtAndTm

	@RptDtAndTm.setter
	def RptDtAndTm(self, value):
		self._RptDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'RptDtAndTm', DateAndDateTime2Choice, False)

	@RptDtAndTm.deleter
	def RptDtAndTm(self):
		del self._RptDtAndTm
		self._RptDtAndTm = base_types.UninitialisedField(self, 'RptDtAndTm', DateAndDateTime2Choice, False)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=EventFrequency6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtAndTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))