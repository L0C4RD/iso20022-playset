# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Max15NumericText
from . import TransactionIndividualStatus1Code

class NumberOfTransactionsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_DtldCtrlSum", "_DtldNbOfTxs", "_DtldSts"]
	@property
	def DtldCtrlSum(self):
		return self._DtldCtrlSum

	@DtldCtrlSum.setter
	def DtldCtrlSum(self, value):
		self._DtldCtrlSum = value if value is not None else base_types.UninitialisedField(self, 'DtldCtrlSum', DecimalNumber, False)

	@DtldCtrlSum.deleter
	def DtldCtrlSum(self):
		del self._DtldCtrlSum
		self._DtldCtrlSum = base_types.UninitialisedField(self, 'DtldCtrlSum', DecimalNumber, False)

	@property
	def DtldNbOfTxs(self):
		return self._DtldNbOfTxs

	@DtldNbOfTxs.setter
	def DtldNbOfTxs(self, value):
		self._DtldNbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'DtldNbOfTxs', Max15NumericText, False)

	@DtldNbOfTxs.deleter
	def DtldNbOfTxs(self):
		del self._DtldNbOfTxs
		self._DtldNbOfTxs = base_types.UninitialisedField(self, 'DtldNbOfTxs', Max15NumericText, False)

	@property
	def DtldSts(self):
		return self._DtldSts

	@DtldSts.setter
	def DtldSts(self, value):
		self._DtldSts = value if value is not None else base_types.UninitialisedField(self, 'DtldSts', TransactionIndividualStatus1Code, False)

	@DtldSts.deleter
	def DtldSts(self):
		del self._DtldSts
		self._DtldSts = base_types.UninitialisedField(self, 'DtldSts', TransactionIndividualStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldNbOfTxs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldSts', type=TransactionIndividualStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))