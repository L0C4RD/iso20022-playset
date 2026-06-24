# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesAccountPositionQueryV01 import SecuritiesAccountPositionQueryV01

class SEMT_025_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.025.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesAcctPosQry"]
		@property
		def SctiesAcctPosQry(self):
			return self._SctiesAcctPosQry

		@SctiesAcctPosQry.setter
		def SctiesAcctPosQry(self, value):
			self._SctiesAcctPosQry = value if type(value) != base_types.auto else self.make_default("SctiesAcctPosQry")

		@SctiesAcctPosQry.deleter
		def SctiesAcctPosQry(self):
			del self._SctiesAcctPosQry
			self._SctiesAcctPosQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctPosQry', type=SecuritiesAccountPositionQueryV01, min=1, max=1, mutex_group=None, array=False),
		))