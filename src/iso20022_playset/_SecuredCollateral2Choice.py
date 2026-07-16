# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValuation6
from . import CollateralValuation7

class SecuredCollateral2Choice(base_types._BaseFieldType):

	__slots__ = ["_MltplColl", "_OthrColl", "_PoolColl", "_SnglColl"]
	@property
	def MltplColl(self):
		return self._MltplColl

	@MltplColl.setter
	def MltplColl(self, value):
		self._MltplColl = value if value is not None else base_types.UninitialisedField(self, 'MltplColl', CollateralValuation6, True)

	@MltplColl.deleter
	def MltplColl(self):
		del self._MltplColl
		self._MltplColl = base_types.UninitialisedField(self, 'MltplColl', CollateralValuation6, True)

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if value is not None else base_types.UninitialisedField(self, 'OthrColl', CollateralValuation7, True)

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = base_types.UninitialisedField(self, 'OthrColl', CollateralValuation7, True)

	@property
	def PoolColl(self):
		return self._PoolColl

	@PoolColl.setter
	def PoolColl(self, value):
		self._PoolColl = value if value is not None else base_types.UninitialisedField(self, 'PoolColl', CollateralValuation6, False)

	@PoolColl.deleter
	def PoolColl(self):
		del self._PoolColl
		self._PoolColl = base_types.UninitialisedField(self, 'PoolColl', CollateralValuation6, False)

	@property
	def SnglColl(self):
		return self._SnglColl

	@SnglColl.setter
	def SnglColl(self, value):
		self._SnglColl = value if value is not None else base_types.UninitialisedField(self, 'SnglColl', CollateralValuation6, False)

	@SnglColl.deleter
	def SnglColl(self):
		del self._SnglColl
		self._SnglColl = base_types.UninitialisedField(self, 'SnglColl', CollateralValuation6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MltplColl', type=CollateralValuation6, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OthrColl', type=CollateralValuation7, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='PoolColl', type=CollateralValuation6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SnglColl', type=CollateralValuation6, min=0, max=1, mutex_group=1, array=False),
	))