# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrument58
from . import ISINOct2015Identifier

class BasketDescription3(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_Indx"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if value is not None else base_types.UninitialisedField(self, 'Indx', FinancialInstrument58, True)

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = base_types.UninitialisedField(self, 'Indx', FinancialInstrument58, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Indx', type=FinancialInstrument58, min=0, max=None, mutex_group=None, array=True),
	))