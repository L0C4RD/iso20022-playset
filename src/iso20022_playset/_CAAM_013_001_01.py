from . import base_types
from ._ATMConfigurationReportV01 import ATMConfigurationReportV01

class CAAM_013_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMCfgtnRpt"]
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

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMCfgtnRpt', type=ATMConfigurationReportV01, min=1, max=1, mutex_group=None, array=False),
		))

