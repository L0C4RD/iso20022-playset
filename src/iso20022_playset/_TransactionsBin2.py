# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import FromToQuantityRange2
from . import Number

class TransactionsBin2(base_types._BaseFieldType):

	__slots__ = ["_NbOfTxs", "_Rg", "_TtlNtnlAmt"]
	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxs', Number, False)

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = base_types.UninitialisedField(self, 'NbOfTxs', Number, False)

	@property
	def Rg(self):
		return self._Rg

	@Rg.setter
	def Rg(self, value):
		self._Rg = value if value is not None else base_types.UninitialisedField(self, 'Rg', FromToQuantityRange2, False)

	@Rg.deleter
	def Rg(self):
		del self._Rg
		self._Rg = base_types.UninitialisedField(self, 'Rg', FromToQuantityRange2, False)

	@property
	def TtlNtnlAmt(self):
		return self._TtlNtnlAmt

	@TtlNtnlAmt.setter
	def TtlNtnlAmt(self, value):
		self._TtlNtnlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlNtnlAmt', DecimalNumber, False)

	@TtlNtnlAmt.deleter
	def TtlNtnlAmt(self):
		del self._TtlNtnlAmt
		self._TtlNtnlAmt = base_types.UninitialisedField(self, 'TtlNtnlAmt', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfTxs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rg', type=FromToQuantityRange2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNtnlAmt', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))