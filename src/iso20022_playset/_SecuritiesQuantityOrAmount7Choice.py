# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINActiveCurrencyAndAmount
from . import SecuritiesOption88

class SecuritiesQuantityOrAmount7Choice(base_types._BaseFieldType):

	__slots__ = ["_InstdAmt", "_SctiesQty"]
	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if value is not None else base_types.UninitialisedField(self, 'InstdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = base_types.UninitialisedField(self, 'InstdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', SecuritiesOption88, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', SecuritiesOption88, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesQty', type=SecuritiesOption88, min=0, max=1, mutex_group=1, array=False),
	))