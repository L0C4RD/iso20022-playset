# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoanContract4
from . import TradeContract4

class UnderlyingContract4Choice(base_types._BaseFieldType):

	__slots__ = ["_Ln", "_Trad"]
	@property
	def Ln(self):
		return self._Ln

	@Ln.setter
	def Ln(self, value):
		self._Ln = value if value is not None else base_types.UninitialisedField(self, 'Ln', LoanContract4, False)

	@Ln.deleter
	def Ln(self):
		del self._Ln
		self._Ln = base_types.UninitialisedField(self, 'Ln', LoanContract4, False)

	@property
	def Trad(self):
		return self._Trad

	@Trad.setter
	def Trad(self, value):
		self._Trad = value if value is not None else base_types.UninitialisedField(self, 'Trad', TradeContract4, False)

	@Trad.deleter
	def Trad(self):
		del self._Trad
		self._Trad = base_types.UninitialisedField(self, 'Trad', TradeContract4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ln', type=LoanContract4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trad', type=TradeContract4, min=0, max=1, mutex_group=1, array=False),
	))