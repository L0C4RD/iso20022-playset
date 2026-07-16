# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SignedQuantityFormat12
from . import SignedQuantityFormat13

class BalanceFormat16Choice(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_ElgblBal", "_FullPrdUnits", "_NotElgblBal", "_PartWayPrdUnits"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat12, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat12, False)

	@property
	def ElgblBal(self):
		return self._ElgblBal

	@ElgblBal.setter
	def ElgblBal(self, value):
		self._ElgblBal = value if value is not None else base_types.UninitialisedField(self, 'ElgblBal', SignedQuantityFormat13, False)

	@ElgblBal.deleter
	def ElgblBal(self):
		del self._ElgblBal
		self._ElgblBal = base_types.UninitialisedField(self, 'ElgblBal', SignedQuantityFormat13, False)

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
	def NotElgblBal(self):
		return self._NotElgblBal

	@NotElgblBal.setter
	def NotElgblBal(self, value):
		self._NotElgblBal = value if value is not None else base_types.UninitialisedField(self, 'NotElgblBal', SignedQuantityFormat13, False)

	@NotElgblBal.deleter
	def NotElgblBal(self):
		del self._NotElgblBal
		self._NotElgblBal = base_types.UninitialisedField(self, 'NotElgblBal', SignedQuantityFormat13, False)

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
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElgblBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FullPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotElgblBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PartWayPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
	))