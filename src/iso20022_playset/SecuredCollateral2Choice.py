import base_types
import CollateralValuation6
import CollateralValuation7

class SecuredCollateral2Choice(base_types._BaseFieldType):

	__slots__ = ["_PoolColl", "_OthrColl", "_SnglColl", "_MltplColl"]
	@property
	def PoolColl(self):
		return self._PoolColl

	@PoolColl.setter
	def PoolColl(self, value):
		self._PoolColl = value if type(value) != auto else self.make_default("PoolColl")

	@PoolColl.deleter
	def PoolColl(self):
		del self._PoolColl
		self._PoolColl = None

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if type(value) != auto else self.make_default("OthrColl")

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = None

	@property
	def SnglColl(self):
		return self._SnglColl

	@SnglColl.setter
	def SnglColl(self, value):
		self._SnglColl = value if type(value) != auto else self.make_default("SnglColl")

	@SnglColl.deleter
	def SnglColl(self):
		del self._SnglColl
		self._SnglColl = None

	@property
	def MltplColl(self):
		return self._MltplColl

	@MltplColl.setter
	def MltplColl(self, value):
		self._MltplColl = value if type(value) != auto else self.make_default("MltplColl")

	@MltplColl.deleter
	def MltplColl(self):
		del self._MltplColl
		self._MltplColl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PoolColl', type=CollateralValuation6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrColl', type=CollateralValuation7, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SnglColl', type=CollateralValuation6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MltplColl', type=CollateralValuation6, min=1, max=None, mutex_group=1, array=True),
	))

