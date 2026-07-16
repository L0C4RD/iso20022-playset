# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CCPClearedProductReportV02

class AUTH_069_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.069.001.02"
		_docname = "auth.069.001.02"

		__slots__ = ["_CCPClrdPdctRpt"]
		@property
		def CCPClrdPdctRpt(self):
			return self._CCPClrdPdctRpt

		@CCPClrdPdctRpt.setter
		def CCPClrdPdctRpt(self, value):
			self._CCPClrdPdctRpt = value if value is not None else base_types.UninitialisedField(self, 'CCPClrdPdctRpt', CCPClearedProductReportV02, False)

		@CCPClrdPdctRpt.deleter
		def CCPClrdPdctRpt(self):
			del self._CCPClrdPdctRpt
			self._CCPClrdPdctRpt = base_types.UninitialisedField(self, 'CCPClrdPdctRpt', CCPClearedProductReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPClrdPdctRpt', type=CCPClearedProductReportV02, min=1, max=1, mutex_group=None, array=False),
		))