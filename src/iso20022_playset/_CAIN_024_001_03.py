# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardManagementResponseV03

class CAIN_024_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.024.001.03"
		_docname = "cain.024.001.03"

		__slots__ = ["_CardMgmtRspn"]
		@property
		def CardMgmtRspn(self):
			return self._CardMgmtRspn

		@CardMgmtRspn.setter
		def CardMgmtRspn(self, value):
			self._CardMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'CardMgmtRspn', CardManagementResponseV03, False)

		@CardMgmtRspn.deleter
		def CardMgmtRspn(self):
			del self._CardMgmtRspn
			self._CardMgmtRspn = base_types.UninitialisedField(self, 'CardMgmtRspn', CardManagementResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CardMgmtRspn', type=CardManagementResponseV03, min=1, max=1, mutex_group=None, array=False),
		))