# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentRegulatoryInformationNotificationV04

class AUTH_024_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.024.001.04"
		_docname = "auth.024.001.04"

		__slots__ = ["_PmtRgltryInfNtfctn"]
		@property
		def PmtRgltryInfNtfctn(self):
			return self._PmtRgltryInfNtfctn

		@PmtRgltryInfNtfctn.setter
		def PmtRgltryInfNtfctn(self, value):
			self._PmtRgltryInfNtfctn = value if value is not None else base_types.UninitialisedField(self, 'PmtRgltryInfNtfctn', PaymentRegulatoryInformationNotificationV04, False)

		@PmtRgltryInfNtfctn.deleter
		def PmtRgltryInfNtfctn(self):
			del self._PmtRgltryInfNtfctn
			self._PmtRgltryInfNtfctn = base_types.UninitialisedField(self, 'PmtRgltryInfNtfctn', PaymentRegulatoryInformationNotificationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtRgltryInfNtfctn', type=PaymentRegulatoryInformationNotificationV04, min=1, max=1, mutex_group=None, array=False),
		))