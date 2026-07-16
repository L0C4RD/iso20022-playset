# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrument59
from . import ISINOct2015Identifier

class GeneralCollateral3(base_types._BaseFieldType):

	__slots__ = ["_ElgblFinInstrmId", "_FinInstrmId"]
	@property
	def ElgblFinInstrmId(self):
		return self._ElgblFinInstrmId

	@ElgblFinInstrmId.setter
	def ElgblFinInstrmId(self, value):
		self._ElgblFinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'ElgblFinInstrmId', ISINOct2015Identifier, True)

	@ElgblFinInstrmId.deleter
	def ElgblFinInstrmId(self):
		del self._ElgblFinInstrmId
		self._ElgblFinInstrmId = base_types.UninitialisedField(self, 'ElgblFinInstrmId', ISINOct2015Identifier, True)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', FinancialInstrument59, True)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', FinancialInstrument59, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblFinInstrmId', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=FinancialInstrument59, min=0, max=None, mutex_group=None, array=True),
	))