# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInitiationV05

class CAIN_003_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.003.001.05"
		_docname = "cain.003.001.05"

		__slots__ = ["_FinInitn"]
		@property
		def FinInitn(self):
			return self._FinInitn

		@FinInitn.setter
		def FinInitn(self, value):
			self._FinInitn = value if value is not None else base_types.UninitialisedField(self, 'FinInitn', FinancialInitiationV05, False)

		@FinInitn.deleter
		def FinInitn(self):
			del self._FinInitn
			self._FinInitn = base_types.UninitialisedField(self, 'FinInitn', FinancialInitiationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInitn', type=FinancialInitiationV05, min=1, max=1, mutex_group=None, array=False),
		))