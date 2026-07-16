# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesMessageRejectionV04

class SEMT_001_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.001.001.04"
		_docname = "semt.001.001.04"

		__slots__ = ["_SctiesMsgRjctn"]
		@property
		def SctiesMsgRjctn(self):
			return self._SctiesMsgRjctn

		@SctiesMsgRjctn.setter
		def SctiesMsgRjctn(self, value):
			self._SctiesMsgRjctn = value if value is not None else base_types.UninitialisedField(self, 'SctiesMsgRjctn', SecuritiesMessageRejectionV04, False)

		@SctiesMsgRjctn.deleter
		def SctiesMsgRjctn(self):
			del self._SctiesMsgRjctn
			self._SctiesMsgRjctn = base_types.UninitialisedField(self, 'SctiesMsgRjctn', SecuritiesMessageRejectionV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesMsgRjctn', type=SecuritiesMessageRejectionV04, min=1, max=1, mutex_group=None, array=False),
		))