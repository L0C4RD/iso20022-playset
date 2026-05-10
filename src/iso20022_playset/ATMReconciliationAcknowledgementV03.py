import base_types
import ATMReconciliationAcknowledgement3
import ContentInformationType15
import Header32
import ContentInformationType10

class ATMReconciliationAcknowledgementV03(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMRcncltnAck", "_ATMRcncltnAck", "_Hdr", "_SctyTrlr"]
	@property
	def PrtctdATMRcncltnAck(self):
		return self._PrtctdATMRcncltnAck

	@PrtctdATMRcncltnAck.setter
	def PrtctdATMRcncltnAck(self, value):
		self._PrtctdATMRcncltnAck = value if type(value) != auto else self.make_default("PrtctdATMRcncltnAck")

	@PrtctdATMRcncltnAck.deleter
	def PrtctdATMRcncltnAck(self):
		del self._PrtctdATMRcncltnAck
		self._PrtctdATMRcncltnAck = None

	@property
	def ATMRcncltnAck(self):
		return self._ATMRcncltnAck

	@ATMRcncltnAck.setter
	def ATMRcncltnAck(self, value):
		self._ATMRcncltnAck = value if type(value) != auto else self.make_default("ATMRcncltnAck")

	@ATMRcncltnAck.deleter
	def ATMRcncltnAck(self):
		del self._ATMRcncltnAck
		self._ATMRcncltnAck = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdATMRcncltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMRcncltnAck', type=ATMReconciliationAcknowledgement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))

