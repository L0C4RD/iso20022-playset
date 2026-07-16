# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentAttributes119
from . import IntraPositionDetails63
from . import SecurityIdentification20

class FinancialInstrumentDetails44(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmAttrbts", "_FinInstrmId", "_SubBal"]
	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes119, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes119, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@property
	def SubBal(self):
		return self._SubBal

	@SubBal.setter
	def SubBal(self, value):
		self._SubBal = value if value is not None else base_types.UninitialisedField(self, 'SubBal', IntraPositionDetails63, True)

	@SubBal.deleter
	def SubBal(self):
		del self._SubBal
		self._SubBal = base_types.UninitialisedField(self, 'SubBal', IntraPositionDetails63, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes119, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBal', type=IntraPositionDetails63, min=1, max=None, mutex_group=None, array=True),
	))