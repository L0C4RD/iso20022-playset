# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NetworkManagementResponseV05 import NetworkManagementResponseV05

class CANM_002_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:canm.002.001.05"
		_docname = "canm.002.001.05"

		__slots__ = ["_NtwkMgmtRspn"]
		@property
		def NtwkMgmtRspn(self):
			return self._NtwkMgmtRspn

		@NtwkMgmtRspn.setter
		def NtwkMgmtRspn(self, value):
			self._NtwkMgmtRspn = value if type(value) != base_types.auto else self.make_default("NtwkMgmtRspn")

		@NtwkMgmtRspn.deleter
		def NtwkMgmtRspn(self):
			del self._NtwkMgmtRspn
			self._NtwkMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtwkMgmtRspn', type=NetworkManagementResponseV05, min=1, max=1, mutex_group=None, array=False),
		))