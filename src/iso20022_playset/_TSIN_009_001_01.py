# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyRegistrationAndGuaranteeRequestV01

class TSIN_009_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.009.001.01"
		_docname = "tsin.009.001.01"

		__slots__ = ["_PtyRegnAndGrntReq"]
		@property
		def PtyRegnAndGrntReq(self):
			return self._PtyRegnAndGrntReq

		@PtyRegnAndGrntReq.setter
		def PtyRegnAndGrntReq(self, value):
			self._PtyRegnAndGrntReq = value if value is not None else base_types.UninitialisedField(self, 'PtyRegnAndGrntReq', PartyRegistrationAndGuaranteeRequestV01, False)

		@PtyRegnAndGrntReq.deleter
		def PtyRegnAndGrntReq(self):
			del self._PtyRegnAndGrntReq
			self._PtyRegnAndGrntReq = base_types.UninitialisedField(self, 'PtyRegnAndGrntReq', PartyRegistrationAndGuaranteeRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntReq', type=PartyRegistrationAndGuaranteeRequestV01, min=1, max=1, mutex_group=None, array=False),
		))