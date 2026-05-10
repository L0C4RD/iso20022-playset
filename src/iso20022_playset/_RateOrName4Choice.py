from . import base_types
from ._RateTypeAndLookback2 import RateTypeAndLookback2
from ._PercentageRate import PercentageRate

class RateOrName4Choice(base_types._BaseFieldType):

	__slots__ = ["_RateIndxDtls", "_Rate"]
	@property
	def RateIndxDtls(self):
		return self._RateIndxDtls

	@RateIndxDtls.setter
	def RateIndxDtls(self, value):
		self._RateIndxDtls = value if type(value) != base_types.auto else self.make_default("RateIndxDtls")

	@RateIndxDtls.deleter
	def RateIndxDtls(self):
		del self._RateIndxDtls
		self._RateIndxDtls = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateIndxDtls', type=RateTypeAndLookback2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

