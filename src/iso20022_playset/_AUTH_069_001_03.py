# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPClearedProductReportV03 import CCPClearedProductReportV03

class AUTH_069_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.069.001.03"
		_docname = "auth.069.001.03"

		__slots__ = ["_CCPClrdPdctRpt"]
		@property
		def CCPClrdPdctRpt(self):
			return self._CCPClrdPdctRpt

		@CCPClrdPdctRpt.setter
		def CCPClrdPdctRpt(self, value):
			self._CCPClrdPdctRpt = value if type(value) != base_types.auto else self.make_default("CCPClrdPdctRpt")

		@CCPClrdPdctRpt.deleter
		def CCPClrdPdctRpt(self):
			del self._CCPClrdPdctRpt
			self._CCPClrdPdctRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPClrdPdctRpt', type=CCPClearedProductReportV03, min=1, max=1, mutex_group=None, array=False),
		))