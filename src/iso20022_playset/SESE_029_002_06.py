from . import base_types
import SecuritiesSettlementAllegementRemovalAdvice002V06

class SESE_029_002_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmAllgmtRmvlAdvc"]
		@property
		def SctiesSttlmAllgmtRmvlAdvc(self):
			return self._SctiesSttlmAllgmtRmvlAdvc

		@SctiesSttlmAllgmtRmvlAdvc.setter
		def SctiesSttlmAllgmtRmvlAdvc(self, value):
			self._SctiesSttlmAllgmtRmvlAdvc = value if type(value) != auto else self.make_default("SctiesSttlmAllgmtRmvlAdvc")

		@SctiesSttlmAllgmtRmvlAdvc.deleter
		def SctiesSttlmAllgmtRmvlAdvc(self):
			del self._SctiesSttlmAllgmtRmvlAdvc
			self._SctiesSttlmAllgmtRmvlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmAllgmtRmvlAdvc', type=SecuritiesSettlementAllegementRemovalAdvice002V06, min=1, max=1, mutex_group=None, array=False),
		))

