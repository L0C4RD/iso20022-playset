# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationVerificationReportV04

class ACMT_024_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.024.001.04"
		_docname = "acmt.024.001.04"

		__slots__ = ["_IdVrfctnRpt"]
		@property
		def IdVrfctnRpt(self):
			return self._IdVrfctnRpt

		@IdVrfctnRpt.setter
		def IdVrfctnRpt(self, value):
			self._IdVrfctnRpt = value if value is not None else base_types.UninitialisedField(self, 'IdVrfctnRpt', IdentificationVerificationReportV04, False)

		@IdVrfctnRpt.deleter
		def IdVrfctnRpt(self):
			del self._IdVrfctnRpt
			self._IdVrfctnRpt = base_types.UninitialisedField(self, 'IdVrfctnRpt', IdentificationVerificationReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IdVrfctnRpt', type=IdentificationVerificationReportV04, min=1, max=1, mutex_group=None, array=False),
		))