# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMKeyDownloadRequest5
from . import ContentInformationType10
from . import ContentInformationType13
from . import Header31

class ATMKeyDownloadRequestV04(base_types._BaseFieldType):

	__slots__ = ["_ATMKeyDwnldReq", "_Hdr", "_PrtctdATMKeyDwnldReq", "_SctyTrlr"]
	@property
	def ATMKeyDwnldReq(self):
		return self._ATMKeyDwnldReq

	@ATMKeyDwnldReq.setter
	def ATMKeyDwnldReq(self, value):
		self._ATMKeyDwnldReq = value if value is not None else base_types.UninitialisedField(self, 'ATMKeyDwnldReq', ATMKeyDownloadRequest5, False)

	@ATMKeyDwnldReq.deleter
	def ATMKeyDwnldReq(self):
		del self._ATMKeyDwnldReq
		self._ATMKeyDwnldReq = base_types.UninitialisedField(self, 'ATMKeyDwnldReq', ATMKeyDownloadRequest5, False)

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
	def PrtctdATMKeyDwnldReq(self):
		return self._PrtctdATMKeyDwnldReq

	@PrtctdATMKeyDwnldReq.setter
	def PrtctdATMKeyDwnldReq(self, value):
		self._PrtctdATMKeyDwnldReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMKeyDwnldReq', ContentInformationType10, False)

	@PrtctdATMKeyDwnldReq.deleter
	def PrtctdATMKeyDwnldReq(self):
		del self._PrtctdATMKeyDwnldReq
		self._PrtctdATMKeyDwnldReq = base_types.UninitialisedField(self, 'PrtctdATMKeyDwnldReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMKeyDwnldReq', type=ATMKeyDownloadRequest5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMKeyDwnldReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
	))