# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTradeConfirmationResponseV03 import SecuritiesTradeConfirmationResponseV03

class SETR_030_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.030.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesTradConfRspn"]
		@property
		def SctiesTradConfRspn(self):
			return self._SctiesTradConfRspn

		@SctiesTradConfRspn.setter
		def SctiesTradConfRspn(self, value):
			self._SctiesTradConfRspn = value if type(value) != base_types.auto else self.make_default("SctiesTradConfRspn")

		@SctiesTradConfRspn.deleter
		def SctiesTradConfRspn(self):
			del self._SctiesTradConfRspn
			self._SctiesTradConfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTradConfRspn', type=SecuritiesTradeConfirmationResponseV03, min=1, max=1, mutex_group=None, array=False),
		))