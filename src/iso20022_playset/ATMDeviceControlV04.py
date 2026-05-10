import base_types
import ATMDeviceControl3
import ContentInformationType13
import Header31
import ContentInformationType10

class ATMDeviceControlV04(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMDvcCtrl", "_ATMDvcCtrl", "_SctyTrlr", "_Hdr"]
	@property
	def PrtctdATMDvcCtrl(self):
		return self._PrtctdATMDvcCtrl

	@PrtctdATMDvcCtrl.setter
	def PrtctdATMDvcCtrl(self, value):
		self._PrtctdATMDvcCtrl = value if type(value) != auto else self.make_default("PrtctdATMDvcCtrl")

	@PrtctdATMDvcCtrl.deleter
	def PrtctdATMDvcCtrl(self):
		del self._PrtctdATMDvcCtrl
		self._PrtctdATMDvcCtrl = None

	@property
	def ATMDvcCtrl(self):
		return self._ATMDvcCtrl

	@ATMDvcCtrl.setter
	def ATMDvcCtrl(self, value):
		self._ATMDvcCtrl = value if type(value) != auto else self.make_default("ATMDvcCtrl")

	@ATMDvcCtrl.deleter
	def ATMDvcCtrl(self):
		del self._ATMDvcCtrl
		self._ATMDvcCtrl = None

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
		base_types.FieldEntry(name='PrtctdATMDvcCtrl', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMDvcCtrl', type=ATMDeviceControl3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

