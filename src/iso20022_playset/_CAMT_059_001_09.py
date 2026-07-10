# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NotificationToReceiveStatusReportV09 import NotificationToReceiveStatusReportV09

class CAMT_059_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.059.001.09"
		_docname = "camt.059.001.09"

		__slots__ = ["_NtfctnToRcvStsRpt"]
		@property
		def NtfctnToRcvStsRpt(self):
			return self._NtfctnToRcvStsRpt

		@NtfctnToRcvStsRpt.setter
		def NtfctnToRcvStsRpt(self, value):
			self._NtfctnToRcvStsRpt = value if type(value) != base_types.auto else self.make_default("NtfctnToRcvStsRpt")

		@NtfctnToRcvStsRpt.deleter
		def NtfctnToRcvStsRpt(self):
			del self._NtfctnToRcvStsRpt
			self._NtfctnToRcvStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcvStsRpt', type=NotificationToReceiveStatusReportV09, min=1, max=1, mutex_group=None, array=False),
		))