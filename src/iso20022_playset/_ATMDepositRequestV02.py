# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositRequest2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMDepositRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ATMDpstReq", "_Hdr", "_PrtctdATMDpstReq", "_SctyTrlr"]
	@property
	def ATMDpstReq(self):
		return self._ATMDpstReq

	@ATMDpstReq.setter
	def ATMDpstReq(self, value):
		self._ATMDpstReq = value if value is not None else base_types.UninitialisedField(self, 'ATMDpstReq', ATMDepositRequest2, False)

	@ATMDpstReq.deleter
	def ATMDpstReq(self):
		del self._ATMDpstReq
		self._ATMDpstReq = base_types.UninitialisedField(self, 'ATMDpstReq', ATMDepositRequest2, False)

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
	def PrtctdATMDpstReq(self):
		return self._PrtctdATMDpstReq

	@PrtctdATMDpstReq.setter
	def PrtctdATMDpstReq(self, value):
		self._PrtctdATMDpstReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDpstReq', ContentInformationType10, False)

	@PrtctdATMDpstReq.deleter
	def PrtctdATMDpstReq(self):
		del self._PrtctdATMDpstReq
		self._PrtctdATMDpstReq = base_types.UninitialisedField(self, 'PrtctdATMDpstReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMDpstReq', type=ATMDepositRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))