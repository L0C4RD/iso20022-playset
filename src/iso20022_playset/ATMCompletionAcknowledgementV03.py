from . import base_types
from .ContentInformationType15 import ContentInformationType15
from .Header32 import Header32
from .ContentInformationType10 import ContentInformationType10
from .ATMCompletionAcknowledgement3 import ATMCompletionAcknowledgement3

class ATMCompletionAcknowledgementV03(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_ATMCmpltnAck", "_PrtctdATMCmpltnAck", "_Hdr"]
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
	def ATMCmpltnAck(self):
		return self._ATMCmpltnAck

	@ATMCmpltnAck.setter
	def ATMCmpltnAck(self, value):
		self._ATMCmpltnAck = value if type(value) != base_types.auto else self.make_default("ATMCmpltnAck")

	@ATMCmpltnAck.deleter
	def ATMCmpltnAck(self):
		del self._ATMCmpltnAck
		self._ATMCmpltnAck = None

	@property
	def PrtctdATMCmpltnAck(self):
		return self._PrtctdATMCmpltnAck

	@PrtctdATMCmpltnAck.setter
	def PrtctdATMCmpltnAck(self, value):
		self._PrtctdATMCmpltnAck = value if type(value) != base_types.auto else self.make_default("PrtctdATMCmpltnAck")

	@PrtctdATMCmpltnAck.deleter
	def PrtctdATMCmpltnAck(self):
		del self._PrtctdATMCmpltnAck
		self._PrtctdATMCmpltnAck = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMCmpltnAck', type=ATMCompletionAcknowledgement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMCmpltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
	))

