from . import base_types
from .PartyStatusAdviceV01 import PartyStatusAdviceV01

class REDA_016_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyStsAdvc"]
		@property
		def PtyStsAdvc(self):
			return self._PtyStsAdvc

		@PtyStsAdvc.setter
		def PtyStsAdvc(self, value):
			self._PtyStsAdvc = value if type(value) != auto else self.make_default("PtyStsAdvc")

		@PtyStsAdvc.deleter
		def PtyStsAdvc(self):
			del self._PtyStsAdvc
			self._PtyStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyStsAdvc', type=PartyStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

