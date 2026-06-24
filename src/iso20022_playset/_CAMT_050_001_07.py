# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LiquidityCreditTransferV07 import LiquidityCreditTransferV07

class CAMT_050_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.050.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_LqdtyCdtTrf"]
		@property
		def LqdtyCdtTrf(self):
			return self._LqdtyCdtTrf

		@LqdtyCdtTrf.setter
		def LqdtyCdtTrf(self, value):
			self._LqdtyCdtTrf = value if type(value) != base_types.auto else self.make_default("LqdtyCdtTrf")

		@LqdtyCdtTrf.deleter
		def LqdtyCdtTrf(self):
			del self._LqdtyCdtTrf
			self._LqdtyCdtTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LqdtyCdtTrf', type=LiquidityCreditTransferV07, min=1, max=1, mutex_group=None, array=False),
		))