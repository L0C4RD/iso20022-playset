# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActivityReportSetUpRequestV02 import ActivityReportSetUpRequestV02

class TSMT_004_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ActvtyRptSetUpReq"]
		@property
		def ActvtyRptSetUpReq(self):
			return self._ActvtyRptSetUpReq

		@ActvtyRptSetUpReq.setter
		def ActvtyRptSetUpReq(self, value):
			self._ActvtyRptSetUpReq = value if type(value) != base_types.auto else self.make_default("ActvtyRptSetUpReq")

		@ActvtyRptSetUpReq.deleter
		def ActvtyRptSetUpReq(self):
			del self._ActvtyRptSetUpReq
			self._ActvtyRptSetUpReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActvtyRptSetUpReq', type=ActivityReportSetUpRequestV02, min=1, max=1, mutex_group=None, array=False),
		))