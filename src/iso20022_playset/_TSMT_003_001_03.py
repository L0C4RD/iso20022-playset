# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivityReportRequestV03

class TSMT_003_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03"
		_docname = "tsmt.003.001.03"

		__slots__ = ["_ActvtyReqRpt"]
		@property
		def ActvtyReqRpt(self):
			return self._ActvtyReqRpt

		@ActvtyReqRpt.setter
		def ActvtyReqRpt(self, value):
			self._ActvtyReqRpt = value if value is not None else base_types.UninitialisedField(self, 'ActvtyReqRpt', ActivityReportRequestV03, False)

		@ActvtyReqRpt.deleter
		def ActvtyReqRpt(self):
			del self._ActvtyReqRpt
			self._ActvtyReqRpt = base_types.UninitialisedField(self, 'ActvtyReqRpt', ActivityReportRequestV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActvtyReqRpt', type=ActivityReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))