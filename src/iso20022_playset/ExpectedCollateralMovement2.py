import base_types
import CollateralMovement9

class ExpectedCollateralMovement2(base_types._BaseFieldType):

	__slots__ = ["_Rtr", "_Dlvry"]
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

	@property
	def Dlvry(self):
		return self._Dlvry

	@Dlvry.setter
	def Dlvry(self, value):
		self._Dlvry = value if type(value) != auto else self.make_default("Dlvry")

	@Dlvry.deleter
	def Dlvry(self):
		del self._Dlvry
		self._Dlvry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rtr', type=CollateralMovement9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dlvry', type=CollateralMovement9, min=0, max=None, mutex_group=None, array=True),
	))

