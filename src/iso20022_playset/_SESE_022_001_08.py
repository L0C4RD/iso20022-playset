# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesStatusOrStatementQueryStatusAdviceV08

class SESE_022_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.022.001.08"
		_docname = "sese.022.001.08"

		__slots__ = ["_SctiesStsOrStmtQryStsAdvc"]
		@property
		def SctiesStsOrStmtQryStsAdvc(self):
			return self._SctiesStsOrStmtQryStsAdvc

		@SctiesStsOrStmtQryStsAdvc.setter
		def SctiesStsOrStmtQryStsAdvc(self, value):
			self._SctiesStsOrStmtQryStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesStsOrStmtQryStsAdvc', SecuritiesStatusOrStatementQueryStatusAdviceV08, False)

		@SctiesStsOrStmtQryStsAdvc.deleter
		def SctiesStsOrStmtQryStsAdvc(self):
			del self._SctiesStsOrStmtQryStsAdvc
			self._SctiesStsOrStmtQryStsAdvc = base_types.UninitialisedField(self, 'SctiesStsOrStmtQryStsAdvc', SecuritiesStatusOrStatementQueryStatusAdviceV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStsOrStmtQryStsAdvc', type=SecuritiesStatusOrStatementQueryStatusAdviceV08, min=1, max=1, mutex_group=None, array=False),
		))