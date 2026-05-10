from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .Max35Text import Max35Text

class ReportParameters8(base_types._BaseFieldType):

	__slots__ = ["_RptId", "_RptDtAndTm"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtAndTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))

