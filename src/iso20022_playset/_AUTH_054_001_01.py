# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPClearingMemberReportV01 import CCPClearingMemberReportV01

class AUTH_054_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.054.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CCPClrMmbRpt"]
		@property
		def CCPClrMmbRpt(self):
			return self._CCPClrMmbRpt

		@CCPClrMmbRpt.setter
		def CCPClrMmbRpt(self, value):
			self._CCPClrMmbRpt = value if type(value) != base_types.auto else self.make_default("CCPClrMmbRpt")

		@CCPClrMmbRpt.deleter
		def CCPClrMmbRpt(self):
			del self._CCPClrMmbRpt
			self._CCPClrMmbRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPClrMmbRpt', type=CCPClearingMemberReportV01, min=1, max=1, mutex_group=None, array=False),
		))