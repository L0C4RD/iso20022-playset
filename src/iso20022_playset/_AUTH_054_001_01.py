# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPClearingMemberReportV01

class AUTH_054_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01"
		_docname = "auth.054.001.01"

		__slots__ = ["_CCPClrMmbRpt"]
		@property
		def CCPClrMmbRpt(self):
			return self._CCPClrMmbRpt

		@CCPClrMmbRpt.setter
		def CCPClrMmbRpt(self, value):
			self._CCPClrMmbRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPClrMmbRpt', CCPClearingMemberReportV01, False)

		@CCPClrMmbRpt.deleter
		def CCPClrMmbRpt(self):
			del self._CCPClrMmbRpt
			self._CCPClrMmbRpt = base_types.UninitialisedField(self, 'CCPClrMmbRpt', CCPClearingMemberReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPClrMmbRpt', type=CCPClearingMemberReportV01, min=1, max=1, mutex_group=None, array=False),
		))