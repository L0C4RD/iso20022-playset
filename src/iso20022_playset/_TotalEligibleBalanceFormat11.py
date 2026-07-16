# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Quantity80Choice
from . import SignedQuantityFormat13

class TotalEligibleBalanceFormat11(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_FullPrdUnits", "_PartWayPrdUnits"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', Quantity80Choice, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', Quantity80Choice, False)

	@property
	def FullPrdUnits(self):
		return self._FullPrdUnits

	@FullPrdUnits.setter
	def FullPrdUnits(self, value):
		self._FullPrdUnits = value if value is not None else base_types.UninitialisedField(self, 'FullPrdUnits', SignedQuantityFormat13, False)

	@FullPrdUnits.deleter
	def FullPrdUnits(self):
		del self._FullPrdUnits
		self._FullPrdUnits = base_types.UninitialisedField(self, 'FullPrdUnits', SignedQuantityFormat13, False)

	@property
	def PartWayPrdUnits(self):
		return self._PartWayPrdUnits

	@PartWayPrdUnits.setter
	def PartWayPrdUnits(self, value):
		self._PartWayPrdUnits = value if value is not None else base_types.UninitialisedField(self, 'PartWayPrdUnits', SignedQuantityFormat13, False)

	@PartWayPrdUnits.deleter
	def PartWayPrdUnits(self):
		del self._PartWayPrdUnits
		self._PartWayPrdUnits = base_types.UninitialisedField(self, 'PartWayPrdUnits', SignedQuantityFormat13, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=Quantity80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PartWayPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
	))