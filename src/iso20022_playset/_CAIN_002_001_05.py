# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorisationResponseV05

class CAIN_002_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.002.001.05"
		_docname = "cain.002.001.05"

		__slots__ = ["_AuthstnRspn"]
		@property
		def AuthstnRspn(self):
			return self._AuthstnRspn

		@AuthstnRspn.setter
		def AuthstnRspn(self, value):
			self._AuthstnRspn = value if value is not None else base_types.UninitialisedField(self, 'AuthstnRspn', AuthorisationResponseV05, False)

		@AuthstnRspn.deleter
		def AuthstnRspn(self):
			del self._AuthstnRspn
			self._AuthstnRspn = base_types.UninitialisedField(self, 'AuthstnRspn', AuthorisationResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AuthstnRspn', type=AuthorisationResponseV05, min=1, max=1, mutex_group=None, array=False),
		))