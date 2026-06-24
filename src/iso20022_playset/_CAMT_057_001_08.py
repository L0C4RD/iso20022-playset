# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NotificationToReceiveV08 import NotificationToReceiveV08

class CAMT_057_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.057.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_NtfctnToRcv"]
		@property
		def NtfctnToRcv(self):
			return self._NtfctnToRcv

		@NtfctnToRcv.setter
		def NtfctnToRcv(self, value):
			self._NtfctnToRcv = value if type(value) != base_types.auto else self.make_default("NtfctnToRcv")

		@NtfctnToRcv.deleter
		def NtfctnToRcv(self):
			del self._NtfctnToRcv
			self._NtfctnToRcv = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcv', type=NotificationToReceiveV08, min=1, max=1, mutex_group=None, array=False),
		))