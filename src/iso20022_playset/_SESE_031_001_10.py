# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementConditionModificationStatusAdviceV10 import SecuritiesSettlementConditionModificationStatusAdviceV10

class SESE_031_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.031.001.10"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmCondModStsAdvc"]
		@property
		def SctiesSttlmCondModStsAdvc(self):
			return self._SctiesSttlmCondModStsAdvc

		@SctiesSttlmCondModStsAdvc.setter
		def SctiesSttlmCondModStsAdvc(self, value):
			self._SctiesSttlmCondModStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmCondModStsAdvc")

		@SctiesSttlmCondModStsAdvc.deleter
		def SctiesSttlmCondModStsAdvc(self):
			del self._SctiesSttlmCondModStsAdvc
			self._SctiesSttlmCondModStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondModStsAdvc', type=SecuritiesSettlementConditionModificationStatusAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))