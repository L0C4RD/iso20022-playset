# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositCompletionAcknowledgement2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMDepositCompletionAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_ATMDpstCmpltnAck", "_Hdr", "_PrtctdATMDpstCmpltnAck", "_SctyTrlr"]
	@property
	def ATMDpstCmpltnAck(self):
		return self._ATMDpstCmpltnAck

	@ATMDpstCmpltnAck.setter
	def ATMDpstCmpltnAck(self, value):
		self._ATMDpstCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMDpstCmpltnAck', ATMDepositCompletionAcknowledgement2, False)

	@ATMDpstCmpltnAck.deleter
	def ATMDpstCmpltnAck(self):
		del self._ATMDpstCmpltnAck
		self._ATMDpstCmpltnAck = base_types.UninitialisedField(self, 'ATMDpstCmpltnAck', ATMDepositCompletionAcknowledgement2, False)

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
	def PrtctdATMDpstCmpltnAck(self):
		return self._PrtctdATMDpstCmpltnAck

	@PrtctdATMDpstCmpltnAck.setter
	def PrtctdATMDpstCmpltnAck(self, value):
		self._PrtctdATMDpstCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDpstCmpltnAck', ContentInformationType10, False)

	@PrtctdATMDpstCmpltnAck.deleter
	def PrtctdATMDpstCmpltnAck(self):
		del self._PrtctdATMDpstCmpltnAck
		self._PrtctdATMDpstCmpltnAck = base_types.UninitialisedField(self, 'PrtctdATMDpstCmpltnAck', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMDpstCmpltnAck', type=ATMDepositCompletionAcknowledgement2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstCmpltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))