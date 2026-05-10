import base_types
import Header32
import ATMDepositCompletionAcknowledgement2
import ContentInformationType15
import ContentInformationType10

class ATMDepositCompletionAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_ATMDpstCmpltnAck", "_SctyTrlr", "_PrtctdATMDpstCmpltnAck"]
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
	def ATMDpstCmpltnAck(self):
		return self._ATMDpstCmpltnAck

	@ATMDpstCmpltnAck.setter
	def ATMDpstCmpltnAck(self, value):
		self._ATMDpstCmpltnAck = value if type(value) != auto else self.make_default("ATMDpstCmpltnAck")

	@ATMDpstCmpltnAck.deleter
	def ATMDpstCmpltnAck(self):
		del self._ATMDpstCmpltnAck
		self._ATMDpstCmpltnAck = None

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
	def PrtctdATMDpstCmpltnAck(self):
		return self._PrtctdATMDpstCmpltnAck

	@PrtctdATMDpstCmpltnAck.setter
	def PrtctdATMDpstCmpltnAck(self, value):
		self._PrtctdATMDpstCmpltnAck = value if type(value) != auto else self.make_default("PrtctdATMDpstCmpltnAck")

	@PrtctdATMDpstCmpltnAck.deleter
	def PrtctdATMDpstCmpltnAck(self):
		del self._PrtctdATMDpstCmpltnAck
		self._PrtctdATMDpstCmpltnAck = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMDpstCmpltnAck', type=ATMDepositCompletionAcknowledgement2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstCmpltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))

