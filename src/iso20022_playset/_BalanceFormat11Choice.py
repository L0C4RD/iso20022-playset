# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SignedQuantityFormat10 import SignedQuantityFormat10
from ._SignedQuantityFormat11 import SignedQuantityFormat11

class BalanceFormat11Choice(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_ElgblBal", "_NotElgblBal"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def ElgblBal(self):
		return self._ElgblBal

	@ElgblBal.setter
	def ElgblBal(self, value):
		self._ElgblBal = value if type(value) != base_types.auto else self.make_default("ElgblBal")

	@ElgblBal.deleter
	def ElgblBal(self):
		del self._ElgblBal
		self._ElgblBal = None

	@property
	def NotElgblBal(self):
		return self._NotElgblBal

	@NotElgblBal.setter
	def NotElgblBal(self, value):
		self._NotElgblBal = value if type(value) != base_types.auto else self.make_default("NotElgblBal")

	@NotElgblBal.deleter
	def NotElgblBal(self):
		del self._NotElgblBal
		self._NotElgblBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElgblBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotElgblBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
	))