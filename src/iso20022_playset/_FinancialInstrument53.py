# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISINOct2015Identifier
from . import LEIIdentifier

class FinancialInstrument53(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_LEI"]
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
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, True)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=None, mutex_group=None, array=True),
	))