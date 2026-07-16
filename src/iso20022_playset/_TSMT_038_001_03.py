# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusReportRequestV03

class TSMT_038_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03"
		_docname = "tsmt.038.001.03"

		__slots__ = ["_StsRptReq"]
		@property
		def StsRptReq(self):
			return self._StsRptReq

		@StsRptReq.setter
		def StsRptReq(self, value):
			self._StsRptReq = value if value is not None else base_types.UninitialisedField(self, 'StsRptReq', StatusReportRequestV03, False)

		@StsRptReq.deleter
		def StsRptReq(self):
			del self._StsRptReq
			self._StsRptReq = base_types.UninitialisedField(self, 'StsRptReq', StatusReportRequestV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsRptReq', type=StatusReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))