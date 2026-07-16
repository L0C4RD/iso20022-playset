# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMConfigurationControlComponent1
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMConfigurationControlV01(base_types._BaseFieldType):

	__slots__ = ["_ATMCfgtnCtrl", "_Hdr", "_PrtctdATMCfgtnCtrl", "_SctyTrlr"]
	@property
	def ATMCfgtnCtrl(self):
		return self._ATMCfgtnCtrl

	@ATMCfgtnCtrl.setter
	def ATMCfgtnCtrl(self, value):
		self._ATMCfgtnCtrl = value if value is not None else base_types.UninitialisedField(self, 'ATMCfgtnCtrl', ATMConfigurationControlComponent1, False)

	@ATMCfgtnCtrl.deleter
	def ATMCfgtnCtrl(self):
		del self._ATMCfgtnCtrl
		self._ATMCfgtnCtrl = base_types.UninitialisedField(self, 'ATMCfgtnCtrl', ATMConfigurationControlComponent1, False)

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
	def PrtctdATMCfgtnCtrl(self):
		return self._PrtctdATMCfgtnCtrl

	@PrtctdATMCfgtnCtrl.setter
	def PrtctdATMCfgtnCtrl(self, value):
		self._PrtctdATMCfgtnCtrl = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMCfgtnCtrl', ContentInformationType10, False)

	@PrtctdATMCfgtnCtrl.deleter
	def PrtctdATMCfgtnCtrl(self):
		del self._PrtctdATMCfgtnCtrl
		self._PrtctdATMCfgtnCtrl = base_types.UninitialisedField(self, 'PrtctdATMCfgtnCtrl', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMCfgtnCtrl', type=ATMConfigurationControlComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMCfgtnCtrl', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))