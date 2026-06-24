# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcknowledgementV03 import AcknowledgementV03

class TSMT_001_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.001.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_Ack"]
		@property
		def Ack(self):
			return self._Ack

		@Ack.setter
		def Ack(self, value):
			self._Ack = value if type(value) != base_types.auto else self.make_default("Ack")

		@Ack.deleter
		def Ack(self):
			del self._Ack
			self._Ack = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Ack', type=AcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))