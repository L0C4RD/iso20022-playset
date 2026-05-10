import base_types
import SaleToPOIMessageRejectionV02

class CASP_013_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIMsgRjctn"]
		@property
		def SaleToPOIMsgRjctn(self):
			return self._SaleToPOIMsgRjctn

		@SaleToPOIMsgRjctn.setter
		def SaleToPOIMsgRjctn(self, value):
			self._SaleToPOIMsgRjctn = value if type(value) != auto else self.make_default("SaleToPOIMsgRjctn")

		@SaleToPOIMsgRjctn.deleter
		def SaleToPOIMsgRjctn(self):
			del self._SaleToPOIMsgRjctn
			self._SaleToPOIMsgRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIMsgRjctn', type=SaleToPOIMessageRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))

