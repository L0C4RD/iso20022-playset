from . import base_types
from ._SecuritiesSettlementAllegementRemovalAdviceV08 import SecuritiesSettlementAllegementRemovalAdviceV08

class SESE_029_001_08():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='SctiesSttlmAllgmtRmvlAdvc', type=SecuritiesSettlementAllegementRemovalAdviceV08, min=1, max=1, mutex_group=None, array=False),
		))

