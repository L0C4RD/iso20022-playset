# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class MarginCollateral1(base_types._BaseFieldType):

	__slots__ = ["_HeldByPtyA", "_HeldByPtyB", "_InTrnstToPtyA", "_InTrnstToPtyB", "_PrrAgrdToPtyA", "_PrrAgrdToPtyB"]
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

	@property
	def InTrnstToPtyA(self):
		return self._InTrnstToPtyA

	@InTrnstToPtyA.setter
	def InTrnstToPtyA(self, value):
		self._InTrnstToPtyA = value if value is not None else base_types.UninitialisedField(self, 'InTrnstToPtyA', ActiveCurrencyAndAmount, False)

	@InTrnstToPtyA.deleter
	def InTrnstToPtyA(self):
		del self._InTrnstToPtyA
		self._InTrnstToPtyA = base_types.UninitialisedField(self, 'InTrnstToPtyA', ActiveCurrencyAndAmount, False)

	@property
	def InTrnstToPtyB(self):
		return self._InTrnstToPtyB

	@InTrnstToPtyB.setter
	def InTrnstToPtyB(self, value):
		self._InTrnstToPtyB = value if value is not None else base_types.UninitialisedField(self, 'InTrnstToPtyB', ActiveCurrencyAndAmount, False)

	@InTrnstToPtyB.deleter
	def InTrnstToPtyB(self):
		del self._InTrnstToPtyB
		self._InTrnstToPtyB = base_types.UninitialisedField(self, 'InTrnstToPtyB', ActiveCurrencyAndAmount, False)

	@property
	def PrrAgrdToPtyA(self):
		return self._PrrAgrdToPtyA

	@PrrAgrdToPtyA.setter
	def PrrAgrdToPtyA(self, value):
		self._PrrAgrdToPtyA = value if value is not None else base_types.UninitialisedField(self, 'PrrAgrdToPtyA', ActiveCurrencyAndAmount, False)

	@PrrAgrdToPtyA.deleter
	def PrrAgrdToPtyA(self):
		del self._PrrAgrdToPtyA
		self._PrrAgrdToPtyA = base_types.UninitialisedField(self, 'PrrAgrdToPtyA', ActiveCurrencyAndAmount, False)

	@property
	def PrrAgrdToPtyB(self):
		return self._PrrAgrdToPtyB

	@PrrAgrdToPtyB.setter
	def PrrAgrdToPtyB(self, value):
		self._PrrAgrdToPtyB = value if value is not None else base_types.UninitialisedField(self, 'PrrAgrdToPtyB', ActiveCurrencyAndAmount, False)

	@PrrAgrdToPtyB.deleter
	def PrrAgrdToPtyB(self):
		del self._PrrAgrdToPtyB
		self._PrrAgrdToPtyB = base_types.UninitialisedField(self, 'PrrAgrdToPtyB', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HeldByPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HeldByPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnstToPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnstToPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrrAgrdToPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrrAgrdToPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))