# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMTransferRequest2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMTransferRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ATMTrfReq", "_Hdr", "_PrtctdATMTrfReq", "_SctyTrlr"]
	@property
	def ATMTrfReq(self):
		return self._ATMTrfReq

	@ATMTrfReq.setter
	def ATMTrfReq(self, value):
		self._ATMTrfReq = value if value is not None else base_types.UninitialisedField(self, 'ATMTrfReq', ATMTransferRequest2, False)

	@ATMTrfReq.deleter
	def ATMTrfReq(self):
		del self._ATMTrfReq
		self._ATMTrfReq = base_types.UninitialisedField(self, 'ATMTrfReq', ATMTransferRequest2, False)

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
	def PrtctdATMTrfReq(self):
		return self._PrtctdATMTrfReq

	@PrtctdATMTrfReq.setter
	def PrtctdATMTrfReq(self, value):
		self._PrtctdATMTrfReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMTrfReq', ContentInformationType10, False)

	@PrtctdATMTrfReq.deleter
	def PrtctdATMTrfReq(self):
		del self._PrtctdATMTrfReq
		self._PrtctdATMTrfReq = base_types.UninitialisedField(self, 'PrtctdATMTrfReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMTrfReq', type=ATMTransferRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMTrfReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))