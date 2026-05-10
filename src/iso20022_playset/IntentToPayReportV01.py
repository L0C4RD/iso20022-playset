from . import base_types
from .MessageIdentification1 import MessageIdentification1
from .ReportLine1 import ReportLine1

class IntentToPayReportV01(base_types._BaseFieldType):

	__slots__ = ["_RptdItms", "_RptId"]
	@property
	def RptdItms(self):
		return self._RptdItms

	@RptdItms.setter
	def RptdItms(self, value):
		self._RptdItms = value if type(value) != auto else self.make_default("RptdItms")

	@RptdItms.deleter
	def RptdItms(self):
		del self._RptdItms
		self._RptdItms = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptdItms', type=ReportLine1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

