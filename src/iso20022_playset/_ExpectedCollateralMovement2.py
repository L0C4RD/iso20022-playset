# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralMovement9

class ExpectedCollateralMovement2(base_types._BaseFieldType):

	__slots__ = ["_Dlvry", "_Rtr"]
	@property
	def Dlvry(self):
		return self._Dlvry

	@Dlvry.setter
	def Dlvry(self, value):
		self._Dlvry = value if value is not None else base_types.UninitialisedField(self, 'Dlvry', CollateralMovement9, True)

	@Dlvry.deleter
	def Dlvry(self):
		del self._Dlvry
		self._Dlvry = base_types.UninitialisedField(self, 'Dlvry', CollateralMovement9, True)

	@property
	def Rtr(self):
		return self._Rtr

	@Rtr.setter
	def Rtr(self, value):
		self._Rtr = value if value is not None else base_types.UninitialisedField(self, 'Rtr', CollateralMovement9, True)

	@Rtr.deleter
	def Rtr(self):
		del self._Rtr
		self._Rtr = base_types.UninitialisedField(self, 'Rtr', CollateralMovement9, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dlvry', type=CollateralMovement9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rtr', type=CollateralMovement9, min=0, max=None, mutex_group=None, array=True),
	))