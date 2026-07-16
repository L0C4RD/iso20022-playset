# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMConfigurationReportComponent1
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMConfigurationReportV01(base_types._BaseFieldType):

	__slots__ = ["_ATMCfgtnRpt", "_Hdr", "_PrtctdATMCfgtnRpt", "_SctyTrlr"]
	@property
	def ATMCfgtnRpt(self):
		return self._ATMCfgtnRpt

	@ATMCfgtnRpt.setter
	def ATMCfgtnRpt(self, value):
		self._ATMCfgtnRpt = value if value is not None else base_types.UninitialisedField(self, 'ATMCfgtnRpt', ATMConfigurationReportComponent1, False)

	@ATMCfgtnRpt.deleter
	def ATMCfgtnRpt(self):
		del self._ATMCfgtnRpt
		self._ATMCfgtnRpt = base_types.UninitialisedField(self, 'ATMCfgtnRpt', ATMConfigurationReportComponent1, False)

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
	def PrtctdATMCfgtnRpt(self):
		return self._PrtctdATMCfgtnRpt

	@PrtctdATMCfgtnRpt.setter
	def PrtctdATMCfgtnRpt(self, value):
		self._PrtctdATMCfgtnRpt = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMCfgtnRpt', ContentInformationType10, False)

	@PrtctdATMCfgtnRpt.deleter
	def PrtctdATMCfgtnRpt(self):
		del self._PrtctdATMCfgtnRpt
		self._PrtctdATMCfgtnRpt = base_types.UninitialisedField(self, 'PrtctdATMCfgtnRpt', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMCfgtnRpt', type=ATMConfigurationReportComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMCfgtnRpt', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))