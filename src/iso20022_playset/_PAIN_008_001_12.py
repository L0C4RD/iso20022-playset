# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerDirectDebitInitiationV12

class PAIN_008_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.008.001.12"
		_docname = "pain.008.001.12"

		__slots__ = ["_CstmrDrctDbtInitn"]
		@property
		def CstmrDrctDbtInitn(self):
			return self._CstmrDrctDbtInitn

		@CstmrDrctDbtInitn.setter
		def CstmrDrctDbtInitn(self, value):
			self._CstmrDrctDbtInitn = value if value is not None else base_types.UninitialisedField(self, 'CstmrDrctDbtInitn', CustomerDirectDebitInitiationV12, False)

		@CstmrDrctDbtInitn.deleter
		def CstmrDrctDbtInitn(self):
			del self._CstmrDrctDbtInitn
			self._CstmrDrctDbtInitn = base_types.UninitialisedField(self, 'CstmrDrctDbtInitn', CustomerDirectDebitInitiationV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrDrctDbtInitn', type=CustomerDirectDebitInitiationV12, min=1, max=1, mutex_group=None, array=False),
		))