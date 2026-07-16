# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivityReportV04

class TSMT_002_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04"
		_docname = "tsmt.002.001.04"

		__slots__ = ["_ActvtyRpt"]
		@property
		def ActvtyRpt(self):
			return self._ActvtyRpt

		@ActvtyRpt.setter
		def ActvtyRpt(self, value):
			self._ActvtyRpt = value if value is not None else base_types.UninitialisedField(self, 'ActvtyRpt', ActivityReportV04, False)

		@ActvtyRpt.deleter
		def ActvtyRpt(self):
			del self._ActvtyRpt
			self._ActvtyRpt = base_types.UninitialisedField(self, 'ActvtyRpt', ActivityReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActvtyRpt', type=ActivityReportV04, min=1, max=1, mutex_group=None, array=False),
		))