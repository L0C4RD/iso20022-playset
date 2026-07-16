# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyModificationRequestV02

class REDA_022_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.022.001.02"
		_docname = "reda.022.001.02"

		__slots__ = ["_PtyModReq"]
		@property
		def PtyModReq(self):
			return self._PtyModReq

		@PtyModReq.setter
		def PtyModReq(self, value):
			self._PtyModReq = value if value is not None else base_types.UninitialisedField(self, 'PtyModReq', PartyModificationRequestV02, False)

		@PtyModReq.deleter
		def PtyModReq(self):
			del self._PtyModReq
			self._PtyModReq = base_types.UninitialisedField(self, 'PtyModReq', PartyModificationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyModReq', type=PartyModificationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))