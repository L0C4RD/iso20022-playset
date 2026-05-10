from . import base_types
from ._ContentInformationType10 import ContentInformationType10
from ._Header31 import Header31
from ._ContentInformationType15 import ContentInformationType15
from ._ATMDepositRequest2 import ATMDepositRequest2

class ATMDepositRequestV02(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_ATMDpstReq", "_PrtctdATMDpstReq"]
	@property
	def ATMDpstReq(self):
		return self._ATMDpstReq

	@ATMDpstReq.setter
	def ATMDpstReq(self, value):
		self._ATMDpstReq = value if type(value) != base_types.auto else self.make_default("ATMDpstReq")

	@ATMDpstReq.deleter
	def ATMDpstReq(self):
		del self._ATMDpstReq
		self._ATMDpstReq = None

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
	def PrtctdATMDpstReq(self):
		return self._PrtctdATMDpstReq

	@PrtctdATMDpstReq.setter
	def PrtctdATMDpstReq(self, value):
		self._PrtctdATMDpstReq = value if type(value) != base_types.auto else self.make_default("PrtctdATMDpstReq")

	@PrtctdATMDpstReq.deleter
	def PrtctdATMDpstReq(self):
		del self._PrtctdATMDpstReq
		self._PrtctdATMDpstReq = None

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
		base_types.FieldEntry(name='ATMDpstReq', type=ATMDepositRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))

