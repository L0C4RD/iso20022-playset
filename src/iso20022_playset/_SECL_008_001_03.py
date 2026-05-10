from . import base_types
from ._BuyInResponseV03 import BuyInResponseV03

class SECL_008_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BuyInRspn"]
		@property
		def BuyInRspn(self):
			return self._BuyInRspn

		@BuyInRspn.setter
		def BuyInRspn(self, value):
			self._BuyInRspn = value if type(value) != base_types.auto else self.make_default("BuyInRspn")

		@BuyInRspn.deleter
		def BuyInRspn(self):
			del self._BuyInRspn
			self._BuyInRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRspn', type=BuyInResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

