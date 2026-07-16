# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCompletionAdviceResponseV14

class CAAA_004_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.004.001.14"
		_docname = "caaa.004.001.14"

		__slots__ = ["_AccptrCmpltnAdvcRspn"]
		@property
		def AccptrCmpltnAdvcRspn(self):
			return self._AccptrCmpltnAdvcRspn

		@AccptrCmpltnAdvcRspn.setter
		def AccptrCmpltnAdvcRspn(self, value):
			self._AccptrCmpltnAdvcRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrCmpltnAdvcRspn', AcceptorCompletionAdviceResponseV14, False)

		@AccptrCmpltnAdvcRspn.deleter
		def AccptrCmpltnAdvcRspn(self):
			del self._AccptrCmpltnAdvcRspn
			self._AccptrCmpltnAdvcRspn = base_types.UninitialisedField(self, 'AccptrCmpltnAdvcRspn', AcceptorCompletionAdviceResponseV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCmpltnAdvcRspn', type=AcceptorCompletionAdviceResponseV14, min=1, max=1, mutex_group=None, array=False),
		))