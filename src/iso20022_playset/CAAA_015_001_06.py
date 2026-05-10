from . import base_types
import AcceptorRejectionV06

class CAAA_015_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrRjctn"]
		@property
		def AccptrRjctn(self):
			return self._AccptrRjctn

		@AccptrRjctn.setter
		def AccptrRjctn(self, value):
			self._AccptrRjctn = value if type(value) != auto else self.make_default("AccptrRjctn")

		@AccptrRjctn.deleter
		def AccptrRjctn(self):
			del self._AccptrRjctn
			self._AccptrRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrRjctn', type=AcceptorRejectionV06, min=1, max=1, mutex_group=None, array=False),
		))

