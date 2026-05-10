from . import base_types
from .CorporateActionInstructionStatusAdviceV15 import CorporateActionInstructionStatusAdviceV15

class SEEV_034_001_15():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnInstrStsAdvc"]
		@property
		def CorpActnInstrStsAdvc(self):
			return self._CorpActnInstrStsAdvc

		@CorpActnInstrStsAdvc.setter
		def CorpActnInstrStsAdvc(self, value):
			self._CorpActnInstrStsAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnInstrStsAdvc")

		@CorpActnInstrStsAdvc.deleter
		def CorpActnInstrStsAdvc(self):
			del self._CorpActnInstrStsAdvc
			self._CorpActnInstrStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrStsAdvc', type=CorporateActionInstructionStatusAdviceV15, min=1, max=1, mutex_group=None, array=False),
		))

