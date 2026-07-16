# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMConfigurationReportV01

class CAAM_013_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.013.001.01"
		_docname = "caam.013.001.01"

		__slots__ = ["_ATMCfgtnRpt"]
		@property
		def ATMCfgtnRpt(self):
			return self._ATMCfgtnRpt

		@ATMCfgtnRpt.setter
		def ATMCfgtnRpt(self, value):
			self._ATMCfgtnRpt = value if value is not None else base_types.UninitialisedField(self, 'ATMCfgtnRpt', ATMConfigurationReportV01, False)

		@ATMCfgtnRpt.deleter
		def ATMCfgtnRpt(self):
			del self._ATMCfgtnRpt
			self._ATMCfgtnRpt = base_types.UninitialisedField(self, 'ATMCfgtnRpt', ATMConfigurationReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMCfgtnRpt', type=ATMConfigurationReportV01, min=1, max=1, mutex_group=None, array=False),
		))