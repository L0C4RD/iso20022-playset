# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMReconciliationAcknowledgementV03 import ATMReconciliationAcknowledgementV03

class CAAM_010_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.010.001.03"
		_docname = "caam.010.001.03"

		__slots__ = ["_ATMRcncltnAck"]
		@property
		def ATMRcncltnAck(self):
			return self._ATMRcncltnAck

		@ATMRcncltnAck.setter
		def ATMRcncltnAck(self, value):
			self._ATMRcncltnAck = value if type(value) != base_types.auto else self.make_default("ATMRcncltnAck")

		@ATMRcncltnAck.deleter
		def ATMRcncltnAck(self):
			del self._ATMRcncltnAck
			self._ATMRcncltnAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnAck', type=ATMReconciliationAcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))