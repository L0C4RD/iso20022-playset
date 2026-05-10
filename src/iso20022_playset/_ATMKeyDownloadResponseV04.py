from . import base_types
from .Header31 import Header31
from .ContentInformationType10 import ContentInformationType10
from .ContentInformationType13 import ContentInformationType13
from .ATMKeyDownloadResponse5 import ATMKeyDownloadResponse5

class ATMKeyDownloadResponseV04(base_types._BaseFieldType):

	__slots__ = ["_ATMKeyDwnldRspn", "_PrtctdATMKeyDwnldRspn", "_SctyTrlr", "_Hdr"]
	@property
	def ATMKeyDwnldRspn(self):
		return self._ATMKeyDwnldRspn

	@ATMKeyDwnldRspn.setter
	def ATMKeyDwnldRspn(self, value):
		self._ATMKeyDwnldRspn = value if type(value) != base_types.auto else self.make_default("ATMKeyDwnldRspn")

	@ATMKeyDwnldRspn.deleter
	def ATMKeyDwnldRspn(self):
		del self._ATMKeyDwnldRspn
		self._ATMKeyDwnldRspn = None

	@property
	def PrtctdATMKeyDwnldRspn(self):
		return self._PrtctdATMKeyDwnldRspn

	@PrtctdATMKeyDwnldRspn.setter
	def PrtctdATMKeyDwnldRspn(self, value):
		self._PrtctdATMKeyDwnldRspn = value if type(value) != base_types.auto else self.make_default("PrtctdATMKeyDwnldRspn")

	@PrtctdATMKeyDwnldRspn.deleter
	def PrtctdATMKeyDwnldRspn(self):
		del self._PrtctdATMKeyDwnldRspn
		self._PrtctdATMKeyDwnldRspn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMKeyDwnldRspn', type=ATMKeyDownloadResponse5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMKeyDwnldRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

