# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestToModifyPaymentV09

class CAMT_087_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.087.001.09"
		_docname = "camt.087.001.09"

		__slots__ = ["_ReqToModfyPmt"]
		@property
		def ReqToModfyPmt(self):
			return self._ReqToModfyPmt

		@ReqToModfyPmt.setter
		def ReqToModfyPmt(self, value):
			self._ReqToModfyPmt = value if value is not None else base_types.UninitialisedField(self, 'ReqToModfyPmt', RequestToModifyPaymentV09, False)

		@ReqToModfyPmt.deleter
		def ReqToModfyPmt(self):
			del self._ReqToModfyPmt
			self._ReqToModfyPmt = base_types.UninitialisedField(self, 'ReqToModfyPmt', RequestToModifyPaymentV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToModfyPmt', type=RequestToModifyPaymentV09, min=1, max=1, mutex_group=None, array=False),
		))