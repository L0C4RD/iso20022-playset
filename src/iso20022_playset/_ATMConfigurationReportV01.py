# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMConfigurationReportComponent1 import ATMConfigurationReportComponent1
from ._ContentInformationType10 import ContentInformationType10
from ._ContentInformationType15 import ContentInformationType15
from ._Header31 import Header31

class ATMConfigurationReportV01(base_types._BaseFieldType):

	__slots__ = ["_ATMCfgtnRpt", "_Hdr", "_PrtctdATMCfgtnRpt", "_SctyTrlr"]
	@property
	def ATMCfgtnRpt(self):
		return self._ATMCfgtnRpt

	@ATMCfgtnRpt.setter
	def ATMCfgtnRpt(self, value):
		self._ATMCfgtnRpt = value if type(value) != base_types.auto else self.make_default("ATMCfgtnRpt")

	@ATMCfgtnRpt.deleter
	def ATMCfgtnRpt(self):
		del self._ATMCfgtnRpt
		self._ATMCfgtnRpt = None

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
	def PrtctdATMCfgtnRpt(self):
		return self._PrtctdATMCfgtnRpt

	@PrtctdATMCfgtnRpt.setter
	def PrtctdATMCfgtnRpt(self, value):
		self._PrtctdATMCfgtnRpt = value if type(value) != base_types.auto else self.make_default("PrtctdATMCfgtnRpt")

	@PrtctdATMCfgtnRpt.deleter
	def PrtctdATMCfgtnRpt(self):
		del self._PrtctdATMCfgtnRpt
		self._PrtctdATMCfgtnRpt = None

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
		base_types.FieldEntry(name='ATMCfgtnRpt', type=ATMConfigurationReportComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMCfgtnRpt', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))