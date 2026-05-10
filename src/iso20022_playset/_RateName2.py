from . import base_types
from .RestrictedFINXMax8Text import RestrictedFINXMax8Text
from .RestrictedFINXMax24Text import RestrictedFINXMax24Text

class RateName2(base_types._BaseFieldType):

	__slots__ = ["_RateNm", "_Issr"]
	@property
	def RateNm(self):
		return self._RateNm

	@RateNm.setter
	def RateNm(self, value):
		self._RateNm = value if type(value) != base_types.auto else self.make_default("RateNm")

	@RateNm.deleter
	def RateNm(self):
		del self._RateNm
		self._RateNm = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateNm', type=RestrictedFINXMax24Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=RestrictedFINXMax8Text, min=0, max=1, mutex_group=None, array=False),
	))

