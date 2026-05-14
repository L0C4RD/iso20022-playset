from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text

class SplitObligationAttributes1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_OblgtnId", "_SpltSeqNb"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def OblgtnId(self):
		return self._OblgtnId

	@OblgtnId.setter
	def OblgtnId(self, value):
		self._OblgtnId = value if type(value) != base_types.auto else self.make_default("OblgtnId")

	@OblgtnId.deleter
	def OblgtnId(self):
		del self._OblgtnId
		self._OblgtnId = None

	@property
	def SpltSeqNb(self):
		return self._SpltSeqNb

	@SpltSeqNb.setter
	def SpltSeqNb(self, value):
		self._SpltSeqNb = value if type(value) != base_types.auto else self.make_default("SpltSeqNb")

	@SpltSeqNb.deleter
	def SpltSeqNb(self):
		del self._SpltSeqNb
		self._SpltSeqNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltSeqNb', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

