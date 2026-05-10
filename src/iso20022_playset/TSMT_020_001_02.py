from . import base_types
import MisMatchAcceptanceV02

class TSMT_020_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MisMtchAccptnc"]
		@property
		def MisMtchAccptnc(self):
			return self._MisMtchAccptnc

		@MisMtchAccptnc.setter
		def MisMtchAccptnc(self, value):
			self._MisMtchAccptnc = value if type(value) != auto else self.make_default("MisMtchAccptnc")

		@MisMtchAccptnc.deleter
		def MisMtchAccptnc(self):
			del self._MisMtchAccptnc
			self._MisMtchAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchAccptnc', type=MisMatchAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))

