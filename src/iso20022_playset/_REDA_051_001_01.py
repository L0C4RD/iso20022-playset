# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountLinkStatusAdviceV01 import AccountLinkStatusAdviceV01

class REDA_051_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.051.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctLkStsAdvc"]
		@property
		def AcctLkStsAdvc(self):
			return self._AcctLkStsAdvc

		@AcctLkStsAdvc.setter
		def AcctLkStsAdvc(self, value):
			self._AcctLkStsAdvc = value if type(value) != base_types.auto else self.make_default("AcctLkStsAdvc")

		@AcctLkStsAdvc.deleter
		def AcctLkStsAdvc(self):
			del self._AcctLkStsAdvc
			self._AcctLkStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkStsAdvc', type=AccountLinkStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))