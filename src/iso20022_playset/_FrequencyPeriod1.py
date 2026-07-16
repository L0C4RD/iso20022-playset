# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Frequency6Code

class FrequencyPeriod1(base_types._BaseFieldType):

	__slots__ = ["_CntPerPrd", "_Tp"]
	@property
	def CntPerPrd(self):
		return self._CntPerPrd

	@CntPerPrd.setter
	def CntPerPrd(self, value):
		self._CntPerPrd = value if value is not None else base_types.UninitialisedField(self, 'CntPerPrd', DecimalNumber, False)

	@CntPerPrd.deleter
	def CntPerPrd(self):
		del self._CntPerPrd
		self._CntPerPrd = base_types.UninitialisedField(self, 'CntPerPrd', DecimalNumber, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Frequency6Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Frequency6Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntPerPrd', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Frequency6Code, min=1, max=1, mutex_group=None, array=False),
	))