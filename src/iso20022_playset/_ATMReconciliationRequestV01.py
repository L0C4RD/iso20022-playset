# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationRequestComponent1
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMReconciliationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ATMRcncltnReq", "_Hdr", "_PrtctdATMRcncltnReq", "_SctyTrlr"]
	@property
	def ATMRcncltnReq(self):
		return self._ATMRcncltnReq

	@ATMRcncltnReq.setter
	def ATMRcncltnReq(self, value):
		self._ATMRcncltnReq = value if value is not None else base_types.UninitialisedField(self, 'ATMRcncltnReq', ATMReconciliationRequestComponent1, False)

	@ATMRcncltnReq.deleter
	def ATMRcncltnReq(self):
		del self._ATMRcncltnReq
		self._ATMRcncltnReq = base_types.UninitialisedField(self, 'ATMRcncltnReq', ATMReconciliationRequestComponent1, False)

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
	def PrtctdATMRcncltnReq(self):
		return self._PrtctdATMRcncltnReq

	@PrtctdATMRcncltnReq.setter
	def PrtctdATMRcncltnReq(self, value):
		self._PrtctdATMRcncltnReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMRcncltnReq', ContentInformationType10, False)

	@PrtctdATMRcncltnReq.deleter
	def PrtctdATMRcncltnReq(self):
		del self._PrtctdATMRcncltnReq
		self._PrtctdATMRcncltnReq = base_types.UninitialisedField(self, 'PrtctdATMRcncltnReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMRcncltnReq', type=ATMReconciliationRequestComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMRcncltnReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))