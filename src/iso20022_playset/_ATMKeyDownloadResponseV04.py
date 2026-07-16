# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMKeyDownloadResponse5
from . import ContentInformationType10
from . import ContentInformationType13
from . import Header31

class ATMKeyDownloadResponseV04(base_types._BaseFieldType):

	__slots__ = ["_ATMKeyDwnldRspn", "_Hdr", "_PrtctdATMKeyDwnldRspn", "_SctyTrlr"]
	@property
	def ATMKeyDwnldRspn(self):
		return self._ATMKeyDwnldRspn

	@ATMKeyDwnldRspn.setter
	def ATMKeyDwnldRspn(self, value):
		self._ATMKeyDwnldRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMKeyDwnldRspn', ATMKeyDownloadResponse5, False)

	@ATMKeyDwnldRspn.deleter
	def ATMKeyDwnldRspn(self):
		del self._ATMKeyDwnldRspn
		self._ATMKeyDwnldRspn = base_types.UninitialisedField(self, 'ATMKeyDwnldRspn', ATMKeyDownloadResponse5, False)

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
	def PrtctdATMKeyDwnldRspn(self):
		return self._PrtctdATMKeyDwnldRspn

	@PrtctdATMKeyDwnldRspn.setter
	def PrtctdATMKeyDwnldRspn(self, value):
		self._PrtctdATMKeyDwnldRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMKeyDwnldRspn', ContentInformationType10, False)

	@PrtctdATMKeyDwnldRspn.deleter
	def PrtctdATMKeyDwnldRspn(self):
		del self._PrtctdATMKeyDwnldRspn
		self._PrtctdATMKeyDwnldRspn = base_types.UninitialisedField(self, 'PrtctdATMKeyDwnldRspn', ContentInformationType10, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType13, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType13, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMKeyDwnldRspn', type=ATMKeyDownloadResponse5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMKeyDwnldRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
	))