# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecurityCSDLinkMaintenanceRequestV01 import SecurityCSDLinkMaintenanceRequestV01

class REDA_046_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.046.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctyCSDLkMntncReq"]
		@property
		def SctyCSDLkMntncReq(self):
			return self._SctyCSDLkMntncReq

		@SctyCSDLkMntncReq.setter
		def SctyCSDLkMntncReq(self, value):
			self._SctyCSDLkMntncReq = value if type(value) != base_types.auto else self.make_default("SctyCSDLkMntncReq")

		@SctyCSDLkMntncReq.deleter
		def SctyCSDLkMntncReq(self):
			del self._SctyCSDLkMntncReq
			self._SctyCSDLkMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCSDLkMntncReq', type=SecurityCSDLinkMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))