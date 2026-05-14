from . import base_types
from ._EligibleCounterpartCSDStatusAdviceV01 import EligibleCounterpartCSDStatusAdviceV01

class REDA_044_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ElgblCntrptCSDStsAdvc"]
		@property
		def ElgblCntrptCSDStsAdvc(self):
			return self._ElgblCntrptCSDStsAdvc

		@ElgblCntrptCSDStsAdvc.setter
		def ElgblCntrptCSDStsAdvc(self, value):
			self._ElgblCntrptCSDStsAdvc = value if type(value) != base_types.auto else self.make_default("ElgblCntrptCSDStsAdvc")

		@ElgblCntrptCSDStsAdvc.deleter
		def ElgblCntrptCSDStsAdvc(self):
			del self._ElgblCntrptCSDStsAdvc
			self._ElgblCntrptCSDStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblCntrptCSDStsAdvc', type=EligibleCounterpartCSDStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

