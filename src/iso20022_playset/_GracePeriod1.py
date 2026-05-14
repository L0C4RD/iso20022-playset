# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GracePeriodUnitType1Code import GracePeriodUnitType1Code
from ._Max35Text import Max35Text
from ._Max3NumericText import Max3NumericText

class GracePeriod1(base_types._BaseFieldType):

	__slots__ = ["_OthrUnitTp", "_Tm", "_UnitTp"]
	@property
	def OthrUnitTp(self):
		return self._OthrUnitTp

	@OthrUnitTp.setter
	def OthrUnitTp(self, value):
		self._OthrUnitTp = value if type(value) != base_types.auto else self.make_default("OthrUnitTp")

	@OthrUnitTp.deleter
	def OthrUnitTp(self):
		del self._OthrUnitTp
		self._OthrUnitTp = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	@property
	def UnitTp(self):
		return self._UnitTp

	@UnitTp.setter
	def UnitTp(self, value):
		self._UnitTp = value if type(value) != base_types.auto else self.make_default("UnitTp")

	@UnitTp.deleter
	def UnitTp(self):
		del self._UnitTp
		self._UnitTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrUnitTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitTp', type=GracePeriodUnitType1Code, min=1, max=1, mutex_group=None, array=False),
	))