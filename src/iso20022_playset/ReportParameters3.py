import base_types
import DateAndDateTimeChoice
import ISODateTime
import EventFrequency6Code
import Max35Text
import CurrencyCode
import Exact5NumericText

class ReportParameters3(base_types._BaseFieldType):

	__slots__ = ["_RptCcy", "_RptNb", "_Frqcy", "_RptId", "_ClctnDtAndTm", "_RptDtAndTm"]
	@property
	def RptCcy(self):
		return self._RptCcy

	@RptCcy.setter
	def RptCcy(self, value):
		self._RptCcy = value if type(value) != auto else self.make_default("RptCcy")

	@RptCcy.deleter
	def RptCcy(self):
		del self._RptCcy
		self._RptCcy = None

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if type(value) != auto else self.make_default("RptNb")

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def ClctnDtAndTm(self):
		return self._ClctnDtAndTm

	@ClctnDtAndTm.setter
	def ClctnDtAndTm(self, value):
		self._ClctnDtAndTm = value if type(value) != auto else self.make_default("ClctnDtAndTm")

	@ClctnDtAndTm.deleter
	def ClctnDtAndTm(self):
		del self._ClctnDtAndTm
		self._ClctnDtAndTm = None

	@property
	def RptDtAndTm(self):
		return self._RptDtAndTm

	@RptDtAndTm.setter
	def RptDtAndTm(self, value):
		self._RptDtAndTm = value if type(value) != auto else self.make_default("RptDtAndTm")

	@RptDtAndTm.deleter
	def RptDtAndTm(self):
		del self._RptDtAndTm
		self._RptDtAndTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptCcy', type=CurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Exact5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=EventFrequency6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtAndTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
	))

