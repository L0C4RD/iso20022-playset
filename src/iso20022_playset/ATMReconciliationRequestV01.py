import base_types
import ATMReconciliationRequestComponent1
import Header31
import ContentInformationType15
import ContentInformationType10

class ATMReconciliationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMRcncltnReq", "_ATMRcncltnReq", "_SctyTrlr", "_Hdr"]
	@property
	def PrtctdATMRcncltnReq(self):
		return self._PrtctdATMRcncltnReq

	@PrtctdATMRcncltnReq.setter
	def PrtctdATMRcncltnReq(self, value):
		self._PrtctdATMRcncltnReq = value if type(value) != auto else self.make_default("PrtctdATMRcncltnReq")

	@PrtctdATMRcncltnReq.deleter
	def PrtctdATMRcncltnReq(self):
		del self._PrtctdATMRcncltnReq
		self._PrtctdATMRcncltnReq = None

	@property
	def ATMRcncltnReq(self):
		return self._ATMRcncltnReq

	@ATMRcncltnReq.setter
	def ATMRcncltnReq(self, value):
		self._ATMRcncltnReq = value if type(value) != auto else self.make_default("ATMRcncltnReq")

	@ATMRcncltnReq.deleter
	def ATMRcncltnReq(self):
		del self._ATMRcncltnReq
		self._ATMRcncltnReq = None

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
		base_types.FieldEntry(name='PrtctdATMRcncltnReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMRcncltnReq', type=ATMReconciliationRequestComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

