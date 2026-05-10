from . import base_types
from ._SecuritiesCollateralResponse2 import SecuritiesCollateralResponse2
from ._CashCollateralResponse3 import CashCollateralResponse3
from ._OtherCollateralResponse3 import OtherCollateralResponse3

class CollateralResponse3(base_types._BaseFieldType):

	__slots__ = ["_SctiesCollRspn", "_CshCollRspn", "_OthrCollRspn"]
	@property
	def CshCollRspn(self):
		return self._CshCollRspn

	@CshCollRspn.setter
	def CshCollRspn(self, value):
		self._CshCollRspn = value if type(value) != base_types.auto else self.make_default("CshCollRspn")

	@CshCollRspn.deleter
	def CshCollRspn(self):
		del self._CshCollRspn
		self._CshCollRspn = None

	@property
	def OthrCollRspn(self):
		return self._OthrCollRspn

	@OthrCollRspn.setter
	def OthrCollRspn(self, value):
		self._OthrCollRspn = value if type(value) != base_types.auto else self.make_default("OthrCollRspn")

	@OthrCollRspn.deleter
	def OthrCollRspn(self):
		del self._OthrCollRspn
		self._OthrCollRspn = None

	@property
	def SctiesCollRspn(self):
		return self._SctiesCollRspn

	@SctiesCollRspn.setter
	def SctiesCollRspn(self, value):
		self._SctiesCollRspn = value if type(value) != base_types.auto else self.make_default("SctiesCollRspn")

	@SctiesCollRspn.deleter
	def SctiesCollRspn(self):
		del self._SctiesCollRspn
		self._SctiesCollRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCollRspn', type=CashCollateralResponse3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrCollRspn', type=OtherCollateralResponse3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesCollRspn', type=SecuritiesCollateralResponse2, min=0, max=None, mutex_group=None, array=True),
	))

