# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyDeletionRequestV01

class REDA_031_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.031.001.01"
		_docname = "reda.031.001.01"

		__slots__ = ["_PtyDeltnReq"]
		@property
		def PtyDeltnReq(self):
			return self._PtyDeltnReq

		@PtyDeltnReq.setter
		def PtyDeltnReq(self, value):
			self._PtyDeltnReq = value if value is not None else base_types.UninitialisedField(self, 'PtyDeltnReq', PartyDeletionRequestV01, False)

		@PtyDeltnReq.deleter
		def PtyDeltnReq(self):
			del self._PtyDeltnReq
			self._PtyDeltnReq = base_types.UninitialisedField(self, 'PtyDeltnReq', PartyDeletionRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyDeltnReq', type=PartyDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))