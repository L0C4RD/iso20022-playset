# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationAcknowledgement3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMReconciliationAcknowledgementV03(base_types._BaseFieldType):

	__slots__ = ["_ATMRcncltnAck", "_Hdr", "_PrtctdATMRcncltnAck", "_SctyTrlr"]
	@property
	def ATMRcncltnAck(self):
		return self._ATMRcncltnAck

	@ATMRcncltnAck.setter
	def ATMRcncltnAck(self, value):
		self._ATMRcncltnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMRcncltnAck', ATMReconciliationAcknowledgement3, False)

	@ATMRcncltnAck.deleter
	def ATMRcncltnAck(self):
		del self._ATMRcncltnAck
		self._ATMRcncltnAck = base_types.UninitialisedField(self, 'ATMRcncltnAck', ATMReconciliationAcknowledgement3, False)

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
	def PrtctdATMRcncltnAck(self):
		return self._PrtctdATMRcncltnAck

	@PrtctdATMRcncltnAck.setter
	def PrtctdATMRcncltnAck(self, value):
		self._PrtctdATMRcncltnAck = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMRcncltnAck', ContentInformationType10, False)

	@PrtctdATMRcncltnAck.deleter
	def PrtctdATMRcncltnAck(self):
		del self._PrtctdATMRcncltnAck
		self._PrtctdATMRcncltnAck = base_types.UninitialisedField(self, 'PrtctdATMRcncltnAck', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMRcncltnAck', type=ATMReconciliationAcknowledgement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMRcncltnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))