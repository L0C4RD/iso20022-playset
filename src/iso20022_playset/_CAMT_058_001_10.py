# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotificationToReceiveCancellationAdviceV10

class CAMT_058_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.058.001.10"
		_docname = "camt.058.001.10"

		__slots__ = ["_NtfctnToRcvCxlAdvc"]
		@property
		def NtfctnToRcvCxlAdvc(self):
			return self._NtfctnToRcvCxlAdvc

		@NtfctnToRcvCxlAdvc.setter
		def NtfctnToRcvCxlAdvc(self, value):
			self._NtfctnToRcvCxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'NtfctnToRcvCxlAdvc', NotificationToReceiveCancellationAdviceV10, False)

		@NtfctnToRcvCxlAdvc.deleter
		def NtfctnToRcvCxlAdvc(self):
			del self._NtfctnToRcvCxlAdvc
			self._NtfctnToRcvCxlAdvc = base_types.UninitialisedField(self, 'NtfctnToRcvCxlAdvc', NotificationToReceiveCancellationAdviceV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcvCxlAdvc', type=NotificationToReceiveCancellationAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))