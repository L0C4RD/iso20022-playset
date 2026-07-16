# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityCSDLinkCreationRequestV01

class REDA_045_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01"
		_docname = "reda.045.001.01"

		__slots__ = ["_SctyCSDLkCreReq"]
		@property
		def SctyCSDLkCreReq(self):
			return self._SctyCSDLkCreReq

		@SctyCSDLkCreReq.setter
		def SctyCSDLkCreReq(self, value):
			self._SctyCSDLkCreReq = value if value is not None else base_types.UninitialisedField(self, 'SctyCSDLkCreReq', SecurityCSDLinkCreationRequestV01, False)

		@SctyCSDLkCreReq.deleter
		def SctyCSDLkCreReq(self):
			del self._SctyCSDLkCreReq
			self._SctyCSDLkCreReq = base_types.UninitialisedField(self, 'SctyCSDLkCreReq', SecurityCSDLinkCreationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCSDLkCreReq', type=SecurityCSDLinkCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))