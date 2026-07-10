# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BatchManagementResponseV03 import BatchManagementResponseV03

class CAAD_002_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.002.001.03"
		_docname = "caad.002.001.03"

		__slots__ = ["_BtchMgmtRspn"]
		@property
		def BtchMgmtRspn(self):
			return self._BtchMgmtRspn

		@BtchMgmtRspn.setter
		def BtchMgmtRspn(self, value):
			self._BtchMgmtRspn = value if type(value) != base_types.auto else self.make_default("BtchMgmtRspn")

		@BtchMgmtRspn.deleter
		def BtchMgmtRspn(self):
			del self._BtchMgmtRspn
			self._BtchMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchMgmtRspn', type=BatchManagementResponseV03, min=1, max=1, mutex_group=None, array=False),
		))