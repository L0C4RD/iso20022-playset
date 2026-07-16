# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import UnitOfMeasure4Code

class UnitOfMeasure3Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrUnitOfMeasr", "_UnitOfMeasrCd"]
	@property
	def OthrUnitOfMeasr(self):
		return self._OthrUnitOfMeasr

	@OthrUnitOfMeasr.setter
	def OthrUnitOfMeasr(self, value):
		self._OthrUnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'OthrUnitOfMeasr', Max35Text, False)

	@OthrUnitOfMeasr.deleter
	def OthrUnitOfMeasr(self):
		del self._OthrUnitOfMeasr
		self._OthrUnitOfMeasr = base_types.UninitialisedField(self, 'OthrUnitOfMeasr', Max35Text, False)

	@property
	def UnitOfMeasrCd(self):
		return self._UnitOfMeasrCd

	@UnitOfMeasrCd.setter
	def UnitOfMeasrCd(self, value):
		self._UnitOfMeasrCd = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasrCd', UnitOfMeasure4Code, False)

	@UnitOfMeasrCd.deleter
	def UnitOfMeasrCd(self):
		del self._UnitOfMeasrCd
		self._UnitOfMeasrCd = base_types.UninitialisedField(self, 'UnitOfMeasrCd', UnitOfMeasure4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrUnitOfMeasr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnitOfMeasrCd', type=UnitOfMeasure4Code, min=0, max=1, mutex_group=1, array=False),
	))