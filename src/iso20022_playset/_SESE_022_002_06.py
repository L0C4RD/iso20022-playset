# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesStatusOrStatementQueryStatusAdvice002V06

class SESE_022_002_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.022.002.06"
		_docname = "sese.022.002.06"

		__slots__ = ["_SctiesStsOrStmtQryStsAdvc"]
		@property
		def SctiesStsOrStmtQryStsAdvc(self):
			return self._SctiesStsOrStmtQryStsAdvc

		@SctiesStsOrStmtQryStsAdvc.setter
		def SctiesStsOrStmtQryStsAdvc(self, value):
			self._SctiesStsOrStmtQryStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesStsOrStmtQryStsAdvc', SecuritiesStatusOrStatementQueryStatusAdvice002V06, False)

		@SctiesStsOrStmtQryStsAdvc.deleter
		def SctiesStsOrStmtQryStsAdvc(self):
			del self._SctiesStsOrStmtQryStsAdvc
			self._SctiesStsOrStmtQryStsAdvc = base_types.UninitialisedField(self, 'SctiesStsOrStmtQryStsAdvc', SecuritiesStatusOrStatementQueryStatusAdvice002V06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStsOrStmtQryStsAdvc', type=SecuritiesStatusOrStatementQueryStatusAdvice002V06, min=1, max=1, mutex_group=None, array=False),
		))