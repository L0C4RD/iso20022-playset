# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TerminalManagementRejectionV05

class CATM_004_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.004.001.05"
		_docname = "catm.004.001.05"

		__slots__ = ["_TermnlMgmtRjctn"]
		@property
		def TermnlMgmtRjctn(self):
			return self._TermnlMgmtRjctn

		@TermnlMgmtRjctn.setter
		def TermnlMgmtRjctn(self, value):
			self._TermnlMgmtRjctn = value if value is not None else base_types.UninitialisedField(self, 'TermnlMgmtRjctn', TerminalManagementRejectionV05, False)

		@TermnlMgmtRjctn.deleter
		def TermnlMgmtRjctn(self):
			del self._TermnlMgmtRjctn
			self._TermnlMgmtRjctn = base_types.UninitialisedField(self, 'TermnlMgmtRjctn', TerminalManagementRejectionV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TermnlMgmtRjctn', type=TerminalManagementRejectionV05, min=1, max=1, mutex_group=None, array=False),
		))