# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMPINManagementRequest3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMPINManagementRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ATMPINMgmtReq", "_Hdr", "_PrtctdATMPINMgmtReq", "_SctyTrlr"]
	@property
	def ATMPINMgmtReq(self):
		return self._ATMPINMgmtReq

	@ATMPINMgmtReq.setter
	def ATMPINMgmtReq(self, value):
		self._ATMPINMgmtReq = value if value is not None else base_types.UninitialisedField(self, 'ATMPINMgmtReq', ATMPINManagementRequest3, False)

	@ATMPINMgmtReq.deleter
	def ATMPINMgmtReq(self):
		del self._ATMPINMgmtReq
		self._ATMPINMgmtReq = base_types.UninitialisedField(self, 'ATMPINMgmtReq', ATMPINManagementRequest3, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header31, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header31, False)

	@property
	def PrtctdATMPINMgmtReq(self):
		return self._PrtctdATMPINMgmtReq

	@PrtctdATMPINMgmtReq.setter
	def PrtctdATMPINMgmtReq(self, value):
		self._PrtctdATMPINMgmtReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMPINMgmtReq', ContentInformationType10, False)

	@PrtctdATMPINMgmtReq.deleter
	def PrtctdATMPINMgmtReq(self):
		del self._PrtctdATMPINMgmtReq
		self._PrtctdATMPINMgmtReq = base_types.UninitialisedField(self, 'PrtctdATMPINMgmtReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMPINMgmtReq', type=ATMPINManagementRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMPINMgmtReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))