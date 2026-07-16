# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReceiptAcknowledgementV01

class ADMI_007_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.007.001.01"
		_docname = "admi.007.001.01"

		__slots__ = ["_RctAck"]
		@property
		def RctAck(self):
			return self._RctAck

		@RctAck.setter
		def RctAck(self, value):
			self._RctAck = value if value is not None else base_types.UninitialisedField(self, 'RctAck', ReceiptAcknowledgementV01, False)

		@RctAck.deleter
		def RctAck(self):
			del self._RctAck
			self._RctAck = base_types.UninitialisedField(self, 'RctAck', ReceiptAcknowledgementV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RctAck', type=ReceiptAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))