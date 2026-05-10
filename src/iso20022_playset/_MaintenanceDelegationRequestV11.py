from . import base_types
from ._ContentInformationType38 import ContentInformationType38
from ._MaintenanceDelegationRequest11 import MaintenanceDelegationRequest11
from ._TMSHeader1 import TMSHeader1

class MaintenanceDelegationRequestV11(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_MntncDlgtnReq", "_SctyTrlr"]
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
	def MntncDlgtnReq(self):
		return self._MntncDlgtnReq

	@MntncDlgtnReq.setter
	def MntncDlgtnReq(self, value):
		self._MntncDlgtnReq = value if type(value) != base_types.auto else self.make_default("MntncDlgtnReq")

	@MntncDlgtnReq.deleter
	def MntncDlgtnReq(self):
		del self._MntncDlgtnReq
		self._MntncDlgtnReq = None

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
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncDlgtnReq', type=MaintenanceDelegationRequest11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=1, max=1, mutex_group=None, array=False),
	))

