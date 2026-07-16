# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat49Choice
from . import PartyIdentification136Choice

class BorrowerLendingDeadline6(base_types._BaseFieldType):

	__slots__ = ["_Brrwr", "_StockLndgDdln"]
	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if value is not None else base_types.UninitialisedField(self, 'Brrwr', PartyIdentification136Choice, False)

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = base_types.UninitialisedField(self, 'Brrwr', PartyIdentification136Choice, False)

	@property
	def StockLndgDdln(self):
		return self._StockLndgDdln

	@StockLndgDdln.setter
	def StockLndgDdln(self, value):
		self._StockLndgDdln = value if value is not None else base_types.UninitialisedField(self, 'StockLndgDdln', DateFormat49Choice, False)

	@StockLndgDdln.deleter
	def StockLndgDdln(self):
		del self._StockLndgDdln
		self._StockLndgDdln = base_types.UninitialisedField(self, 'StockLndgDdln', DateFormat49Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brrwr', type=PartyIdentification136Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLndgDdln', type=DateFormat49Choice, min=1, max=1, mutex_group=None, array=False),
	))