import base_types
import Header31
import ContentInformationType15
import ATMTransferRequest2
import ContentInformationType10

class ATMTransferRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ATMTrfReq", "_PrtctdATMTrfReq", "_SctyTrlr", "_Hdr"]
	@property
	def ATMTrfReq(self):
		return self._ATMTrfReq

	@ATMTrfReq.setter
	def ATMTrfReq(self, value):
		self._ATMTrfReq = value if type(value) != auto else self.make_default("ATMTrfReq")

	@ATMTrfReq.deleter
	def ATMTrfReq(self):
		del self._ATMTrfReq
		self._ATMTrfReq = None

	@property
	def PrtctdATMTrfReq(self):
		return self._PrtctdATMTrfReq

	@PrtctdATMTrfReq.setter
	def PrtctdATMTrfReq(self, value):
		self._PrtctdATMTrfReq = value if type(value) != auto else self.make_default("PrtctdATMTrfReq")

	@PrtctdATMTrfReq.deleter
	def PrtctdATMTrfReq(self):
		del self._PrtctdATMTrfReq
		self._PrtctdATMTrfReq = None

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
		base_types.FieldEntry(name='ATMTrfReq', type=ATMTransferRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMTrfReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

