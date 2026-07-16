# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCompletionAcknowledgement3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMCompletionAcknowledgementV03(base_types._BaseFieldType):

	__slots__ = ["_ATMCmpltnAck", "_Hdr", "_PrtctdATMCmpltnAck", "_SctyTrlr"]
	@property
	def ATMCmpltnAck(self):
		return self._ATMCmpltnAck

	@ATMCmpltnAck.setter
	def ATMCmpltnAck(self, value):
		self._ATMCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMCmpltnAck', ATMCompletionAcknowledgement3, False)

	@ATMCmpltnAck.deleter
	def ATMCmpltnAck(self):
		del self._ATMCmpltnAck
		self._ATMCmpltnAck = base_types.UninitialisedField(self, 'ATMCmpltnAck', ATMCompletionAcknowledgement3, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header32, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header32, False)

	@property
	def PrtctdATMCmpltnAck(self):
		return self._PrtctdATMCmpltnAck

	@PrtctdATMCmpltnAck.setter
	def PrtctdATMCmpltnAck(self, value):
		self._PrtctdATMCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMCmpltnAck', ContentInformationType10, False)

	@PrtctdATMCmpltnAck.deleter
	def PrtctdATMCmpltnAck(self):
		del self._PrtctdATMCmpltnAck
		self._PrtctdATMCmpltnAck = base_types.UninitialisedField(self, 'PrtctdATMCmpltnAck', ContentInformationType10, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMCmpltnAck', type=ATMCompletionAcknowledgement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMCmpltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))