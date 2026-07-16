# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max15NumericText
from . import Max35Text

class SplitObligationAttributes1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_OblgtnId", "_SpltSeqNb"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def OblgtnId(self):
		return self._OblgtnId

	@OblgtnId.setter
	def OblgtnId(self, value):
		self._OblgtnId = value if value is not None else base_types.UninitialisedField(self, 'OblgtnId', Max35Text, False)

	@OblgtnId.deleter
	def OblgtnId(self):
		del self._OblgtnId
		self._OblgtnId = base_types.UninitialisedField(self, 'OblgtnId', Max35Text, False)

	@property
	def SpltSeqNb(self):
		return self._SpltSeqNb

	@SpltSeqNb.setter
	def SpltSeqNb(self, value):
		self._SpltSeqNb = value if value is not None else base_types.UninitialisedField(self, 'SpltSeqNb', Max15NumericText, False)

	@SpltSeqNb.deleter
	def SpltSeqNb(self):
		del self._SpltSeqNb
		self._SpltSeqNb = base_types.UninitialisedField(self, 'SpltSeqNb', Max15NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltSeqNb', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))