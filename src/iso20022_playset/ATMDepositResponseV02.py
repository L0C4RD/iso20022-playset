import base_types
import Header31
import ATMDepositResponse2
import ContentInformationType15
import ContentInformationType10

class ATMDepositResponseV02(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_PrtctdATMDpstRspn", "_ATMDpstRspn", "_Hdr"]
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
	def PrtctdATMDpstRspn(self):
		return self._PrtctdATMDpstRspn

	@PrtctdATMDpstRspn.setter
	def PrtctdATMDpstRspn(self, value):
		self._PrtctdATMDpstRspn = value if type(value) != auto else self.make_default("PrtctdATMDpstRspn")

	@PrtctdATMDpstRspn.deleter
	def PrtctdATMDpstRspn(self):
		del self._PrtctdATMDpstRspn
		self._PrtctdATMDpstRspn = None

	@property
	def ATMDpstRspn(self):
		return self._ATMDpstRspn

	@ATMDpstRspn.setter
	def ATMDpstRspn(self, value):
		self._ATMDpstRspn = value if type(value) != auto else self.make_default("ATMDpstRspn")

	@ATMDpstRspn.deleter
	def ATMDpstRspn(self):
		del self._ATMDpstRspn
		self._ATMDpstRspn = None

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
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMDpstRspn', type=ATMDepositResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

