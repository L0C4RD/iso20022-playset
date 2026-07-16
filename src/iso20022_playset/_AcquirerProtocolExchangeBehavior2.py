# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationProcess2Code
from . import ExchangeConfiguration10
from . import ExchangeConfiguration9
from . import FinancialCapture1Code

class AcquirerProtocolExchangeBehavior2(base_types._BaseFieldType):

	__slots__ = ["_BtchTrf", "_CmpltnXchg", "_CxlXchg", "_FinCaptr"]
	@property
	def BtchTrf(self):
		return self._BtchTrf

	@BtchTrf.setter
	def BtchTrf(self, value):
		self._BtchTrf = value if value is not None else base_types.UninitialisedField(self, 'BtchTrf', ExchangeConfiguration9, False)

	@BtchTrf.deleter
	def BtchTrf(self):
		del self._BtchTrf
		self._BtchTrf = base_types.UninitialisedField(self, 'BtchTrf', ExchangeConfiguration9, False)

	@property
	def CmpltnXchg(self):
		return self._CmpltnXchg

	@CmpltnXchg.setter
	def CmpltnXchg(self, value):
		self._CmpltnXchg = value if value is not None else base_types.UninitialisedField(self, 'CmpltnXchg', ExchangeConfiguration10, False)

	@CmpltnXchg.deleter
	def CmpltnXchg(self):
		del self._CmpltnXchg
		self._CmpltnXchg = base_types.UninitialisedField(self, 'CmpltnXchg', ExchangeConfiguration10, False)

	@property
	def CxlXchg(self):
		return self._CxlXchg

	@CxlXchg.setter
	def CxlXchg(self, value):
		self._CxlXchg = value if value is not None else base_types.UninitialisedField(self, 'CxlXchg', CancellationProcess2Code, False)

	@CxlXchg.deleter
	def CxlXchg(self):
		del self._CxlXchg
		self._CxlXchg = base_types.UninitialisedField(self, 'CxlXchg', CancellationProcess2Code, False)

	@property
	def FinCaptr(self):
		return self._FinCaptr

	@FinCaptr.setter
	def FinCaptr(self, value):
		self._FinCaptr = value if value is not None else base_types.UninitialisedField(self, 'FinCaptr', FinancialCapture1Code, False)

	@FinCaptr.deleter
	def FinCaptr(self):
		del self._FinCaptr
		self._FinCaptr = base_types.UninitialisedField(self, 'FinCaptr', FinancialCapture1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchTrf', type=ExchangeConfiguration9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnXchg', type=ExchangeConfiguration10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlXchg', type=CancellationProcess2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinCaptr', type=FinancialCapture1Code, min=1, max=1, mutex_group=None, array=False),
	))