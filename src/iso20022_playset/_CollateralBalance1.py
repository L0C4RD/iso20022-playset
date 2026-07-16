# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class CollateralBalance1(base_types._BaseFieldType):

	__slots__ = ["_HeldByPtyA", "_HeldByPtyB"]
	@property
	def HeldByPtyA(self):
		return self._HeldByPtyA

	@HeldByPtyA.setter
	def HeldByPtyA(self, value):
		self._HeldByPtyA = value if value is not None else base_types.UninitialisedField(self, 'HeldByPtyA', ActiveCurrencyAndAmount, False)

	@HeldByPtyA.deleter
	def HeldByPtyA(self):
		del self._HeldByPtyA
		self._HeldByPtyA = base_types.UninitialisedField(self, 'HeldByPtyA', ActiveCurrencyAndAmount, False)

	@property
	def HeldByPtyB(self):
		return self._HeldByPtyB

	@HeldByPtyB.setter
	def HeldByPtyB(self, value):
		self._HeldByPtyB = value if value is not None else base_types.UninitialisedField(self, 'HeldByPtyB', ActiveCurrencyAndAmount, False)

	@HeldByPtyB.deleter
	def HeldByPtyB(self):
		del self._HeldByPtyB
		self._HeldByPtyB = base_types.UninitialisedField(self, 'HeldByPtyB', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HeldByPtyA', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HeldByPtyB', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))