# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NotificationToReceiveCancellationAdviceV10 import NotificationToReceiveCancellationAdviceV10

class CAMT_058_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.058.001.10",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_NtfctnToRcvCxlAdvc"]
		@property
		def NtfctnToRcvCxlAdvc(self):
			return self._NtfctnToRcvCxlAdvc

		@NtfctnToRcvCxlAdvc.setter
		def NtfctnToRcvCxlAdvc(self, value):
			self._NtfctnToRcvCxlAdvc = value if type(value) != base_types.auto else self.make_default("NtfctnToRcvCxlAdvc")

		@NtfctnToRcvCxlAdvc.deleter
		def NtfctnToRcvCxlAdvc(self):
			del self._NtfctnToRcvCxlAdvc
			self._NtfctnToRcvCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcvCxlAdvc', type=NotificationToReceiveCancellationAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))