from . import base_types
from .BuyInConfirmationV03 import BuyInConfirmationV03

class SECL_009_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BuyInConf"]
		@property
		def BuyInConf(self):
			return self._BuyInConf

		@BuyInConf.setter
		def BuyInConf(self, value):
			self._BuyInConf = value if type(value) != auto else self.make_default("BuyInConf")

		@BuyInConf.deleter
		def BuyInConf(self):
			del self._BuyInConf
			self._BuyInConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInConf', type=BuyInConfirmationV03, min=1, max=1, mutex_group=None, array=False),
		))

