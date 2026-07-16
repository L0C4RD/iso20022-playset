# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalCompletionAcknowledgement3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMWithdrawalCompletionAcknowledgementV03(base_types._BaseFieldType):

	__slots__ = ["_ATMWdrwlCmpltnAck", "_Hdr", "_PrtctdATMWdrwlCmpltnAck", "_SctyTrlr"]
	@property
	def ATMWdrwlCmpltnAck(self):
		return self._ATMWdrwlCmpltnAck

	@ATMWdrwlCmpltnAck.setter
	def ATMWdrwlCmpltnAck(self, value):
		self._ATMWdrwlCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAck', ATMWithdrawalCompletionAcknowledgement3, False)

	@ATMWdrwlCmpltnAck.deleter
	def ATMWdrwlCmpltnAck(self):
		del self._ATMWdrwlCmpltnAck
		self._ATMWdrwlCmpltnAck = base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAck', ATMWithdrawalCompletionAcknowledgement3, False)

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
	def PrtctdATMWdrwlCmpltnAck(self):
		return self._PrtctdATMWdrwlCmpltnAck

	@PrtctdATMWdrwlCmpltnAck.setter
	def PrtctdATMWdrwlCmpltnAck(self, value):
		self._PrtctdATMWdrwlCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMWdrwlCmpltnAck', ContentInformationType10, False)

	@PrtctdATMWdrwlCmpltnAck.deleter
	def PrtctdATMWdrwlCmpltnAck(self):
		del self._PrtctdATMWdrwlCmpltnAck
		self._PrtctdATMWdrwlCmpltnAck = base_types.UninitialisedField(self, 'PrtctdATMWdrwlCmpltnAck', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMWdrwlCmpltnAck', type=ATMWithdrawalCompletionAcknowledgement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMWdrwlCmpltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))