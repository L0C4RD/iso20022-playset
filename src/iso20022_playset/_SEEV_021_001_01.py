# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAMovementConfirmationV01

class SEEV_021_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01"
		_docname = "seev.021.001.01"

		__slots__ = ["_AgtCAMvmntConf"]
		@property
		def AgtCAMvmntConf(self):
			return self._AgtCAMvmntConf

		@AgtCAMvmntConf.setter
		def AgtCAMvmntConf(self, value):
			self._AgtCAMvmntConf = value if value is not None else base_types.UninitialisedField(self, 'AgtCAMvmntConf', AgentCAMovementConfirmationV01, False)

		@AgtCAMvmntConf.deleter
		def AgtCAMvmntConf(self):
			del self._AgtCAMvmntConf
			self._AgtCAMvmntConf = base_types.UninitialisedField(self, 'AgtCAMvmntConf', AgentCAMovementConfirmationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAMvmntConf', type=AgentCAMovementConfirmationV01, min=1, max=1, mutex_group=None, array=False),
		))