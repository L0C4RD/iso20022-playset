# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorConfigurationUpdateV14

class CATM_003_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.003.001.14"
		_docname = "catm.003.001.14"

		__slots__ = ["_AccptrCfgtnUpd"]
		@property
		def AccptrCfgtnUpd(self):
			return self._AccptrCfgtnUpd

		@AccptrCfgtnUpd.setter
		def AccptrCfgtnUpd(self, value):
			self._AccptrCfgtnUpd = value if value is not None else base_types.UninitialisedField(self, 'AccptrCfgtnUpd', AcceptorConfigurationUpdateV14, False)

		@AccptrCfgtnUpd.deleter
		def AccptrCfgtnUpd(self):
			del self._AccptrCfgtnUpd
			self._AccptrCfgtnUpd = base_types.UninitialisedField(self, 'AccptrCfgtnUpd', AcceptorConfigurationUpdateV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCfgtnUpd', type=AcceptorConfigurationUpdateV14, min=1, max=1, mutex_group=None, array=False),
		))