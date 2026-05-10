import base_types
import ATMReconciliationRequestComponent1
import Header31
import ContentInformationType15
import ContentInformationType10

class ATMReconciliationResponseV01(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMRcncltnRspn", "_ATMRcncltnRspn", "_SctyTrlr", "_Hdr"]
	@property
	def PrtctdATMRcncltnRspn(self):
		return self._PrtctdATMRcncltnRspn

	@PrtctdATMRcncltnRspn.setter
	def PrtctdATMRcncltnRspn(self, value):
		self._PrtctdATMRcncltnRspn = value if type(value) != auto else self.make_default("PrtctdATMRcncltnRspn")

	@PrtctdATMRcncltnRspn.deleter
	def PrtctdATMRcncltnRspn(self):
		del self._PrtctdATMRcncltnRspn
		self._PrtctdATMRcncltnRspn = None

	@property
	def ATMRcncltnRspn(self):
		return self._ATMRcncltnRspn

	@ATMRcncltnRspn.setter
	def ATMRcncltnRspn(self, value):
		self._ATMRcncltnRspn = value if type(value) != auto else self.make_default("ATMRcncltnRspn")

	@ATMRcncltnRspn.deleter
	def ATMRcncltnRspn(self):
		del self._ATMRcncltnRspn
		self._ATMRcncltnRspn = None

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
		base_types.FieldEntry(name='PrtctdATMRcncltnRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMRcncltnRspn', type=ATMReconciliationRequestComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

