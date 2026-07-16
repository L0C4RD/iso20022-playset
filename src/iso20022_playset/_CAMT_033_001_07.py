# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestForDuplicateV07

class CAMT_033_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.033.001.07"
		_docname = "camt.033.001.07"

		__slots__ = ["_ReqForDplct"]
		@property
		def ReqForDplct(self):
			return self._ReqForDplct

		@ReqForDplct.setter
		def ReqForDplct(self, value):
			self._ReqForDplct = value if value is not None else base_types.UninitialisedField(self, 'ReqForDplct', RequestForDuplicateV07, False)

		@ReqForDplct.deleter
		def ReqForDplct(self):
			del self._ReqForDplct
			self._ReqForDplct = base_types.UninitialisedField(self, 'ReqForDplct', RequestForDuplicateV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForDplct', type=RequestForDuplicateV07, min=1, max=1, mutex_group=None, array=False),
		))