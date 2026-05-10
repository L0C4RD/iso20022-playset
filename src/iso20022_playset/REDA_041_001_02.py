from . import base_types
from .PartyActivityAdviceV02 import PartyActivityAdviceV02

class REDA_041_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyActvtyAdvc"]
		@property
		def PtyActvtyAdvc(self):
			return self._PtyActvtyAdvc

		@PtyActvtyAdvc.setter
		def PtyActvtyAdvc(self, value):
			self._PtyActvtyAdvc = value if type(value) != auto else self.make_default("PtyActvtyAdvc")

		@PtyActvtyAdvc.deleter
		def PtyActvtyAdvc(self):
			del self._PtyActvtyAdvc
			self._PtyActvtyAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyActvtyAdvc', type=PartyActivityAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

