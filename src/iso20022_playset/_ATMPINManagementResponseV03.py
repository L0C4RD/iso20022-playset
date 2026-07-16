# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMPINManagementResponse3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMPINManagementResponseV03(base_types._BaseFieldType):

	__slots__ = ["_ATMPINMgmtRspn", "_Hdr", "_PrtctdATMPINMgmtRspn", "_SctyTrlr"]
	@property
	def ATMPINMgmtRspn(self):
		return self._ATMPINMgmtRspn

	@ATMPINMgmtRspn.setter
	def ATMPINMgmtRspn(self, value):
		self._ATMPINMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMPINMgmtRspn', ATMPINManagementResponse3, False)

	@ATMPINMgmtRspn.deleter
	def ATMPINMgmtRspn(self):
		del self._ATMPINMgmtRspn
		self._ATMPINMgmtRspn = base_types.UninitialisedField(self, 'ATMPINMgmtRspn', ATMPINManagementResponse3, False)

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
	def PrtctdATMPINMgmtRspn(self):
		return self._PrtctdATMPINMgmtRspn

	@PrtctdATMPINMgmtRspn.setter
	def PrtctdATMPINMgmtRspn(self, value):
		self._PrtctdATMPINMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMPINMgmtRspn', ContentInformationType10, False)

	@PrtctdATMPINMgmtRspn.deleter
	def PrtctdATMPINMgmtRspn(self):
		del self._PrtctdATMPINMgmtRspn
		self._PrtctdATMPINMgmtRspn = base_types.UninitialisedField(self, 'PrtctdATMPINMgmtRspn', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMPINMgmtRspn', type=ATMPINManagementResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMPINMgmtRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))