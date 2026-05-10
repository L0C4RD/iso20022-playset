from . import base_types
from .BuyInRegulatoryAdviceResponseV02 import BuyInRegulatoryAdviceResponseV02

class SESE_042_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BuyInRgltryAdvcRspn"]
		@property
		def BuyInRgltryAdvcRspn(self):
			return self._BuyInRgltryAdvcRspn

		@BuyInRgltryAdvcRspn.setter
		def BuyInRgltryAdvcRspn(self, value):
			self._BuyInRgltryAdvcRspn = value if type(value) != auto else self.make_default("BuyInRgltryAdvcRspn")

		@BuyInRgltryAdvcRspn.deleter
		def BuyInRgltryAdvcRspn(self):
			del self._BuyInRgltryAdvcRspn
			self._BuyInRgltryAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRgltryAdvcRspn', type=BuyInRegulatoryAdviceResponseV02, min=1, max=1, mutex_group=None, array=False),
		))

