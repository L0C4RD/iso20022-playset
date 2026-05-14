from . import base_types
from ._ContentInformationType38 import ContentInformationType38
from ._StatusReport15 import StatusReport15
from ._TMSHeader1 import TMSHeader1

class StatusReportV15(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_StsRpt"]
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
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def StsRpt(self):
		return self._StsRpt

	@StsRpt.setter
	def StsRpt(self, value):
		self._StsRpt = value if type(value) != base_types.auto else self.make_default("StsRpt")

	@StsRpt.deleter
	def StsRpt(self):
		del self._StsRpt
		self._StsRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRpt', type=StatusReport15, min=1, max=1, mutex_group=None, array=False),
	))

