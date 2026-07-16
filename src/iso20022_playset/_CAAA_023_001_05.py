# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorNonFinancialResponseV05

class CAAA_023_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.023.001.05"
		_docname = "caaa.023.001.05"

		__slots__ = ["_AccptrNonFinRspn"]
		@property
		def AccptrNonFinRspn(self):
			return self._AccptrNonFinRspn

		@AccptrNonFinRspn.setter
		def AccptrNonFinRspn(self, value):
			self._AccptrNonFinRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrNonFinRspn', AcceptorNonFinancialResponseV05, False)

		@AccptrNonFinRspn.deleter
		def AccptrNonFinRspn(self):
			del self._AccptrNonFinRspn
			self._AccptrNonFinRspn = base_types.UninitialisedField(self, 'AccptrNonFinRspn', AcceptorNonFinancialResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrNonFinRspn', type=AcceptorNonFinancialResponseV05, min=1, max=1, mutex_group=None, array=False),
		))