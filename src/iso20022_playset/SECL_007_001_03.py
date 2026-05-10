from . import base_types
import BuyInNotificationV03

class SECL_007_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BuyInNtfctn"]
		@property
		def BuyInNtfctn(self):
			return self._BuyInNtfctn

		@BuyInNtfctn.setter
		def BuyInNtfctn(self, value):
			self._BuyInNtfctn = value if type(value) != auto else self.make_default("BuyInNtfctn")

		@BuyInNtfctn.deleter
		def BuyInNtfctn(self):
			del self._BuyInNtfctn
			self._BuyInNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInNtfctn', type=BuyInNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

