from . import base_types
import ExchangeConfiguration10
import FinancialCapture1Code
import ExchangeConfiguration9
import CancellationProcess2Code

class AcquirerProtocolExchangeBehavior2(base_types._BaseFieldType):

	__slots__ = ["_CmpltnXchg", "_BtchTrf", "_CxlXchg", "_FinCaptr"]
	@property
	def CmpltnXchg(self):
		return self._CmpltnXchg

	@CmpltnXchg.setter
	def CmpltnXchg(self, value):
		self._CmpltnXchg = value if type(value) != auto else self.make_default("CmpltnXchg")

	@CmpltnXchg.deleter
	def CmpltnXchg(self):
		del self._CmpltnXchg
		self._CmpltnXchg = None

	@property
	def BtchTrf(self):
		return self._BtchTrf

	@BtchTrf.setter
	def BtchTrf(self, value):
		self._BtchTrf = value if type(value) != auto else self.make_default("BtchTrf")

	@BtchTrf.deleter
	def BtchTrf(self):
		del self._BtchTrf
		self._BtchTrf = None

	@property
	def CxlXchg(self):
		return self._CxlXchg

	@CxlXchg.setter
	def CxlXchg(self, value):
		self._CxlXchg = value if type(value) != auto else self.make_default("CxlXchg")

	@CxlXchg.deleter
	def CxlXchg(self):
		del self._CxlXchg
		self._CxlXchg = None

	@property
	def FinCaptr(self):
		return self._FinCaptr

	@FinCaptr.setter
	def FinCaptr(self, value):
		self._FinCaptr = value if type(value) != auto else self.make_default("FinCaptr")

	@FinCaptr.deleter
	def FinCaptr(self):
		del self._FinCaptr
		self._FinCaptr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmpltnXchg', type=ExchangeConfiguration10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchTrf', type=ExchangeConfiguration9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlXchg', type=CancellationProcess2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinCaptr', type=FinancialCapture1Code, min=1, max=1, mutex_group=None, array=False),
	))

