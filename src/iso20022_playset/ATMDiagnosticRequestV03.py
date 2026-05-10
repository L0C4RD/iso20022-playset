import base_types
import Header31
import ContentInformationType15
import ContentInformationType10
import ATMDiagnosticRequest3

class ATMDiagnosticRequestV03(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMDgnstcReq", "_Hdr", "_ATMDgnstcReq", "_SctyTrlr"]
	@property
	def PrtctdATMDgnstcReq(self):
		return self._PrtctdATMDgnstcReq

	@PrtctdATMDgnstcReq.setter
	def PrtctdATMDgnstcReq(self, value):
		self._PrtctdATMDgnstcReq = value if type(value) != auto else self.make_default("PrtctdATMDgnstcReq")

	@PrtctdATMDgnstcReq.deleter
	def PrtctdATMDgnstcReq(self):
		del self._PrtctdATMDgnstcReq
		self._PrtctdATMDgnstcReq = None

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
	def ATMDgnstcReq(self):
		return self._ATMDgnstcReq

	@ATMDgnstcReq.setter
	def ATMDgnstcReq(self, value):
		self._ATMDgnstcReq = value if type(value) != auto else self.make_default("ATMDgnstcReq")

	@ATMDgnstcReq.deleter
	def ATMDgnstcReq(self):
		del self._ATMDgnstcReq
		self._ATMDgnstcReq = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdATMDgnstcReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMDgnstcReq', type=ATMDiagnosticRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))

