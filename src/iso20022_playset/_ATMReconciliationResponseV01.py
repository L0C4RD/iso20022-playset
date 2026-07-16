# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationRequestComponent1
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMReconciliationResponseV01(base_types._BaseFieldType):

	__slots__ = ["_ATMRcncltnRspn", "_Hdr", "_PrtctdATMRcncltnRspn", "_SctyTrlr"]
	@property
	def ATMRcncltnRspn(self):
		return self._ATMRcncltnRspn

	@ATMRcncltnRspn.setter
	def ATMRcncltnRspn(self, value):
		self._ATMRcncltnRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMRcncltnRspn', ATMReconciliationRequestComponent1, False)

	@ATMRcncltnRspn.deleter
	def ATMRcncltnRspn(self):
		del self._ATMRcncltnRspn
		self._ATMRcncltnRspn = base_types.UninitialisedField(self, 'ATMRcncltnRspn', ATMReconciliationRequestComponent1, False)

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
	def PrtctdATMRcncltnRspn(self):
		return self._PrtctdATMRcncltnRspn

	@PrtctdATMRcncltnRspn.setter
	def PrtctdATMRcncltnRspn(self, value):
		self._PrtctdATMRcncltnRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMRcncltnRspn', ContentInformationType10, False)

	@PrtctdATMRcncltnRspn.deleter
	def PrtctdATMRcncltnRspn(self):
		del self._PrtctdATMRcncltnRspn
		self._PrtctdATMRcncltnRspn = base_types.UninitialisedField(self, 'PrtctdATMRcncltnRspn', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMRcncltnRspn', type=ATMReconciliationRequestComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMRcncltnRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))