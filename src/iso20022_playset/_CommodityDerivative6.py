# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max25Text

class CommodityDerivative6(base_types._BaseFieldType):

	__slots__ = ["_SttlmLctn"]
	@property
	def SttlmLctn(self):
		return self._SttlmLctn

	@SttlmLctn.setter
	def SttlmLctn(self, value):
		self._SttlmLctn = value if value is not None else base_types.UninitialisedField(self, 'SttlmLctn', Max25Text, False)

	@SttlmLctn.deleter
	def SttlmLctn(self):
		del self._SttlmLctn
		self._SttlmLctn = base_types.UninitialisedField(self, 'SttlmLctn', Max25Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmLctn', type=Max25Text, min=1, max=1, mutex_group=None, array=False),
	))