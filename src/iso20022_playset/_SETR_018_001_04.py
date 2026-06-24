# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RequestForOrderStatusReportV04 import RequestForOrderStatusReportV04

class SETR_018_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.018.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ReqForOrdrStsRpt"]
		@property
		def ReqForOrdrStsRpt(self):
			return self._ReqForOrdrStsRpt

		@ReqForOrdrStsRpt.setter
		def ReqForOrdrStsRpt(self, value):
			self._ReqForOrdrStsRpt = value if type(value) != base_types.auto else self.make_default("ReqForOrdrStsRpt")

		@ReqForOrdrStsRpt.deleter
		def ReqForOrdrStsRpt(self):
			del self._ReqForOrdrStsRpt
			self._ReqForOrdrStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForOrdrStsRpt', type=RequestForOrderStatusReportV04, min=1, max=1, mutex_group=None, array=False),
		))