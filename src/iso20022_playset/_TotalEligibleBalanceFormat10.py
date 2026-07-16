# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Quantity49Choice
from . import SignedQuantityFormat10

class TotalEligibleBalanceFormat10(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_FullPrdUnits", "_PartWayPrdUnits"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', Quantity49Choice, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', Quantity49Choice, False)

	@property
	def FullPrdUnits(self):
		return self._FullPrdUnits

	@FullPrdUnits.setter
	def FullPrdUnits(self, value):
		self._FullPrdUnits = value if value is not None else base_types.UninitialisedField(self, 'FullPrdUnits', SignedQuantityFormat10, False)

	@FullPrdUnits.deleter
	def FullPrdUnits(self):
		del self._FullPrdUnits
		self._FullPrdUnits = base_types.UninitialisedField(self, 'FullPrdUnits', SignedQuantityFormat10, False)

	@property
	def PartWayPrdUnits(self):
		return self._PartWayPrdUnits

	@PartWayPrdUnits.setter
	def PartWayPrdUnits(self, value):
		self._PartWayPrdUnits = value if value is not None else base_types.UninitialisedField(self, 'PartWayPrdUnits', SignedQuantityFormat10, False)

	@PartWayPrdUnits.deleter
	def PartWayPrdUnits(self):
		del self._PartWayPrdUnits
		self._PartWayPrdUnits = base_types.UninitialisedField(self, 'PartWayPrdUnits', SignedQuantityFormat10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=Quantity49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullPrdUnits', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PartWayPrdUnits', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
	))