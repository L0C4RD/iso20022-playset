# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GetLimitV08 import GetLimitV08

class CAMT_009_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.009.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_GetLmt"]
		@property
		def GetLmt(self):
			return self._GetLmt

		@GetLmt.setter
		def GetLmt(self, value):
			self._GetLmt = value if type(value) != base_types.auto else self.make_default("GetLmt")

		@GetLmt.deleter
		def GetLmt(self):
			del self._GetLmt
			self._GetLmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetLmt', type=GetLimitV08, min=1, max=1, mutex_group=None, array=False),
		))