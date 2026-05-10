from . import base_types
import Header31
import ATMWithdrawalRequest3
import ContentInformationType10
import ContentInformationType15

class ATMWithdrawalRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ATMWdrwlReq", "_PrtctdATMWdrwlReq", "_SctyTrlr", "_Hdr"]
	@property
	def ATMWdrwlReq(self):
		return self._ATMWdrwlReq

	@ATMWdrwlReq.setter
	def ATMWdrwlReq(self, value):
		self._ATMWdrwlReq = value if type(value) != auto else self.make_default("ATMWdrwlReq")

	@ATMWdrwlReq.deleter
	def ATMWdrwlReq(self):
		del self._ATMWdrwlReq
		self._ATMWdrwlReq = None

	@property
	def PrtctdATMWdrwlReq(self):
		return self._PrtctdATMWdrwlReq

	@PrtctdATMWdrwlReq.setter
	def PrtctdATMWdrwlReq(self, value):
		self._PrtctdATMWdrwlReq = value if type(value) != auto else self.make_default("PrtctdATMWdrwlReq")

	@PrtctdATMWdrwlReq.deleter
	def PrtctdATMWdrwlReq(self):
		del self._PrtctdATMWdrwlReq
		self._PrtctdATMWdrwlReq = None

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
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMWdrwlReq', type=ATMWithdrawalRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMWdrwlReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

