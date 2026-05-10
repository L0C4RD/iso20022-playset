from . import base_types
import ContentInformationType38
import StatusReport14
import TMSHeader1

class StatusReportV14(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_StsRpt", "_Hdr"]
	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def StsRpt(self):
		return self._StsRpt

	@StsRpt.setter
	def StsRpt(self, value):
		self._StsRpt = value if type(value) != auto else self.make_default("StsRpt")

	@StsRpt.deleter
	def StsRpt(self):
		del self._StsRpt
		self._StsRpt = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRpt', type=StatusReport14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
	))

