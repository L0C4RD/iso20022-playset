# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotificationToReceiveStatusReportV08

class CAMT_059_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.059.001.08"
		_docname = "camt.059.001.08"

		__slots__ = ["_NtfctnToRcvStsRpt"]
		@property
		def NtfctnToRcvStsRpt(self):
			return self._NtfctnToRcvStsRpt

		@NtfctnToRcvStsRpt.setter
		def NtfctnToRcvStsRpt(self, value):
			self._NtfctnToRcvStsRpt = value if value is not None else base_types.UninitialisedField(self, 'NtfctnToRcvStsRpt', NotificationToReceiveStatusReportV08, False)

		@NtfctnToRcvStsRpt.deleter
		def NtfctnToRcvStsRpt(self):
			del self._NtfctnToRcvStsRpt
			self._NtfctnToRcvStsRpt = base_types.UninitialisedField(self, 'NtfctnToRcvStsRpt', NotificationToReceiveStatusReportV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcvStsRpt', type=NotificationToReceiveStatusReportV08, min=1, max=1, mutex_group=None, array=False),
		))