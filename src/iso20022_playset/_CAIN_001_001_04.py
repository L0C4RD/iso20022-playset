# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorisationInitiationV04

class CAIN_001_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.001.001.04"
		_docname = "cain.001.001.04"

		__slots__ = ["_AuthstnInitn"]
		@property
		def AuthstnInitn(self):
			return self._AuthstnInitn

		@AuthstnInitn.setter
		def AuthstnInitn(self, value):
			self._AuthstnInitn = value if value is not None else base_types.UninitialisedField(self, 'AuthstnInitn', AuthorisationInitiationV04, False)

		@AuthstnInitn.deleter
		def AuthstnInitn(self):
			del self._AuthstnInitn
			self._AuthstnInitn = base_types.UninitialisedField(self, 'AuthstnInitn', AuthorisationInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AuthstnInitn', type=AuthorisationInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))