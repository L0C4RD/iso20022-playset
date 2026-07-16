# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPInteroperabilityReportV01

class AUTH_112_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01"
		_docname = "auth.112.001.01"

		__slots__ = ["_CCPIntrprbltyRpt"]
		@property
		def CCPIntrprbltyRpt(self):
			return self._CCPIntrprbltyRpt

		@CCPIntrprbltyRpt.setter
		def CCPIntrprbltyRpt(self, value):
			self._CCPIntrprbltyRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPIntrprbltyRpt', CCPInteroperabilityReportV01, False)

		@CCPIntrprbltyRpt.deleter
		def CCPIntrprbltyRpt(self):
			del self._CCPIntrprbltyRpt
			self._CCPIntrprbltyRpt = base_types.UninitialisedField(self, 'CCPIntrprbltyRpt', CCPInteroperabilityReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPIntrprbltyRpt', type=CCPInteroperabilityReportV01, min=1, max=1, mutex_group=None, array=False),
		))