import base_types
import UndertakingApplicationV01

class TSIN_005_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgAppl"]
		@property
		def UdrtkgAppl(self):
			return self._UdrtkgAppl

		@UdrtkgAppl.setter
		def UdrtkgAppl(self, value):
			self._UdrtkgAppl = value if type(value) != auto else self.make_default("UdrtkgAppl")

		@UdrtkgAppl.deleter
		def UdrtkgAppl(self):
			del self._UdrtkgAppl
			self._UdrtkgAppl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAppl', type=UndertakingApplicationV01, min=1, max=1, mutex_group=None, array=False),
		))

