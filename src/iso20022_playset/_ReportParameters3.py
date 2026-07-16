# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyCode
from . import DateAndDateTimeChoice
from . import EventFrequency6Code
from . import Exact5NumericText
from . import ISODateTime
from . import Max35Text

class ReportParameters3(base_types._BaseFieldType):

	__slots__ = ["_ClctnDtAndTm", "_Frqcy", "_RptCcy", "_RptDtAndTm", "_RptId", "_RptNb"]
	@property
	def ClctnDtAndTm(self):
		return self._ClctnDtAndTm

	@ClctnDtAndTm.setter
	def ClctnDtAndTm(self, value):
		self._ClctnDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'ClctnDtAndTm', ISODateTime, False)

	@ClctnDtAndTm.deleter
	def ClctnDtAndTm(self):
		del self._ClctnDtAndTm
		self._ClctnDtAndTm = base_types.UninitialisedField(self, 'ClctnDtAndTm', ISODateTime, False)

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
		self._RptCcy = value if value is not None else base_types.UninitialisedField(self, 'RptCcy', CurrencyCode, False)

	@RptCcy.deleter
	def RptCcy(self):
		del self._RptCcy
		self._RptCcy = base_types.UninitialisedField(self, 'RptCcy', CurrencyCode, False)

	@property
	def RptDtAndTm(self):
		return self._RptDtAndTm

	@RptDtAndTm.setter
	def RptDtAndTm(self, value):
		self._RptDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'RptDtAndTm', DateAndDateTimeChoice, False)

	@RptDtAndTm.deleter
	def RptDtAndTm(self):
		del self._RptDtAndTm
		self._RptDtAndTm = base_types.UninitialisedField(self, 'RptDtAndTm', DateAndDateTimeChoice, False)

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

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if value is not None else base_types.UninitialisedField(self, 'RptNb', Exact5NumericText, False)

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = base_types.UninitialisedField(self, 'RptNb', Exact5NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=EventFrequency6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptCcy', type=CurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtAndTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Exact5NumericText, min=0, max=1, mutex_group=None, array=False),
	))