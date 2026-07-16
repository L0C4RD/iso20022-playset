# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BatchManagementResponseV04

class CAAD_002_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.002.001.04"
		_docname = "caad.002.001.04"

		__slots__ = ["_BtchMgmtRspn"]
		@property
		def BtchMgmtRspn(self):
			return self._BtchMgmtRspn

		@BtchMgmtRspn.setter
		def BtchMgmtRspn(self, value):
			self._BtchMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'BtchMgmtRspn', BatchManagementResponseV04, False)

		@BtchMgmtRspn.deleter
		def BtchMgmtRspn(self):
			del self._BtchMgmtRspn
			self._BtchMgmtRspn = base_types.UninitialisedField(self, 'BtchMgmtRspn', BatchManagementResponseV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchMgmtRspn', type=BatchManagementResponseV04, min=1, max=1, mutex_group=None, array=False),
		))