# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Collateral54
from . import CollateralMovement13

class CollateralMovement6Choice(base_types._BaseFieldType):

	__slots__ = ["_CollMvmntDrctn", "_Rtr"]
	@property
	def CollMvmntDrctn(self):
		return self._CollMvmntDrctn

	@CollMvmntDrctn.setter
	def CollMvmntDrctn(self, value):
		self._CollMvmntDrctn = value if value is not None else base_types.UninitialisedField(self, 'CollMvmntDrctn', CollateralMovement13, False)

	@CollMvmntDrctn.deleter
	def CollMvmntDrctn(self):
		del self._CollMvmntDrctn
		self._CollMvmntDrctn = base_types.UninitialisedField(self, 'CollMvmntDrctn', CollateralMovement13, False)

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
		base_types.FieldEntry(name='CollMvmntDrctn', type=CollateralMovement13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rtr', type=Collateral54, min=0, max=1, mutex_group=1, array=False),
	))