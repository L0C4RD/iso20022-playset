# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SignedQuantityFormat10
from . import SignedQuantityFormat11

class BalanceFormat11Choice(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_ElgblBal", "_NotElgblBal"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat11, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat11, False)

	@property
	def ElgblBal(self):
		return self._ElgblBal

	@ElgblBal.setter
	def ElgblBal(self, value):
		self._ElgblBal = value if value is not None else base_types.UninitialisedField(self, 'ElgblBal', SignedQuantityFormat10, False)

	@ElgblBal.deleter
	def ElgblBal(self):
		del self._ElgblBal
		self._ElgblBal = base_types.UninitialisedField(self, 'ElgblBal', SignedQuantityFormat10, False)

	@property
	def NotElgblBal(self):
		return self._NotElgblBal

	@NotElgblBal.setter
	def NotElgblBal(self, value):
		self._NotElgblBal = value if value is not None else base_types.UninitialisedField(self, 'NotElgblBal', SignedQuantityFormat10, False)

	@NotElgblBal.deleter
	def NotElgblBal(self):
		del self._NotElgblBal
		self._NotElgblBal = base_types.UninitialisedField(self, 'NotElgblBal', SignedQuantityFormat10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElgblBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotElgblBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
	))