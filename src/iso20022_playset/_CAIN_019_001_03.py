# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import VerificationResponseV03

class CAIN_019_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.019.001.03"
		_docname = "cain.019.001.03"

		__slots__ = ["_VrfctnRspn"]
		@property
		def VrfctnRspn(self):
			return self._VrfctnRspn

		@VrfctnRspn.setter
		def VrfctnRspn(self, value):
			self._VrfctnRspn = value if value is not None else base_types.UninitialisedField(self, 'VrfctnRspn', VerificationResponseV03, False)

		@VrfctnRspn.deleter
		def VrfctnRspn(self):
			del self._VrfctnRspn
			self._VrfctnRspn = base_types.UninitialisedField(self, 'VrfctnRspn', VerificationResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='VrfctnRspn', type=VerificationResponseV03, min=1, max=1, mutex_group=None, array=False),
		))