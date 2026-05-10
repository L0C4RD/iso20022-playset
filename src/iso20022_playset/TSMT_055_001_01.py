from . import base_types
from .PartyEventAdviceV01 import PartyEventAdviceV01

class TSMT_055_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyEvtAdvc"]
		@property
		def PtyEvtAdvc(self):
			return self._PtyEvtAdvc

		@PtyEvtAdvc.setter
		def PtyEvtAdvc(self, value):
			self._PtyEvtAdvc = value if type(value) != auto else self.make_default("PtyEvtAdvc")

		@PtyEvtAdvc.deleter
		def PtyEvtAdvc(self):
			del self._PtyEvtAdvc
			self._PtyEvtAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyEvtAdvc', type=PartyEventAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

