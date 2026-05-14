from . import base_types
from ._ATMKeyDownloadRequest6 import ATMKeyDownloadRequest6
from ._ContentInformationType10 import ContentInformationType10
from ._ContentInformationType13 import ContentInformationType13
from ._Header31 import Header31

class ATMKeyDownloadRequestV05(base_types._BaseFieldType):

	__slots__ = ["_ATMKeyDwnldReq", "_Hdr", "_PrtctdATMKeyDwnldReq", "_SctyTrlr"]
	@property
	def ATMKeyDwnldReq(self):
		return self._ATMKeyDwnldReq

	@ATMKeyDwnldReq.setter
	def ATMKeyDwnldReq(self, value):
		self._ATMKeyDwnldReq = value if type(value) != base_types.auto else self.make_default("ATMKeyDwnldReq")

	@ATMKeyDwnldReq.deleter
	def ATMKeyDwnldReq(self):
		del self._ATMKeyDwnldReq
		self._ATMKeyDwnldReq = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def PrtctdATMKeyDwnldReq(self):
		return self._PrtctdATMKeyDwnldReq

	@PrtctdATMKeyDwnldReq.setter
	def PrtctdATMKeyDwnldReq(self, value):
		self._PrtctdATMKeyDwnldReq = value if type(value) != base_types.auto else self.make_default("PrtctdATMKeyDwnldReq")

	@PrtctdATMKeyDwnldReq.deleter
	def PrtctdATMKeyDwnldReq(self):
		del self._PrtctdATMKeyDwnldReq
		self._PrtctdATMKeyDwnldReq = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMKeyDwnldReq', type=ATMKeyDownloadRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMKeyDwnldReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
	))

