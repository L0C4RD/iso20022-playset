# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountLinkStatusAdviceV01

class REDA_051_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01"
		_docname = "reda.051.001.01"

		__slots__ = ["_AcctLkStsAdvc"]
		@property
		def AcctLkStsAdvc(self):
			return self._AcctLkStsAdvc

		@AcctLkStsAdvc.setter
		def AcctLkStsAdvc(self, value):
			self._AcctLkStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AcctLkStsAdvc', AccountLinkStatusAdviceV01, False)

		@AcctLkStsAdvc.deleter
		def AcctLkStsAdvc(self):
			del self._AcctLkStsAdvc
			self._AcctLkStsAdvc = base_types.UninitialisedField(self, 'AcctLkStsAdvc', AccountLinkStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkStsAdvc', type=AccountLinkStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))