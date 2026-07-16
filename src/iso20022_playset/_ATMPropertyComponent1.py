# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMPropertyType1Code
from . import Max2000Text
from . import Max70Text

class ATMPropertyComponent1(base_types._BaseFieldType):

	__slots__ = ["_PrprtyNm", "_PrprtyTp", "_PrprtyVal"]
	@property
	def PrprtyNm(self):
		return self._PrprtyNm

	@PrprtyNm.setter
	def PrprtyNm(self, value):
		self._PrprtyNm = value if value is not None else base_types.UninitialisedField(self, 'PrprtyNm', Max70Text, False)

	@PrprtyNm.deleter
	def PrprtyNm(self):
		del self._PrprtyNm
		self._PrprtyNm = base_types.UninitialisedField(self, 'PrprtyNm', Max70Text, False)

	@property
	def PrprtyTp(self):
		return self._PrprtyTp

	@PrprtyTp.setter
	def PrprtyTp(self, value):
		self._PrprtyTp = value if value is not None else base_types.UninitialisedField(self, 'PrprtyTp', ATMPropertyType1Code, False)

	@PrprtyTp.deleter
	def PrprtyTp(self):
		del self._PrprtyTp
		self._PrprtyTp = base_types.UninitialisedField(self, 'PrprtyTp', ATMPropertyType1Code, False)

	@property
	def PrprtyVal(self):
		return self._PrprtyVal

	@PrprtyVal.setter
	def PrprtyVal(self, value):
		self._PrprtyVal = value if value is not None else base_types.UninitialisedField(self, 'PrprtyVal', Max2000Text, False)

	@PrprtyVal.deleter
	def PrprtyVal(self):
		del self._PrprtyVal
		self._PrprtyVal = base_types.UninitialisedField(self, 'PrprtyVal', Max2000Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrprtyNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyTp', type=ATMPropertyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyVal', type=Max2000Text, min=1, max=1, mutex_group=None, array=False),
	))