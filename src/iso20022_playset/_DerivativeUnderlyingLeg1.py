# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DefinedAttributes1Choice
from . import FinancialInstrumentAttributes88

class DerivativeUnderlyingLeg1(base_types._BaseFieldType):

	__slots__ = ["_CtrctAttrbts", "_DfndAttrbts"]
	@property
	def CtrctAttrbts(self):
		return self._CtrctAttrbts

	@CtrctAttrbts.setter
	def CtrctAttrbts(self, value):
		self._CtrctAttrbts = value if value is not None else base_types.UninitialisedField(self, 'CtrctAttrbts', FinancialInstrumentAttributes88, False)

	@CtrctAttrbts.deleter
	def CtrctAttrbts(self):
		del self._CtrctAttrbts
		self._CtrctAttrbts = base_types.UninitialisedField(self, 'CtrctAttrbts', FinancialInstrumentAttributes88, False)

	@property
	def DfndAttrbts(self):
		return self._DfndAttrbts

	@DfndAttrbts.setter
	def DfndAttrbts(self, value):
		self._DfndAttrbts = value if value is not None else base_types.UninitialisedField(self, 'DfndAttrbts', DefinedAttributes1Choice, False)

	@DfndAttrbts.deleter
	def DfndAttrbts(self):
		del self._DfndAttrbts
		self._DfndAttrbts = base_types.UninitialisedField(self, 'DfndAttrbts', DefinedAttributes1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctAttrbts', type=FinancialInstrumentAttributes88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfndAttrbts', type=DefinedAttributes1Choice, min=0, max=1, mutex_group=None, array=False),
	))