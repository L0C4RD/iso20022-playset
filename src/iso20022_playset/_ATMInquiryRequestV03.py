from . import base_types
from ._ContentInformationType10 import ContentInformationType10
from ._ContentInformationType15 import ContentInformationType15
from ._Header31 import Header31
from ._ATMInquiryRequest3 import ATMInquiryRequest3

class ATMInquiryRequestV03(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMNqryReq", "_Hdr", "_SctyTrlr", "_ATMNqryReq"]
	@property
	def PrtctdATMNqryReq(self):
		return self._PrtctdATMNqryReq

	@PrtctdATMNqryReq.setter
	def PrtctdATMNqryReq(self, value):
		self._PrtctdATMNqryReq = value if type(value) != base_types.auto else self.make_default("PrtctdATMNqryReq")

	@PrtctdATMNqryReq.deleter
	def PrtctdATMNqryReq(self):
		del self._PrtctdATMNqryReq
		self._PrtctdATMNqryReq = None

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
	def ATMNqryReq(self):
		return self._ATMNqryReq

	@ATMNqryReq.setter
	def ATMNqryReq(self, value):
		self._ATMNqryReq = value if type(value) != base_types.auto else self.make_default("ATMNqryReq")

	@ATMNqryReq.deleter
	def ATMNqryReq(self):
		del self._ATMNqryReq
		self._ATMNqryReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdATMNqryReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMNqryReq', type=ATMInquiryRequest3, min=0, max=1, mutex_group=None, array=False),
	))

