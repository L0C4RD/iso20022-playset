from . import base_types
from .UndertakingDemandV01 import UndertakingDemandV01

class TSRV_013_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgDmnd"]
		@property
		def UdrtkgDmnd(self):
			return self._UdrtkgDmnd

		@UdrtkgDmnd.setter
		def UdrtkgDmnd(self, value):
			self._UdrtkgDmnd = value if type(value) != base_types.auto else self.make_default("UdrtkgDmnd")

		@UdrtkgDmnd.deleter
		def UdrtkgDmnd(self):
			del self._UdrtkgDmnd
			self._UdrtkgDmnd = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgDmnd', type=UndertakingDemandV01, min=1, max=1, mutex_group=None, array=False),
		))

