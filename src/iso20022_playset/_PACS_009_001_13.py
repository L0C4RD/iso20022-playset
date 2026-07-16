# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstitutionCreditTransferV13

class PACS_009_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13"
		_docname = "pacs.009.001.13"

		__slots__ = ["_FICdtTrf"]
		@property
		def FICdtTrf(self):
			return self._FICdtTrf

		@FICdtTrf.setter
		def FICdtTrf(self, value):
			self._FICdtTrf = value if value is not None else base_types.UninitialisedField(self, 'FICdtTrf', FinancialInstitutionCreditTransferV13, False)

		@FICdtTrf.deleter
		def FICdtTrf(self):
			del self._FICdtTrf
			self._FICdtTrf = base_types.UninitialisedField(self, 'FICdtTrf', FinancialInstitutionCreditTransferV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FICdtTrf', type=FinancialInstitutionCreditTransferV13, min=1, max=1, mutex_group=None, array=False),
		))