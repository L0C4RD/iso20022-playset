# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyRegistrationAndGuaranteeStatusV01

class TSIN_010_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01"
		_docname = "tsin.010.001.01"

		__slots__ = ["_PtyRegnAndGrntSts"]
		@property
		def PtyRegnAndGrntSts(self):
			return self._PtyRegnAndGrntSts

		@PtyRegnAndGrntSts.setter
		def PtyRegnAndGrntSts(self, value):
			self._PtyRegnAndGrntSts = value if value is not None else base_types.UninitialisedField(self, 'PtyRegnAndGrntSts', PartyRegistrationAndGuaranteeStatusV01, False)

		@PtyRegnAndGrntSts.deleter
		def PtyRegnAndGrntSts(self):
			del self._PtyRegnAndGrntSts
			self._PtyRegnAndGrntSts = base_types.UninitialisedField(self, 'PtyRegnAndGrntSts', PartyRegistrationAndGuaranteeStatusV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntSts', type=PartyRegistrationAndGuaranteeStatusV01, min=1, max=1, mutex_group=None, array=False),
		))