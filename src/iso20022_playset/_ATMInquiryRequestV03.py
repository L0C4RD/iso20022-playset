# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMInquiryRequest3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMInquiryRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ATMNqryReq", "_Hdr", "_PrtctdATMNqryReq", "_SctyTrlr"]
	@property
	def ATMNqryReq(self):
		return self._ATMNqryReq

	@ATMNqryReq.setter
	def ATMNqryReq(self, value):
		self._ATMNqryReq = value if value is not None else base_types.UninitialisedField(self, 'ATMNqryReq', ATMInquiryRequest3, False)

	@ATMNqryReq.deleter
	def ATMNqryReq(self):
		del self._ATMNqryReq
		self._ATMNqryReq = base_types.UninitialisedField(self, 'ATMNqryReq', ATMInquiryRequest3, False)

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
	def PrtctdATMNqryReq(self):
		return self._PrtctdATMNqryReq

	@PrtctdATMNqryReq.setter
	def PrtctdATMNqryReq(self, value):
		self._PrtctdATMNqryReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMNqryReq', ContentInformationType10, False)

	@PrtctdATMNqryReq.deleter
	def PrtctdATMNqryReq(self):
		del self._PrtctdATMNqryReq
		self._PrtctdATMNqryReq = base_types.UninitialisedField(self, 'PrtctdATMNqryReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMNqryReq', type=ATMInquiryRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMNqryReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))