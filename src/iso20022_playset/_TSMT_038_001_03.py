# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusReportRequestV03 import StatusReportRequestV03

class TSMT_038_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_StsRptReq"]
		@property
		def StsRptReq(self):
			return self._StsRptReq

		@StsRptReq.setter
		def StsRptReq(self, value):
			self._StsRptReq = value if type(value) != base_types.auto else self.make_default("StsRptReq")

		@StsRptReq.deleter
		def StsRptReq(self):
			del self._StsRptReq
			self._StsRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsRptReq', type=StatusReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))