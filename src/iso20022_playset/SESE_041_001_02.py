import base_types
import BuyInRegulatoryAdviceV02

class SESE_041_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BuyInRgltryAdvc"]
		@property
		def BuyInRgltryAdvc(self):
			return self._BuyInRgltryAdvc

		@BuyInRgltryAdvc.setter
		def BuyInRgltryAdvc(self, value):
			self._BuyInRgltryAdvc = value if type(value) != auto else self.make_default("BuyInRgltryAdvc")

		@BuyInRgltryAdvc.deleter
		def BuyInRgltryAdvc(self):
			del self._BuyInRgltryAdvc
			self._BuyInRgltryAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRgltryAdvc', type=BuyInRegulatoryAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

