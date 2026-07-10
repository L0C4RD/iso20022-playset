# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMConfigurationControlV01 import ATMConfigurationControlV01

class CAAM_014_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.014.001.01"
		_docname = "caam.014.001.01"

		__slots__ = ["_ATMCfgtnCtrl"]
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

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMCfgtnCtrl', type=ATMConfigurationControlV01, min=1, max=1, mutex_group=None, array=False),
		))