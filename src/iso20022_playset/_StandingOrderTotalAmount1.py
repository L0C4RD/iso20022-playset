# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TotalAmountAndCurrency1

class StandingOrderTotalAmount1(base_types._BaseFieldType):

	__slots__ = ["_PdgPrdfndOrdr", "_PdgStgOrdr", "_SetPrdfndOrdr", "_SetStgOrdr"]
	@property
	def PdgPrdfndOrdr(self):
		return self._PdgPrdfndOrdr

	@PdgPrdfndOrdr.setter
	def PdgPrdfndOrdr(self, value):
		self._PdgPrdfndOrdr = value if value is not None else base_types.UninitialisedField(self, 'PdgPrdfndOrdr', TotalAmountAndCurrency1, False)

	@PdgPrdfndOrdr.deleter
	def PdgPrdfndOrdr(self):
		del self._PdgPrdfndOrdr
		self._PdgPrdfndOrdr = base_types.UninitialisedField(self, 'PdgPrdfndOrdr', TotalAmountAndCurrency1, False)

	@property
	def PdgStgOrdr(self):
		return self._PdgStgOrdr

	@PdgStgOrdr.setter
	def PdgStgOrdr(self, value):
		self._PdgStgOrdr = value if value is not None else base_types.UninitialisedField(self, 'PdgStgOrdr', TotalAmountAndCurrency1, False)

	@PdgStgOrdr.deleter
	def PdgStgOrdr(self):
		del self._PdgStgOrdr
		self._PdgStgOrdr = base_types.UninitialisedField(self, 'PdgStgOrdr', TotalAmountAndCurrency1, False)

	@property
	def SetPrdfndOrdr(self):
		return self._SetPrdfndOrdr

	@SetPrdfndOrdr.setter
	def SetPrdfndOrdr(self, value):
		self._SetPrdfndOrdr = value if value is not None else base_types.UninitialisedField(self, 'SetPrdfndOrdr', TotalAmountAndCurrency1, False)

	@SetPrdfndOrdr.deleter
	def SetPrdfndOrdr(self):
		del self._SetPrdfndOrdr
		self._SetPrdfndOrdr = base_types.UninitialisedField(self, 'SetPrdfndOrdr', TotalAmountAndCurrency1, False)

	@property
	def SetStgOrdr(self):
		return self._SetStgOrdr

	@SetStgOrdr.setter
	def SetStgOrdr(self, value):
		self._SetStgOrdr = value if value is not None else base_types.UninitialisedField(self, 'SetStgOrdr', TotalAmountAndCurrency1, False)

	@SetStgOrdr.deleter
	def SetStgOrdr(self):
		del self._SetStgOrdr
		self._SetStgOrdr = base_types.UninitialisedField(self, 'SetStgOrdr', TotalAmountAndCurrency1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgPrdfndOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgStgOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SetPrdfndOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SetStgOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
	))