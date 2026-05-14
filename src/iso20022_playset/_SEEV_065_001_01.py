from . import base_types
from ._BuyerProtectionInstructionAllegementRemovalAdviceV01 import BuyerProtectionInstructionAllegementRemovalAdviceV01

class SEEV_065_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BuyrPrtcnInstrAllgmtRmvlAdvc"]
		@property
		def BuyrPrtcnInstrAllgmtRmvlAdvc(self):
			return self._BuyrPrtcnInstrAllgmtRmvlAdvc

		@BuyrPrtcnInstrAllgmtRmvlAdvc.setter
		def BuyrPrtcnInstrAllgmtRmvlAdvc(self, value):
			self._BuyrPrtcnInstrAllgmtRmvlAdvc = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrAllgmtRmvlAdvc")

		@BuyrPrtcnInstrAllgmtRmvlAdvc.deleter
		def BuyrPrtcnInstrAllgmtRmvlAdvc(self):
			del self._BuyrPrtcnInstrAllgmtRmvlAdvc
			self._BuyrPrtcnInstrAllgmtRmvlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrAllgmtRmvlAdvc', type=BuyerProtectionInstructionAllegementRemovalAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

