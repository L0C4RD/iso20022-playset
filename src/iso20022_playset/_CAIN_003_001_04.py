# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInitiationV04

class CAIN_003_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04"
		_docname = "cain.003.001.04"

		__slots__ = ["_FinInitn"]
		@property
		def FinInitn(self):
			return self._FinInitn

		@FinInitn.setter
		def FinInitn(self, value):
			self._FinInitn = value if value is not None else base_types.UninitialisedField(self, 'FinInitn', FinancialInitiationV04, False)

		@FinInitn.deleter
		def FinInitn(self):
			del self._FinInitn
			self._FinInitn = base_types.UninitialisedField(self, 'FinInitn', FinancialInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInitn', type=FinancialInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))