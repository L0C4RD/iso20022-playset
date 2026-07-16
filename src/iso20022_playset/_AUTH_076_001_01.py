# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialSupervisedPartyIdentityReportV01

class AUTH_076_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.076.001.01"
		_docname = "auth.076.001.01"

		__slots__ = ["_FinSprvsdPtyIdntyRpt"]
		@property
		def FinSprvsdPtyIdntyRpt(self):
			return self._FinSprvsdPtyIdntyRpt

		@FinSprvsdPtyIdntyRpt.setter
		def FinSprvsdPtyIdntyRpt(self, value):
			self._FinSprvsdPtyIdntyRpt = value if value is not None else base_types.UninitialisedField(self, 'FinSprvsdPtyIdntyRpt', FinancialSupervisedPartyIdentityReportV01, False)

		@FinSprvsdPtyIdntyRpt.deleter
		def FinSprvsdPtyIdntyRpt(self):
			del self._FinSprvsdPtyIdntyRpt
			self._FinSprvsdPtyIdntyRpt = base_types.UninitialisedField(self, 'FinSprvsdPtyIdntyRpt', FinancialSupervisedPartyIdentityReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinSprvsdPtyIdntyRpt', type=FinancialSupervisedPartyIdentityReportV01, min=1, max=1, mutex_group=None, array=False),
		))