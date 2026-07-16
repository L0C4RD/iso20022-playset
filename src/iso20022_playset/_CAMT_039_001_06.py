# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CaseStatusReportV06

class CAMT_039_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.039.001.06"
		_docname = "camt.039.001.06"

		__slots__ = ["_CaseStsRpt"]
		@property
		def CaseStsRpt(self):
			return self._CaseStsRpt

		@CaseStsRpt.setter
		def CaseStsRpt(self, value):
			self._CaseStsRpt = value if value is not None else base_types.UninitialisedField(self, 'CaseStsRpt', CaseStatusReportV06, False)

		@CaseStsRpt.deleter
		def CaseStsRpt(self):
			del self._CaseStsRpt
			self._CaseStsRpt = base_types.UninitialisedField(self, 'CaseStsRpt', CaseStatusReportV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CaseStsRpt', type=CaseStatusReportV06, min=1, max=1, mutex_group=None, array=False),
		))