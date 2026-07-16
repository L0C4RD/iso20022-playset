# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityCSDLinkMaintenanceRequestV01

class REDA_046_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.046.001.01"
		_docname = "reda.046.001.01"

		__slots__ = ["_SctyCSDLkMntncReq"]
		@property
		def SctyCSDLkMntncReq(self):
			return self._SctyCSDLkMntncReq

		@SctyCSDLkMntncReq.setter
		def SctyCSDLkMntncReq(self, value):
			self._SctyCSDLkMntncReq = value if value is not None else base_types.UninitialisedField(self, 'SctyCSDLkMntncReq', SecurityCSDLinkMaintenanceRequestV01, False)

		@SctyCSDLkMntncReq.deleter
		def SctyCSDLkMntncReq(self):
			del self._SctyCSDLkMntncReq
			self._SctyCSDLkMntncReq = base_types.UninitialisedField(self, 'SctyCSDLkMntncReq', SecurityCSDLinkMaintenanceRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCSDLkMntncReq', type=SecurityCSDLinkMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))