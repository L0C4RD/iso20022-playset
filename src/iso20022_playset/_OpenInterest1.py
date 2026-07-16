# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd24Amount
from . import PositiveNumber

class OpenInterest1(base_types._BaseFieldType):

	__slots__ = ["_GrssNtnlAmt", "_NbOfLots"]
	@property
	def GrssNtnlAmt(self):
		return self._GrssNtnlAmt

	@GrssNtnlAmt.setter
	def GrssNtnlAmt(self, value):
		self._GrssNtnlAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssNtnlAmt', ActiveCurrencyAnd24Amount, False)

	@GrssNtnlAmt.deleter
	def GrssNtnlAmt(self):
		del self._GrssNtnlAmt
		self._GrssNtnlAmt = base_types.UninitialisedField(self, 'GrssNtnlAmt', ActiveCurrencyAnd24Amount, False)

	@property
	def NbOfLots(self):
		return self._NbOfLots

	@NbOfLots.setter
	def NbOfLots(self, value):
		self._NbOfLots = value if value is not None else base_types.UninitialisedField(self, 'NbOfLots', PositiveNumber, False)

	@NbOfLots.deleter
	def NbOfLots(self):
		del self._NbOfLots
		self._NbOfLots = base_types.UninitialisedField(self, 'NbOfLots', PositiveNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrssNtnlAmt', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfLots', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))