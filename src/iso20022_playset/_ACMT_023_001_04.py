# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationVerificationRequestV04

class ACMT_023_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.023.001.04"
		_docname = "acmt.023.001.04"

		__slots__ = ["_IdVrfctnReq"]
		@property
		def IdVrfctnReq(self):
			return self._IdVrfctnReq

		@IdVrfctnReq.setter
		def IdVrfctnReq(self, value):
			self._IdVrfctnReq = value if value is not None else base_types.UninitialisedField(self, 'IdVrfctnReq', IdentificationVerificationRequestV04, False)

		@IdVrfctnReq.deleter
		def IdVrfctnReq(self):
			del self._IdVrfctnReq
			self._IdVrfctnReq = base_types.UninitialisedField(self, 'IdVrfctnReq', IdentificationVerificationRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IdVrfctnReq', type=IdentificationVerificationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))