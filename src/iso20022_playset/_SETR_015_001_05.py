# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SwitchOrderConfirmationV05

class SETR_015_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.015.001.05"
		_docname = "setr.015.001.05"

		__slots__ = ["_SwtchOrdrConf"]
		@property
		def SwtchOrdrConf(self):
			return self._SwtchOrdrConf

		@SwtchOrdrConf.setter
		def SwtchOrdrConf(self, value):
			self._SwtchOrdrConf = value if value is not None else base_types.UninitialisedField(self, 'SwtchOrdrConf', SwitchOrderConfirmationV05, False)

		@SwtchOrdrConf.deleter
		def SwtchOrdrConf(self):
			del self._SwtchOrdrConf
			self._SwtchOrdrConf = base_types.UninitialisedField(self, 'SwtchOrdrConf', SwitchOrderConfirmationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrConf', type=SwitchOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))