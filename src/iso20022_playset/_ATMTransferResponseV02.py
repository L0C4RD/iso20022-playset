# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMTransferResponse2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMTransferResponseV02(base_types._BaseFieldType):

	__slots__ = ["_ATMTrfRspn", "_Hdr", "_PrtctdATMTrfRspn", "_SctyTrlr"]
	@property
	def ATMTrfRspn(self):
		return self._ATMTrfRspn

	@ATMTrfRspn.setter
	def ATMTrfRspn(self, value):
		self._ATMTrfRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMTrfRspn', ATMTransferResponse2, False)

	@ATMTrfRspn.deleter
	def ATMTrfRspn(self):
		del self._ATMTrfRspn
		self._ATMTrfRspn = base_types.UninitialisedField(self, 'ATMTrfRspn', ATMTransferResponse2, False)

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
	def PrtctdATMTrfRspn(self):
		return self._PrtctdATMTrfRspn

	@PrtctdATMTrfRspn.setter
	def PrtctdATMTrfRspn(self, value):
		self._PrtctdATMTrfRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMTrfRspn', ContentInformationType10, False)

	@PrtctdATMTrfRspn.deleter
	def PrtctdATMTrfRspn(self):
		del self._PrtctdATMTrfRspn
		self._PrtctdATMTrfRspn = base_types.UninitialisedField(self, 'PrtctdATMTrfRspn', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMTrfRspn', type=ATMTransferResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMTrfRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))