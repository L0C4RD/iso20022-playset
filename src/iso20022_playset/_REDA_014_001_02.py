# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyCreationRequestV02

class REDA_014_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.014.001.02"
		_docname = "reda.014.001.02"

		__slots__ = ["_PtyCreReq"]
		@property
		def PtyCreReq(self):
			return self._PtyCreReq

		@PtyCreReq.setter
		def PtyCreReq(self, value):
			self._PtyCreReq = value if value is not None else base_types.UninitialisedField(self, 'PtyCreReq', PartyCreationRequestV02, False)

		@PtyCreReq.deleter
		def PtyCreReq(self):
			del self._PtyCreReq
			self._PtyCreReq = base_types.UninitialisedField(self, 'PtyCreReq', PartyCreationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyCreReq', type=PartyCreationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))