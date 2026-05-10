import base_types
import AmendmentAcceptanceV02

class TSMT_005_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AmdmntAccptnc"]
		@property
		def AmdmntAccptnc(self):
			return self._AmdmntAccptnc

		@AmdmntAccptnc.setter
		def AmdmntAccptnc(self, value):
			self._AmdmntAccptnc = value if type(value) != auto else self.make_default("AmdmntAccptnc")

		@AmdmntAccptnc.deleter
		def AmdmntAccptnc(self):
			del self._AmdmntAccptnc
			self._AmdmntAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntAccptnc', type=AmendmentAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))

