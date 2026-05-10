from . import base_types
from .TMSHeader1 import TMSHeader1
from .ContentInformationType38 import ContentInformationType38
from .MaintenanceDelegationResponse8 import MaintenanceDelegationResponse8

class MaintenanceDelegationResponseV08(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_MntncDlgtnRspn"]
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
	def MntncDlgtnRspn(self):
		return self._MntncDlgtnRspn

	@MntncDlgtnRspn.setter
	def MntncDlgtnRspn(self, value):
		self._MntncDlgtnRspn = value if type(value) != auto else self.make_default("MntncDlgtnRspn")

	@MntncDlgtnRspn.deleter
	def MntncDlgtnRspn(self):
		del self._MntncDlgtnRspn
		self._MntncDlgtnRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncDlgtnRspn', type=MaintenanceDelegationResponse8, min=1, max=1, mutex_group=None, array=False),
	))

