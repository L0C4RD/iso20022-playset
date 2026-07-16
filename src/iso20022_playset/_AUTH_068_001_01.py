# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPAccountPositionReportV01

class AUTH_068_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01"
		_docname = "auth.068.001.01"

		__slots__ = ["_CCPAcctPosRpt"]
		@property
		def CCPAcctPosRpt(self):
			return self._CCPAcctPosRpt

		@CCPAcctPosRpt.setter
		def CCPAcctPosRpt(self, value):
			self._CCPAcctPosRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPAcctPosRpt', CCPAccountPositionReportV01, False)

		@CCPAcctPosRpt.deleter
		def CCPAcctPosRpt(self):
			del self._CCPAcctPosRpt
			self._CCPAcctPosRpt = base_types.UninitialisedField(self, 'CCPAcctPosRpt', CCPAccountPositionReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPAcctPosRpt', type=CCPAccountPositionReportV01, min=1, max=1, mutex_group=None, array=False),
		))