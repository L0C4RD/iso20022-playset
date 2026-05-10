from . import base_types
import ContentInformationType13
import ATMKeyDownloadResponse5
import ContentInformationType10
import Header31

class ATMKeyDownloadResponseV04(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_PrtctdATMKeyDwnldRspn", "_Hdr", "_ATMKeyDwnldRspn"]
	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def PrtctdATMKeyDwnldRspn(self):
		return self._PrtctdATMKeyDwnldRspn

	@PrtctdATMKeyDwnldRspn.setter
	def PrtctdATMKeyDwnldRspn(self, value):
		self._PrtctdATMKeyDwnldRspn = value if type(value) != auto else self.make_default("PrtctdATMKeyDwnldRspn")

	@PrtctdATMKeyDwnldRspn.deleter
	def PrtctdATMKeyDwnldRspn(self):
		del self._PrtctdATMKeyDwnldRspn
		self._PrtctdATMKeyDwnldRspn = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def ATMKeyDwnldRspn(self):
		return self._ATMKeyDwnldRspn

	@ATMKeyDwnldRspn.setter
	def ATMKeyDwnldRspn(self, value):
		self._ATMKeyDwnldRspn = value if type(value) != auto else self.make_default("ATMKeyDwnldRspn")

	@ATMKeyDwnldRspn.deleter
	def ATMKeyDwnldRspn(self):
		del self._ATMKeyDwnldRspn
		self._ATMKeyDwnldRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMKeyDwnldRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMKeyDwnldRspn', type=ATMKeyDownloadResponse5, min=0, max=1, mutex_group=None, array=False),
	))

