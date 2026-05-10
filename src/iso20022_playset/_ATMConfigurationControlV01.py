from . import base_types
from .Header31 import Header31
from .ContentInformationType10 import ContentInformationType10
from .ContentInformationType15 import ContentInformationType15
from .ATMConfigurationControlComponent1 import ATMConfigurationControlComponent1

class ATMConfigurationControlV01(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMCfgtnCtrl", "_SctyTrlr", "_ATMCfgtnCtrl", "_Hdr"]
	@property
	def PrtctdATMCfgtnCtrl(self):
		return self._PrtctdATMCfgtnCtrl

	@PrtctdATMCfgtnCtrl.setter
	def PrtctdATMCfgtnCtrl(self, value):
		self._PrtctdATMCfgtnCtrl = value if type(value) != base_types.auto else self.make_default("PrtctdATMCfgtnCtrl")

	@PrtctdATMCfgtnCtrl.deleter
	def PrtctdATMCfgtnCtrl(self):
		del self._PrtctdATMCfgtnCtrl
		self._PrtctdATMCfgtnCtrl = None

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
	def ATMCfgtnCtrl(self):
		return self._ATMCfgtnCtrl

	@ATMCfgtnCtrl.setter
	def ATMCfgtnCtrl(self, value):
		self._ATMCfgtnCtrl = value if type(value) != base_types.auto else self.make_default("ATMCfgtnCtrl")

	@ATMCfgtnCtrl.deleter
	def ATMCfgtnCtrl(self):
		del self._ATMCfgtnCtrl
		self._ATMCfgtnCtrl = None

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
		base_types.FieldEntry(name='PrtctdATMCfgtnCtrl', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMCfgtnCtrl', type=ATMConfigurationControlComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
	))

