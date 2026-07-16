# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPBackTestingResultReportV01

class AUTH_066_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01"
		_docname = "auth.066.001.01"

		__slots__ = ["_CCPBckTstgRsltRpt"]
		@property
		def CCPBckTstgRsltRpt(self):
			return self._CCPBckTstgRsltRpt

		@CCPBckTstgRsltRpt.setter
		def CCPBckTstgRsltRpt(self, value):
			self._CCPBckTstgRsltRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPBckTstgRsltRpt', CCPBackTestingResultReportV01, False)

		@CCPBckTstgRsltRpt.deleter
		def CCPBckTstgRsltRpt(self):
			del self._CCPBckTstgRsltRpt
			self._CCPBckTstgRsltRpt = base_types.UninitialisedField(self, 'CCPBckTstgRsltRpt', CCPBackTestingResultReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPBckTstgRsltRpt', type=CCPBackTestingResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))