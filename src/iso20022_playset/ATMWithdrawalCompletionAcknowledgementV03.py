from . import base_types
import Header32
import ATMWithdrawalCompletionAcknowledgement3
import ContentInformationType10
import ContentInformationType15

class ATMWithdrawalCompletionAcknowledgementV03(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMWdrwlCmpltnAck", "_SctyTrlr", "_Hdr", "_ATMWdrwlCmpltnAck"]
	@property
	def PrtctdATMWdrwlCmpltnAck(self):
		return self._PrtctdATMWdrwlCmpltnAck

	@PrtctdATMWdrwlCmpltnAck.setter
	def PrtctdATMWdrwlCmpltnAck(self, value):
		self._PrtctdATMWdrwlCmpltnAck = value if type(value) != auto else self.make_default("PrtctdATMWdrwlCmpltnAck")

	@PrtctdATMWdrwlCmpltnAck.deleter
	def PrtctdATMWdrwlCmpltnAck(self):
		del self._PrtctdATMWdrwlCmpltnAck
		self._PrtctdATMWdrwlCmpltnAck = None

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

	@property
	def ATMWdrwlCmpltnAck(self):
		return self._ATMWdrwlCmpltnAck

	@ATMWdrwlCmpltnAck.setter
	def ATMWdrwlCmpltnAck(self, value):
		self._ATMWdrwlCmpltnAck = value if type(value) != auto else self.make_default("ATMWdrwlCmpltnAck")

	@ATMWdrwlCmpltnAck.deleter
	def ATMWdrwlCmpltnAck(self):
		del self._ATMWdrwlCmpltnAck
		self._ATMWdrwlCmpltnAck = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdATMWdrwlCmpltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMWdrwlCmpltnAck', type=ATMWithdrawalCompletionAcknowledgement3, min=0, max=1, mutex_group=None, array=False),
	))

