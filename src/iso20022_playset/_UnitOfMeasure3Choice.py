from . import base_types
from .Max35Text import Max35Text
from .UnitOfMeasure4Code import UnitOfMeasure4Code

class UnitOfMeasure3Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrUnitOfMeasr", "_UnitOfMeasrCd"]
	@property
	def OthrUnitOfMeasr(self):
		return self._OthrUnitOfMeasr

	@OthrUnitOfMeasr.setter
	def OthrUnitOfMeasr(self, value):
		self._OthrUnitOfMeasr = value if type(value) != base_types.auto else self.make_default("OthrUnitOfMeasr")

	@OthrUnitOfMeasr.deleter
	def OthrUnitOfMeasr(self):
		del self._OthrUnitOfMeasr
		self._OthrUnitOfMeasr = None

	@property
	def UnitOfMeasrCd(self):
		return self._UnitOfMeasrCd

	@UnitOfMeasrCd.setter
	def UnitOfMeasrCd(self, value):
		self._UnitOfMeasrCd = value if type(value) != base_types.auto else self.make_default("UnitOfMeasrCd")

	@UnitOfMeasrCd.deleter
	def UnitOfMeasrCd(self):
		del self._UnitOfMeasrCd
		self._UnitOfMeasrCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrUnitOfMeasr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnitOfMeasrCd', type=UnitOfMeasure4Code, min=0, max=1, mutex_group=1, array=False),
	))

