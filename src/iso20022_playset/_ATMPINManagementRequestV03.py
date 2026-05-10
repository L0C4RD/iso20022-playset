from . import base_types
from ._ATMPINManagementRequest3 import ATMPINManagementRequest3
from ._ContentInformationType10 import ContentInformationType10
from ._ContentInformationType15 import ContentInformationType15
from ._Header31 import Header31

class ATMPINManagementRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ATMPINMgmtReq", "_Hdr", "_PrtctdATMPINMgmtReq", "_SctyTrlr"]
	@property
	def ATMPINMgmtReq(self):
		return self._ATMPINMgmtReq

	@ATMPINMgmtReq.setter
	def ATMPINMgmtReq(self, value):
		self._ATMPINMgmtReq = value if type(value) != base_types.auto else self.make_default("ATMPINMgmtReq")

	@ATMPINMgmtReq.deleter
	def ATMPINMgmtReq(self):
		del self._ATMPINMgmtReq
		self._ATMPINMgmtReq = None

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
	def PrtctdATMPINMgmtReq(self):
		return self._PrtctdATMPINMgmtReq

	@PrtctdATMPINMgmtReq.setter
	def PrtctdATMPINMgmtReq(self, value):
		self._PrtctdATMPINMgmtReq = value if type(value) != base_types.auto else self.make_default("PrtctdATMPINMgmtReq")

	@PrtctdATMPINMgmtReq.deleter
	def PrtctdATMPINMgmtReq(self):
		del self._PrtctdATMPINMgmtReq
		self._PrtctdATMPINMgmtReq = None

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
		base_types.FieldEntry(name='ATMPINMgmtReq', type=ATMPINManagementRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMPINMgmtReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))

