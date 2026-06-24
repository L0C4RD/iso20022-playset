# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PaymentRegulatoryInformationNotificationV04 import PaymentRegulatoryInformationNotificationV04

class AUTH_024_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.024.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_PmtRgltryInfNtfctn"]
		@property
		def PmtRgltryInfNtfctn(self):
			return self._PmtRgltryInfNtfctn

		@PmtRgltryInfNtfctn.setter
		def PmtRgltryInfNtfctn(self, value):
			self._PmtRgltryInfNtfctn = value if type(value) != base_types.auto else self.make_default("PmtRgltryInfNtfctn")

		@PmtRgltryInfNtfctn.deleter
		def PmtRgltryInfNtfctn(self):
			del self._PmtRgltryInfNtfctn
			self._PmtRgltryInfNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtRgltryInfNtfctn', type=PaymentRegulatoryInformationNotificationV04, min=1, max=1, mutex_group=None, array=False),
		))