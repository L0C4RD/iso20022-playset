# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentAttributes89
from . import FinancialInstrumentAttributes90

class DefinedAttributes1Choice(base_types._BaseFieldType):

	__slots__ = ["_QtyDfndAttrbts", "_ValDfndAttrbts"]
	@property
	def QtyDfndAttrbts(self):
		return self._QtyDfndAttrbts

	@QtyDfndAttrbts.setter
	def QtyDfndAttrbts(self, value):
		self._QtyDfndAttrbts = value if value is not None else base_types.UninitialisedField(self, 'QtyDfndAttrbts', FinancialInstrumentAttributes89, False)

	@QtyDfndAttrbts.deleter
	def QtyDfndAttrbts(self):
		del self._QtyDfndAttrbts
		self._QtyDfndAttrbts = base_types.UninitialisedField(self, 'QtyDfndAttrbts', FinancialInstrumentAttributes89, False)

	@property
	def ValDfndAttrbts(self):
		return self._ValDfndAttrbts

	@ValDfndAttrbts.setter
	def ValDfndAttrbts(self, value):
		self._ValDfndAttrbts = value if value is not None else base_types.UninitialisedField(self, 'ValDfndAttrbts', FinancialInstrumentAttributes90, False)

	@ValDfndAttrbts.deleter
	def ValDfndAttrbts(self):
		del self._ValDfndAttrbts
		self._ValDfndAttrbts = base_types.UninitialisedField(self, 'ValDfndAttrbts', FinancialInstrumentAttributes90, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyDfndAttrbts', type=FinancialInstrumentAttributes89, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValDfndAttrbts', type=FinancialInstrumentAttributes90, min=0, max=1, mutex_group=1, array=False),
	))