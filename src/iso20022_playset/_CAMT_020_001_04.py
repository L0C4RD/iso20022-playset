# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GetGeneralBusinessInformationV04 import GetGeneralBusinessInformationV04

class CAMT_020_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.020.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_GetGnlBizInf"]
		@property
		def GetGnlBizInf(self):
			return self._GetGnlBizInf

		@GetGnlBizInf.setter
		def GetGnlBizInf(self, value):
			self._GetGnlBizInf = value if type(value) != base_types.auto else self.make_default("GetGnlBizInf")

		@GetGnlBizInf.deleter
		def GetGnlBizInf(self):
			del self._GetGnlBizInf
			self._GetGnlBizInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetGnlBizInf', type=GetGeneralBusinessInformationV04, min=1, max=1, mutex_group=None, array=False),
		))