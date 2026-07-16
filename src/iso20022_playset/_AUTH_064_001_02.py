# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPAvailableFinancialResourcesReportV02

class AUTH_064_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02"
		_docname = "auth.064.001.02"

		__slots__ = ["_CCPAvlblFinRsrcsRpt"]
		@property
		def CCPAvlblFinRsrcsRpt(self):
			return self._CCPAvlblFinRsrcsRpt

		@CCPAvlblFinRsrcsRpt.setter
		def CCPAvlblFinRsrcsRpt(self, value):
			self._CCPAvlblFinRsrcsRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPAvlblFinRsrcsRpt', CCPAvailableFinancialResourcesReportV02, False)

		@CCPAvlblFinRsrcsRpt.deleter
		def CCPAvlblFinRsrcsRpt(self):
			del self._CCPAvlblFinRsrcsRpt
			self._CCPAvlblFinRsrcsRpt = base_types.UninitialisedField(self, 'CCPAvlblFinRsrcsRpt', CCPAvailableFinancialResourcesReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPAvlblFinRsrcsRpt', type=CCPAvailableFinancialResourcesReportV02, min=1, max=1, mutex_group=None, array=False),
		))