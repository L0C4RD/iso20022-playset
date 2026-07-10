# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstitutionDirectDebitV06 import FinancialInstitutionDirectDebitV06

class PACS_010_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06"
		_docname = "pacs.010.001.06"

		__slots__ = ["_FIDrctDbt"]
		@property
		def FIDrctDbt(self):
			return self._FIDrctDbt

		@FIDrctDbt.setter
		def FIDrctDbt(self, value):
			self._FIDrctDbt = value if type(value) != base_types.auto else self.make_default("FIDrctDbt")

		@FIDrctDbt.deleter
		def FIDrctDbt(self):
			del self._FIDrctDbt
			self._FIDrctDbt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIDrctDbt', type=FinancialInstitutionDirectDebitV06, min=1, max=1, mutex_group=None, array=False),
		))