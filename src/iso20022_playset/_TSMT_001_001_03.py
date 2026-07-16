# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgementV03

class TSMT_001_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.001.001.03"
		_docname = "tsmt.001.001.03"

		__slots__ = ["_Ack"]
		@property
		def Ack(self):
			return self._Ack

		@Ack.setter
		def Ack(self, value):
			self._Ack = value if value is not None else base_types.UninitialisedField(self, 'Ack', AcknowledgementV03, False)

		@Ack.deleter
		def Ack(self):
			del self._Ack
			self._Ack = base_types.UninitialisedField(self, 'Ack', AcknowledgementV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='Ack', type=AcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))