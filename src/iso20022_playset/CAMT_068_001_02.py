from . import base_types
import IntraBalanceMovementConfirmationV02

class CAMT_068_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntConf"]
		@property
		def IntraBalMvmntConf(self):
			return self._IntraBalMvmntConf

		@IntraBalMvmntConf.setter
		def IntraBalMvmntConf(self, value):
			self._IntraBalMvmntConf = value if type(value) != auto else self.make_default("IntraBalMvmntConf")

		@IntraBalMvmntConf.deleter
		def IntraBalMvmntConf(self):
			del self._IntraBalMvmntConf
			self._IntraBalMvmntConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntConf', type=IntraBalanceMovementConfirmationV02, min=1, max=1, mutex_group=None, array=False),
		))

