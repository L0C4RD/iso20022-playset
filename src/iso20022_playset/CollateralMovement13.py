import base_types
import Collateral55
import Collateral54

class CollateralMovement13(base_types._BaseFieldType):

	__slots__ = ["_Dlvr", "_Rtr"]
	@property
	def Dlvr(self):
		return self._Dlvr

	@Dlvr.setter
	def Dlvr(self, value):
		self._Dlvr = value if type(value) != auto else self.make_default("Dlvr")

	@Dlvr.deleter
	def Dlvr(self):
		del self._Dlvr
		self._Dlvr = None

	@property
	def Rtr(self):
		return self._Rtr

	@Rtr.setter
	def Rtr(self, value):
		self._Rtr = value if type(value) != auto else self.make_default("Rtr")

	@Rtr.deleter
	def Rtr(self):
		del self._Rtr
		self._Rtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dlvr', type=Collateral55, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rtr', type=Collateral54, min=0, max=1, mutex_group=None, array=False),
	))

