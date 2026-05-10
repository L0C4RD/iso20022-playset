from . import base_types
import IdentificationModificationAdviceV04

class ACMT_022_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IdModAdvc"]
		@property
		def IdModAdvc(self):
			return self._IdModAdvc

		@IdModAdvc.setter
		def IdModAdvc(self, value):
			self._IdModAdvc = value if type(value) != auto else self.make_default("IdModAdvc")

		@IdModAdvc.deleter
		def IdModAdvc(self):
			del self._IdModAdvc
			self._IdModAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IdModAdvc', type=IdentificationModificationAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))

