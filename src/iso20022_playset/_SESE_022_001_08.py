# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesStatusOrStatementQueryStatusAdviceV08 import SecuritiesStatusOrStatementQueryStatusAdviceV08

class SESE_022_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.022.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesStsOrStmtQryStsAdvc"]
		@property
		def SctiesStsOrStmtQryStsAdvc(self):
			return self._SctiesStsOrStmtQryStsAdvc

		@SctiesStsOrStmtQryStsAdvc.setter
		def SctiesStsOrStmtQryStsAdvc(self, value):
			self._SctiesStsOrStmtQryStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesStsOrStmtQryStsAdvc")

		@SctiesStsOrStmtQryStsAdvc.deleter
		def SctiesStsOrStmtQryStsAdvc(self):
			del self._SctiesStsOrStmtQryStsAdvc
			self._SctiesStsOrStmtQryStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStsOrStmtQryStsAdvc', type=SecuritiesStatusOrStatementQueryStatusAdviceV08, min=1, max=1, mutex_group=None, array=False),
		))