# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CustomerCreditTransferInitiationV13 import CustomerCreditTransferInitiationV13

class PAIN_001_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.001.001.13"
		_docname = "pain.001.001.13"

		__slots__ = ["_CstmrCdtTrfInitn"]
		@property
		def CstmrCdtTrfInitn(self):
			return self._CstmrCdtTrfInitn

		@CstmrCdtTrfInitn.setter
		def CstmrCdtTrfInitn(self, value):
			self._CstmrCdtTrfInitn = value if type(value) != base_types.auto else self.make_default("CstmrCdtTrfInitn")

		@CstmrCdtTrfInitn.deleter
		def CstmrCdtTrfInitn(self):
			del self._CstmrCdtTrfInitn
			self._CstmrCdtTrfInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrCdtTrfInitn', type=CustomerCreditTransferInitiationV13, min=1, max=1, mutex_group=None, array=False),
		))