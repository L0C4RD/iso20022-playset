# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPMemberRequirementsReportV01

class AUTH_055_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01"
		_docname = "auth.055.001.01"

		__slots__ = ["_CCPMmbRqrmntsRpt"]
		@property
		def CCPMmbRqrmntsRpt(self):
			return self._CCPMmbRqrmntsRpt

		@CCPMmbRqrmntsRpt.setter
		def CCPMmbRqrmntsRpt(self, value):
			self._CCPMmbRqrmntsRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPMmbRqrmntsRpt', CCPMemberRequirementsReportV01, False)

		@CCPMmbRqrmntsRpt.deleter
		def CCPMmbRqrmntsRpt(self):
			del self._CCPMmbRqrmntsRpt
			self._CCPMmbRqrmntsRpt = base_types.UninitialisedField(self, 'CCPMmbRqrmntsRpt', CCPMemberRequirementsReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPMmbRqrmntsRpt', type=CCPMemberRequirementsReportV01, min=1, max=1, mutex_group=None, array=False),
		))