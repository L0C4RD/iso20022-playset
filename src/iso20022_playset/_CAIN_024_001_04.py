# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardManagementResponseV04 import CardManagementResponseV04

class CAIN_024_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cain.024.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CardMgmtRspn"]
		@property
		def CardMgmtRspn(self):
			return self._CardMgmtRspn

		@CardMgmtRspn.setter
		def CardMgmtRspn(self, value):
			self._CardMgmtRspn = value if type(value) != base_types.auto else self.make_default("CardMgmtRspn")

		@CardMgmtRspn.deleter
		def CardMgmtRspn(self):
			del self._CardMgmtRspn
			self._CardMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CardMgmtRspn', type=CardManagementResponseV04, min=1, max=1, mutex_group=None, array=False),
		))