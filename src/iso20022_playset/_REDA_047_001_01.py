# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityCSDLinkStatusAdviceV01

class REDA_047_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.047.001.01"
		_docname = "reda.047.001.01"

		__slots__ = ["_SctyCSDLkStsAdvc"]
		@property
		def SctyCSDLkStsAdvc(self):
			return self._SctyCSDLkStsAdvc

		@SctyCSDLkStsAdvc.setter
		def SctyCSDLkStsAdvc(self, value):
			self._SctyCSDLkStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctyCSDLkStsAdvc', SecurityCSDLinkStatusAdviceV01, False)

		@SctyCSDLkStsAdvc.deleter
		def SctyCSDLkStsAdvc(self):
			del self._SctyCSDLkStsAdvc
			self._SctyCSDLkStsAdvc = base_types.UninitialisedField(self, 'SctyCSDLkStsAdvc', SecurityCSDLinkStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCSDLkStsAdvc', type=SecurityCSDLinkStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))