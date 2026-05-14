from . import base_types
from ._CorporateActionMovementPreliminaryAdviceV17 import CorporateActionMovementPreliminaryAdviceV17

class SEEV_035_001_17():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnMvmntPrlimryAdvc"]
		@property
		def CorpActnMvmntPrlimryAdvc(self):
			return self._CorpActnMvmntPrlimryAdvc

		@CorpActnMvmntPrlimryAdvc.setter
		def CorpActnMvmntPrlimryAdvc(self, value):
			self._CorpActnMvmntPrlimryAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnMvmntPrlimryAdvc")

		@CorpActnMvmntPrlimryAdvc.deleter
		def CorpActnMvmntPrlimryAdvc(self):
			del self._CorpActnMvmntPrlimryAdvc
			self._CorpActnMvmntPrlimryAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntPrlimryAdvc', type=CorporateActionMovementPreliminaryAdviceV17, min=1, max=1, mutex_group=None, array=False),
		))

