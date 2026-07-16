# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotificationToReceiveV08

class CAMT_057_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.057.001.08"
		_docname = "camt.057.001.08"

		__slots__ = ["_NtfctnToRcv"]
		@property
		def NtfctnToRcv(self):
			return self._NtfctnToRcv

		@NtfctnToRcv.setter
		def NtfctnToRcv(self, value):
			self._NtfctnToRcv = value if value is not None else base_types.UninitialisedField(self, 'NtfctnToRcv', NotificationToReceiveV08, False)

		@NtfctnToRcv.deleter
		def NtfctnToRcv(self):
			del self._NtfctnToRcv
			self._NtfctnToRcv = base_types.UninitialisedField(self, 'NtfctnToRcv', NotificationToReceiveV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcv', type=NotificationToReceiveV08, min=1, max=1, mutex_group=None, array=False),
		))