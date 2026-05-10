from . import base_types
from ._ContentInformationType38 import ContentInformationType38
from ._Header41 import Header41
from ._ReportResponse8 import ReportResponse8

class SaleToPOIReportResponseV07(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_RptRspn", "_SctyTrlr"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def RptRspn(self):
		return self._RptRspn

	@RptRspn.setter
	def RptRspn(self, value):
		self._RptRspn = value if type(value) != base_types.auto else self.make_default("RptRspn")

	@RptRspn.deleter
	def RptRspn(self):
		del self._RptRspn
		self._RptRspn = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptRspn', type=ReportResponse8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))

