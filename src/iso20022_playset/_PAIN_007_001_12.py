# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CustomerPaymentReversalV12 import CustomerPaymentReversalV12

class PAIN_007_001_12():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:pain.007.001.12",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CstmrPmtRvsl"]
		@property
		def CstmrPmtRvsl(self):
			return self._CstmrPmtRvsl

		@CstmrPmtRvsl.setter
		def CstmrPmtRvsl(self, value):
			self._CstmrPmtRvsl = value if type(value) != base_types.auto else self.make_default("CstmrPmtRvsl")

		@CstmrPmtRvsl.deleter
		def CstmrPmtRvsl(self):
			del self._CstmrPmtRvsl
			self._CstmrPmtRvsl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtRvsl', type=CustomerPaymentReversalV12, min=1, max=1, mutex_group=None, array=False),
		))