# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ChequeCancellationOrStopRequestV02 import ChequeCancellationOrStopRequestV02

class CAMT_108_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.108.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ChqCxlOrStopReq"]
		@property
		def ChqCxlOrStopReq(self):
			return self._ChqCxlOrStopReq

		@ChqCxlOrStopReq.setter
		def ChqCxlOrStopReq(self, value):
			self._ChqCxlOrStopReq = value if type(value) != base_types.auto else self.make_default("ChqCxlOrStopReq")

		@ChqCxlOrStopReq.deleter
		def ChqCxlOrStopReq(self):
			del self._ChqCxlOrStopReq
			self._ChqCxlOrStopReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChqCxlOrStopReq', type=ChequeCancellationOrStopRequestV02, min=1, max=1, mutex_group=None, array=False),
		))