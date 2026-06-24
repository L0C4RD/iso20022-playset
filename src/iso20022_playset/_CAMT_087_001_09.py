# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RequestToModifyPaymentV09 import RequestToModifyPaymentV09

class CAMT_087_001_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.087.001.09"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ReqToModfyPmt"]
		@property
		def ReqToModfyPmt(self):
			return self._ReqToModfyPmt

		@ReqToModfyPmt.setter
		def ReqToModfyPmt(self, value):
			self._ReqToModfyPmt = value if type(value) != base_types.auto else self.make_default("ReqToModfyPmt")

		@ReqToModfyPmt.deleter
		def ReqToModfyPmt(self):
			del self._ReqToModfyPmt
			self._ReqToModfyPmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToModfyPmt', type=RequestToModifyPaymentV09, min=1, max=1, mutex_group=None, array=False),
		))