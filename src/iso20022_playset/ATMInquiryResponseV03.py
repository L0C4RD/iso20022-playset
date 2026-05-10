from . import base_types
import Header31
import ATMInquiryResponse3
import ContentInformationType15
import ContentInformationType10

class ATMInquiryResponseV03(base_types._BaseFieldType):

	__slots__ = ["_ATMNqryRspn", "_SctyTrlr", "_PrtctdATMNqryRspn", "_Hdr"]
	@property
	def ATMNqryRspn(self):
		return self._ATMNqryRspn

	@ATMNqryRspn.setter
	def ATMNqryRspn(self, value):
		self._ATMNqryRspn = value if type(value) != auto else self.make_default("ATMNqryRspn")

	@ATMNqryRspn.deleter
	def ATMNqryRspn(self):
		del self._ATMNqryRspn
		self._ATMNqryRspn = None

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
	def PrtctdATMNqryRspn(self):
		return self._PrtctdATMNqryRspn

	@PrtctdATMNqryRspn.setter
	def PrtctdATMNqryRspn(self, value):
		self._PrtctdATMNqryRspn = value if type(value) != auto else self.make_default("PrtctdATMNqryRspn")

	@PrtctdATMNqryRspn.deleter
	def PrtctdATMNqryRspn(self):
		del self._PrtctdATMNqryRspn
		self._PrtctdATMNqryRspn = None

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
		base_types.FieldEntry(name='ATMNqryRspn', type=ATMInquiryResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMNqryRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

