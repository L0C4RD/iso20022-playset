from . import base_types
from ._OrderData4 import OrderData4
from ._AuctionData2 import AuctionData2
from ._OrderIdentification2 import OrderIdentification2

class OrderData3(base_types._BaseFieldType):

	__slots__ = ["_AuctnData", "_OrdrData", "_OrdrIdData"]
	@property
	def AuctnData(self):
		return self._AuctnData

	@AuctnData.setter
	def AuctnData(self, value):
		self._AuctnData = value if type(value) != base_types.auto else self.make_default("AuctnData")

	@AuctnData.deleter
	def AuctnData(self):
		del self._AuctnData
		self._AuctnData = None

	@property
	def OrdrData(self):
		return self._OrdrData

	@OrdrData.setter
	def OrdrData(self, value):
		self._OrdrData = value if type(value) != base_types.auto else self.make_default("OrdrData")

	@OrdrData.deleter
	def OrdrData(self):
		del self._OrdrData
		self._OrdrData = None

	@property
	def OrdrIdData(self):
		return self._OrdrIdData

	@OrdrIdData.setter
	def OrdrIdData(self, value):
		self._OrdrIdData = value if type(value) != base_types.auto else self.make_default("OrdrIdData")

	@OrdrIdData.deleter
	def OrdrIdData(self):
		del self._OrdrIdData
		self._OrdrIdData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuctnData', type=AuctionData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrData', type=OrderData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrIdData', type=OrderIdentification2, min=1, max=1, mutex_group=None, array=False),
	))

