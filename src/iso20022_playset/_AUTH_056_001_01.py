# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPMemberObligationsReportV01

class AUTH_056_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01"
		_docname = "auth.056.001.01"

		__slots__ = ["_CCPMmbOblgtnsRpt"]
		@property
		def CCPMmbOblgtnsRpt(self):
			return self._CCPMmbOblgtnsRpt

		@CCPMmbOblgtnsRpt.setter
		def CCPMmbOblgtnsRpt(self, value):
			self._CCPMmbOblgtnsRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPMmbOblgtnsRpt', CCPMemberObligationsReportV01, False)

		@CCPMmbOblgtnsRpt.deleter
		def CCPMmbOblgtnsRpt(self):
			del self._CCPMmbOblgtnsRpt
			self._CCPMmbOblgtnsRpt = base_types.UninitialisedField(self, 'CCPMmbOblgtnsRpt', CCPMemberObligationsReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPMmbOblgtnsRpt', type=CCPMemberObligationsReportV01, min=1, max=1, mutex_group=None, array=False),
		))