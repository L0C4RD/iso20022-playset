# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountRequestRejectionV04

class ACMT_011_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.011.001.04"
		_docname = "acmt.011.001.04"

		__slots__ = ["_AcctReqRjctn"]
		@property
		def AcctReqRjctn(self):
			return self._AcctReqRjctn

		@AcctReqRjctn.setter
		def AcctReqRjctn(self, value):
			self._AcctReqRjctn = value if value is not None else base_types.UninitialisedField(self, 'AcctReqRjctn', AccountRequestRejectionV04, False)

		@AcctReqRjctn.deleter
		def AcctReqRjctn(self):
			del self._AcctReqRjctn
			self._AcctReqRjctn = base_types.UninitialisedField(self, 'AcctReqRjctn', AccountRequestRejectionV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctReqRjctn', type=AccountRequestRejectionV04, min=1, max=1, mutex_group=None, array=False),
		))