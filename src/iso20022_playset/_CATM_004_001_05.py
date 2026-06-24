# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TerminalManagementRejectionV05 import TerminalManagementRejectionV05

class CATM_004_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catm.004.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_TermnlMgmtRjctn"]
		@property
		def TermnlMgmtRjctn(self):
			return self._TermnlMgmtRjctn

		@TermnlMgmtRjctn.setter
		def TermnlMgmtRjctn(self, value):
			self._TermnlMgmtRjctn = value if type(value) != base_types.auto else self.make_default("TermnlMgmtRjctn")

		@TermnlMgmtRjctn.deleter
		def TermnlMgmtRjctn(self):
			del self._TermnlMgmtRjctn
			self._TermnlMgmtRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TermnlMgmtRjctn', type=TerminalManagementRejectionV05, min=1, max=1, mutex_group=None, array=False),
		))