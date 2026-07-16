# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositResponse2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMDepositResponseV02(base_types._BaseFieldType):

	__slots__ = ["_ATMDpstRspn", "_Hdr", "_PrtctdATMDpstRspn", "_SctyTrlr"]
	@property
	def ATMDpstRspn(self):
		return self._ATMDpstRspn

	@ATMDpstRspn.setter
	def ATMDpstRspn(self, value):
		self._ATMDpstRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMDpstRspn', ATMDepositResponse2, False)

	@ATMDpstRspn.deleter
	def ATMDpstRspn(self):
		del self._ATMDpstRspn
		self._ATMDpstRspn = base_types.UninitialisedField(self, 'ATMDpstRspn', ATMDepositResponse2, False)

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
	def PrtctdATMDpstRspn(self):
		return self._PrtctdATMDpstRspn

	@PrtctdATMDpstRspn.setter
	def PrtctdATMDpstRspn(self, value):
		self._PrtctdATMDpstRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDpstRspn', ContentInformationType10, False)

	@PrtctdATMDpstRspn.deleter
	def PrtctdATMDpstRspn(self):
		del self._PrtctdATMDpstRspn
		self._PrtctdATMDpstRspn = base_types.UninitialisedField(self, 'PrtctdATMDpstRspn', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMDpstRspn', type=ATMDepositResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))