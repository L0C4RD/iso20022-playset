import base_types
import Max25Text

class CommodityDerivative6(base_types._BaseFieldType):

	__slots__ = ["_SttlmLctn"]
	@property
	def SttlmLctn(self):
		return self._SttlmLctn

	@SttlmLctn.setter
	def SttlmLctn(self, value):
		self._SttlmLctn = value if type(value) != auto else self.make_default("SttlmLctn")

	@SttlmLctn.deleter
	def SttlmLctn(self):
		del self._SttlmLctn
		self._SttlmLctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmLctn', type=Max25Text, min=1, max=1, mutex_group=None, array=False),
	))

