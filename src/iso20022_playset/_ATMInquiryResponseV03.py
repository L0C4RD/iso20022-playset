# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMInquiryResponse3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMInquiryResponseV03(base_types._BaseFieldType):

	__slots__ = ["_ATMNqryRspn", "_Hdr", "_PrtctdATMNqryRspn", "_SctyTrlr"]
	@property
	def ATMNqryRspn(self):
		return self._ATMNqryRspn

	@ATMNqryRspn.setter
	def ATMNqryRspn(self, value):
		self._ATMNqryRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMNqryRspn', ATMInquiryResponse3, False)

	@ATMNqryRspn.deleter
	def ATMNqryRspn(self):
		del self._ATMNqryRspn
		self._ATMNqryRspn = base_types.UninitialisedField(self, 'ATMNqryRspn', ATMInquiryResponse3, False)

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
	def PrtctdATMNqryRspn(self):
		return self._PrtctdATMNqryRspn

	@PrtctdATMNqryRspn.setter
	def PrtctdATMNqryRspn(self, value):
		self._PrtctdATMNqryRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMNqryRspn', ContentInformationType10, False)

	@PrtctdATMNqryRspn.deleter
	def PrtctdATMNqryRspn(self):
		del self._PrtctdATMNqryRspn
		self._PrtctdATMNqryRspn = base_types.UninitialisedField(self, 'PrtctdATMNqryRspn', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMNqryRspn', type=ATMInquiryResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMNqryRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))