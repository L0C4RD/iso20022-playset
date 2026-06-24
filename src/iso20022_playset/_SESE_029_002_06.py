# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementAllegementRemovalAdvice002V06 import SecuritiesSettlementAllegementRemovalAdvice002V06

class SESE_029_002_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.029.002.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmAllgmtRmvlAdvc"]
		@property
		def SctiesSttlmAllgmtRmvlAdvc(self):
			return self._SctiesSttlmAllgmtRmvlAdvc

		@SctiesSttlmAllgmtRmvlAdvc.setter
		def SctiesSttlmAllgmtRmvlAdvc(self, value):
			self._SctiesSttlmAllgmtRmvlAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmAllgmtRmvlAdvc")

		@SctiesSttlmAllgmtRmvlAdvc.deleter
		def SctiesSttlmAllgmtRmvlAdvc(self):
			del self._SctiesSttlmAllgmtRmvlAdvc
			self._SctiesSttlmAllgmtRmvlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmAllgmtRmvlAdvc', type=SecuritiesSettlementAllegementRemovalAdvice002V06, min=1, max=1, mutex_group=None, array=False),
		))