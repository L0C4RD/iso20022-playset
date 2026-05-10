from . import base_types
from .TransferOutConfirmationV09 import TransferOutConfirmationV09

class SESE_003_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfOutConf"]
		@property
		def TrfOutConf(self):
			return self._TrfOutConf

		@TrfOutConf.setter
		def TrfOutConf(self, value):
			self._TrfOutConf = value if type(value) != auto else self.make_default("TrfOutConf")

		@TrfOutConf.deleter
		def TrfOutConf(self):
			del self._TrfOutConf
			self._TrfOutConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfOutConf', type=TransferOutConfirmationV09, min=1, max=1, mutex_group=None, array=False),
		))

