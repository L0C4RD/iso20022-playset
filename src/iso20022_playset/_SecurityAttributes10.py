# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommonFinancialInstrumentAttributes10
from . import FinancialInstrument97
from . import SecurityIdentification39

class SecurityAttributes10(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmAttrbts", "_FinInstrmId", "_FinInstrmTp"]
	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', CommonFinancialInstrumentAttributes10, True)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', CommonFinancialInstrumentAttributes10, True)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification39, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification39, False)

	@property
	def FinInstrmTp(self):
		return self._FinInstrmTp

	@FinInstrmTp.setter
	def FinInstrmTp(self, value):
		self._FinInstrmTp = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmTp', FinancialInstrument97, True)

	@FinInstrmTp.deleter
	def FinInstrmTp(self):
		del self._FinInstrmTp
		self._FinInstrmTp = base_types.UninitialisedField(self, 'FinInstrmTp', FinancialInstrument97, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmAttrbts', type=CommonFinancialInstrumentAttributes10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmTp', type=FinancialInstrument97, min=0, max=None, mutex_group=None, array=True),
	))