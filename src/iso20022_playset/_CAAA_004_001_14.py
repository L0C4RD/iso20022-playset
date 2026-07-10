# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCompletionAdviceResponseV14 import AcceptorCompletionAdviceResponseV14

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
			self._AccptrCmpltnAdvcRspn = value if type(value) != base_types.auto else self.make_default("AccptrCmpltnAdvcRspn")

		@AccptrCmpltnAdvcRspn.deleter
		def AccptrCmpltnAdvcRspn(self):
			del self._AccptrCmpltnAdvcRspn
			self._AccptrCmpltnAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCmpltnAdvcRspn', type=AcceptorCompletionAdviceResponseV14, min=1, max=1, mutex_group=None, array=False),
		))