# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyRegistrationAndGuaranteeNotificationV01

class TSIN_011_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.011.001.01"
		_docname = "tsin.011.001.01"

		__slots__ = ["_PtyRegnAndGrntNtfctn"]
		@property
		def PtyRegnAndGrntNtfctn(self):
			return self._PtyRegnAndGrntNtfctn

		@PtyRegnAndGrntNtfctn.setter
		def PtyRegnAndGrntNtfctn(self, value):
			self._PtyRegnAndGrntNtfctn = value if value is not None else base_types.UninitialisedField(self, 'PtyRegnAndGrntNtfctn', PartyRegistrationAndGuaranteeNotificationV01, False)

		@PtyRegnAndGrntNtfctn.deleter
		def PtyRegnAndGrntNtfctn(self):
			del self._PtyRegnAndGrntNtfctn
			self._PtyRegnAndGrntNtfctn = base_types.UninitialisedField(self, 'PtyRegnAndGrntNtfctn', PartyRegistrationAndGuaranteeNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntNtfctn', type=PartyRegistrationAndGuaranteeNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))