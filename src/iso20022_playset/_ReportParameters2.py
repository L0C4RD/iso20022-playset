from . import base_types
from ._CurrencyCode import CurrencyCode
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._EventFrequency6Code import EventFrequency6Code
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text

class ReportParameters2(base_types._BaseFieldType):

	__slots__ = ["_ClctnDt", "_Frqcy", "_RptCcy", "_RptDtAndTm", "_RptId"]
	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if type(value) != base_types.auto else self.make_default("ClctnDt")

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def RptCcy(self):
		return self._RptCcy

	@RptCcy.setter
	def RptCcy(self, value):
		self._RptCcy = value if type(value) != base_types.auto else self.make_default("RptCcy")

	@RptCcy.deleter
	def RptCcy(self):
		del self._RptCcy
		self._RptCcy = None

	@property
	def RptDtAndTm(self):
		return self._RptDtAndTm

	@RptDtAndTm.setter
	def RptDtAndTm(self, value):
		self._RptDtAndTm = value if type(value) != base_types.auto else self.make_default("RptDtAndTm")

	@RptDtAndTm.deleter
	def RptDtAndTm(self):
		del self._RptDtAndTm
		self._RptDtAndTm = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != base_types.auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=EventFrequency6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptCcy', type=CurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtAndTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

