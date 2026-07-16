# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateType8Code
from . import Period11

class Period6Choice(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_PrdCd"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', Period11, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', Period11, False)

	@property
	def PrdCd(self):
		return self._PrdCd

	@PrdCd.setter
	def PrdCd(self, value):
		self._PrdCd = value if value is not None else base_types.UninitialisedField(self, 'PrdCd', DateType8Code, False)

	@PrdCd.deleter
	def PrdCd(self):
		del self._PrdCd
		self._PrdCd = base_types.UninitialisedField(self, 'PrdCd', DateType8Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=Period11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrdCd', type=DateType8Code, min=0, max=1, mutex_group=1, array=False),
	))