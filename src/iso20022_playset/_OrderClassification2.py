# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max50Text
from . import OrderType3Code

class OrderClassification2(base_types._BaseFieldType):

	__slots__ = ["_OrdrTp", "_OrdrTpClssfctn"]
	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if value is not None else base_types.UninitialisedField(self, 'OrdrTp', Max50Text, False)

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = base_types.UninitialisedField(self, 'OrdrTp', Max50Text, False)

	@property
	def OrdrTpClssfctn(self):
		return self._OrdrTpClssfctn

	@OrdrTpClssfctn.setter
	def OrdrTpClssfctn(self, value):
		self._OrdrTpClssfctn = value if value is not None else base_types.UninitialisedField(self, 'OrdrTpClssfctn', OrderType3Code, False)

	@OrdrTpClssfctn.deleter
	def OrdrTpClssfctn(self):
		del self._OrdrTpClssfctn
		self._OrdrTpClssfctn = base_types.UninitialisedField(self, 'OrdrTpClssfctn', OrderType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrTp', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTpClssfctn', type=OrderType3Code, min=0, max=1, mutex_group=None, array=False),
	))