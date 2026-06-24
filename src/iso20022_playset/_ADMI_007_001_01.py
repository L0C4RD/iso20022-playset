# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReceiptAcknowledgementV01 import ReceiptAcknowledgementV01

class ADMI_007_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:admi.007.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_RctAck"]
		@property
		def RctAck(self):
			return self._RctAck

		@RctAck.setter
		def RctAck(self, value):
			self._RctAck = value if type(value) != base_types.auto else self.make_default("RctAck")

		@RctAck.deleter
		def RctAck(self):
			del self._RctAck
			self._RctAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RctAck', type=ReceiptAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))