# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyRegistrationAndGuaranteeAcknowledgementV01 import PartyRegistrationAndGuaranteeAcknowledgementV01

class TSIN_012_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.012.001.01"
		_docname = "tsin.012.001.01"

		__slots__ = ["_PtyRegnAndGrntAck"]
		@property
		def PtyRegnAndGrntAck(self):
			return self._PtyRegnAndGrntAck

		@PtyRegnAndGrntAck.setter
		def PtyRegnAndGrntAck(self, value):
			self._PtyRegnAndGrntAck = value if type(value) != base_types.auto else self.make_default("PtyRegnAndGrntAck")

		@PtyRegnAndGrntAck.deleter
		def PtyRegnAndGrntAck(self):
			del self._PtyRegnAndGrntAck
			self._PtyRegnAndGrntAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntAck', type=PartyRegistrationAndGuaranteeAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))