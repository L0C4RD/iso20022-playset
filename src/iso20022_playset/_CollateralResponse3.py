# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashCollateralResponse3
from . import OtherCollateralResponse3
from . import SecuritiesCollateralResponse2

class CollateralResponse3(base_types._BaseFieldType):

	__slots__ = ["_CshCollRspn", "_OthrCollRspn", "_SctiesCollRspn"]
	@property
	def CshCollRspn(self):
		return self._CshCollRspn

	@CshCollRspn.setter
	def CshCollRspn(self, value):
		self._CshCollRspn = value if value is not None else base_types.UninitialisedField(self, 'CshCollRspn', CashCollateralResponse3, True)

	@CshCollRspn.deleter
	def CshCollRspn(self):
		del self._CshCollRspn
		self._CshCollRspn = base_types.UninitialisedField(self, 'CshCollRspn', CashCollateralResponse3, True)

	@property
	def OthrCollRspn(self):
		return self._OthrCollRspn

	@OthrCollRspn.setter
	def OthrCollRspn(self, value):
		self._OthrCollRspn = value if value is not None else base_types.UninitialisedField(self, 'OthrCollRspn', OtherCollateralResponse3, True)

	@OthrCollRspn.deleter
	def OthrCollRspn(self):
		del self._OthrCollRspn
		self._OthrCollRspn = base_types.UninitialisedField(self, 'OthrCollRspn', OtherCollateralResponse3, True)

	@property
	def SctiesCollRspn(self):
		return self._SctiesCollRspn

	@SctiesCollRspn.setter
	def SctiesCollRspn(self, value):
		self._SctiesCollRspn = value if value is not None else base_types.UninitialisedField(self, 'SctiesCollRspn', SecuritiesCollateralResponse2, True)

	@SctiesCollRspn.deleter
	def SctiesCollRspn(self):
		del self._SctiesCollRspn
		self._SctiesCollRspn = base_types.UninitialisedField(self, 'SctiesCollRspn', SecuritiesCollateralResponse2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCollRspn', type=CashCollateralResponse3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrCollRspn', type=OtherCollateralResponse3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesCollRspn', type=SecuritiesCollateralResponse2, min=0, max=None, mutex_group=None, array=True),
	))