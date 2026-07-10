# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CustomerDirectDebitInitiationV11 import CustomerDirectDebitInitiationV11

class PAIN_008_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.008.001.11"
		_docname = "pain.008.001.11"

		__slots__ = ["_CstmrDrctDbtInitn"]
		@property
		def CstmrDrctDbtInitn(self):
			return self._CstmrDrctDbtInitn

		@CstmrDrctDbtInitn.setter
		def CstmrDrctDbtInitn(self, value):
			self._CstmrDrctDbtInitn = value if type(value) != base_types.auto else self.make_default("CstmrDrctDbtInitn")

		@CstmrDrctDbtInitn.deleter
		def CstmrDrctDbtInitn(self):
			del self._CstmrDrctDbtInitn
			self._CstmrDrctDbtInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrDrctDbtInitn', type=CustomerDirectDebitInitiationV11, min=1, max=1, mutex_group=None, array=False),
		))