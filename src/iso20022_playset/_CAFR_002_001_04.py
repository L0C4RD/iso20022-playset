# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FraudReportingResponseV04 import FraudReportingResponseV04

class CAFR_002_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cafr.002.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FrdRptgRspn"]
		@property
		def FrdRptgRspn(self):
			return self._FrdRptgRspn

		@FrdRptgRspn.setter
		def FrdRptgRspn(self, value):
			self._FrdRptgRspn = value if type(value) != base_types.auto else self.make_default("FrdRptgRspn")

		@FrdRptgRspn.deleter
		def FrdRptgRspn(self):
			del self._FrdRptgRspn
			self._FrdRptgRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdRptgRspn', type=FraudReportingResponseV04, min=1, max=1, mutex_group=None, array=False),
		))