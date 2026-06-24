# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NotificationToReceiveStatusReportV08 import NotificationToReceiveStatusReportV08

class CAMT_059_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.059.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

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
			base_types.FieldEntry(name='NtfctnToRcvStsRpt', type=NotificationToReceiveStatusReportV08, min=1, max=1, mutex_group=None, array=False),
		))