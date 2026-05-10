import base_types
import Max50Text
import OrderType3Code

class OrderClassification2(base_types._BaseFieldType):

	__slots__ = ["_OrdrTpClssfctn", "_OrdrTp"]
	@property
	def OrdrTpClssfctn(self):
		return self._OrdrTpClssfctn

	@OrdrTpClssfctn.setter
	def OrdrTpClssfctn(self, value):
		self._OrdrTpClssfctn = value if type(value) != auto else self.make_default("OrdrTpClssfctn")

	@OrdrTpClssfctn.deleter
	def OrdrTpClssfctn(self):
		del self._OrdrTpClssfctn
		self._OrdrTpClssfctn = None

	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if type(value) != auto else self.make_default("OrdrTp")

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrTpClssfctn', type=OrderType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))

