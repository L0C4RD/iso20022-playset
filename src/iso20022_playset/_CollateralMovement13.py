# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Collateral54
from . import Collateral55

class CollateralMovement13(base_types._BaseFieldType):

	__slots__ = ["_Dlvr", "_Rtr"]
	@property
	def Dlvr(self):
		return self._Dlvr

	@Dlvr.setter
	def Dlvr(self, value):
		self._Dlvr = value if value is not None else base_types.UninitialisedField(self, 'Dlvr', Collateral55, False)

	@Dlvr.deleter
	def Dlvr(self):
		del self._Dlvr
		self._Dlvr = base_types.UninitialisedField(self, 'Dlvr', Collateral55, False)

	@property
	def Rtr(self):
		return self._Rtr

	@Rtr.setter
	def Rtr(self, value):
		self._Rtr = value if value is not None else base_types.UninitialisedField(self, 'Rtr', Collateral54, False)

	@Rtr.deleter
	def Rtr(self):
		del self._Rtr
		self._Rtr = base_types.UninitialisedField(self, 'Rtr', Collateral54, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dlvr', type=Collateral55, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rtr', type=Collateral54, min=0, max=1, mutex_group=None, array=False),
	))