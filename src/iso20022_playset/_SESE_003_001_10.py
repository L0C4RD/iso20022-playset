from . import base_types
from ._TransferOutConfirmationV10 import TransferOutConfirmationV10

class SESE_003_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfOutConf"]
		@property
		def TrfOutConf(self):
			return self._TrfOutConf

		@TrfOutConf.setter
		def TrfOutConf(self, value):
			self._TrfOutConf = value if type(value) != base_types.auto else self.make_default("TrfOutConf")

		@TrfOutConf.deleter
		def TrfOutConf(self):
			del self._TrfOutConf
			self._TrfOutConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfOutConf', type=TransferOutConfirmationV10, min=1, max=1, mutex_group=None, array=False),
		))

