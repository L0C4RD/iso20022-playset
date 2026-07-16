# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max500Text
from . import NetworkType1Code

class NetworkParameters9(base_types._BaseFieldType):

	__slots__ = ["_AdrVal", "_NtwkTp"]
	@property
	def AdrVal(self):
		return self._AdrVal

	@AdrVal.setter
	def AdrVal(self, value):
		self._AdrVal = value if value is not None else base_types.UninitialisedField(self, 'AdrVal', Max500Text, False)

	@AdrVal.deleter
	def AdrVal(self):
		del self._AdrVal
		self._AdrVal = base_types.UninitialisedField(self, 'AdrVal', Max500Text, False)

	@property
	def NtwkTp(self):
		return self._NtwkTp

	@NtwkTp.setter
	def NtwkTp(self, value):
		self._NtwkTp = value if value is not None else base_types.UninitialisedField(self, 'NtwkTp', NetworkType1Code, False)

	@NtwkTp.deleter
	def NtwkTp(self):
		del self._NtwkTp
		self._NtwkTp = base_types.UninitialisedField(self, 'NtwkTp', NetworkType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrVal', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkTp', type=NetworkType1Code, min=1, max=1, mutex_group=None, array=False),
	))