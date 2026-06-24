# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BatchTransferInitiationV03 import BatchTransferInitiationV03

class CAAD_003_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caad.003.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_BtchTrfInitn"]
		@property
		def BtchTrfInitn(self):
			return self._BtchTrfInitn

		@BtchTrfInitn.setter
		def BtchTrfInitn(self, value):
			self._BtchTrfInitn = value if type(value) != base_types.auto else self.make_default("BtchTrfInitn")

		@BtchTrfInitn.deleter
		def BtchTrfInitn(self):
			del self._BtchTrfInitn
			self._BtchTrfInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchTrfInitn', type=BatchTransferInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))