# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialResponseV05

class CAIN_004_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.004.001.05"
		_docname = "cain.004.001.05"

		__slots__ = ["_FinRspn"]
		@property
		def FinRspn(self):
			return self._FinRspn

		@FinRspn.setter
		def FinRspn(self, value):
			self._FinRspn = value if value is not None else base_types.UninitialisedField(self, 'FinRspn', FinancialResponseV05, False)

		@FinRspn.deleter
		def FinRspn(self):
			del self._FinRspn
			self._FinRspn = base_types.UninitialisedField(self, 'FinRspn', FinancialResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinRspn', type=FinancialResponseV05, min=1, max=1, mutex_group=None, array=False),
		))