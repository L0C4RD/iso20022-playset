# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd19DecimalAmount
from . import Max20PositiveNumber
from . import NotionalAmountLegs6

class PositionSetTotal2(base_types._BaseFieldType):

	__slots__ = ["_NbOfTrds", "_NegVal", "_Ntnl", "_OthrPmtAmt", "_PostvVal"]
	@property
	def NbOfTrds(self):
		return self._NbOfTrds

	@NbOfTrds.setter
	def NbOfTrds(self, value):
		self._NbOfTrds = value if value is not None else base_types.UninitialisedField(self, 'NbOfTrds', Max20PositiveNumber, False)

	@NbOfTrds.deleter
	def NbOfTrds(self):
		del self._NbOfTrds
		self._NbOfTrds = base_types.UninitialisedField(self, 'NbOfTrds', Max20PositiveNumber, False)

	@property
	def NegVal(self):
		return self._NegVal

	@NegVal.setter
	def NegVal(self, value):
		self._NegVal = value if value is not None else base_types.UninitialisedField(self, 'NegVal', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@NegVal.deleter
	def NegVal(self):
		del self._NegVal
		self._NegVal = base_types.UninitialisedField(self, 'NegVal', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@property
	def Ntnl(self):
		return self._Ntnl

	@Ntnl.setter
	def Ntnl(self, value):
		self._Ntnl = value if value is not None else base_types.UninitialisedField(self, 'Ntnl', NotionalAmountLegs6, False)

	@Ntnl.deleter
	def Ntnl(self):
		del self._Ntnl
		self._Ntnl = base_types.UninitialisedField(self, 'Ntnl', NotionalAmountLegs6, False)

	@property
	def OthrPmtAmt(self):
		return self._OthrPmtAmt

	@OthrPmtAmt.setter
	def OthrPmtAmt(self, value):
		self._OthrPmtAmt = value if value is not None else base_types.UninitialisedField(self, 'OthrPmtAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, True)

	@OthrPmtAmt.deleter
	def OthrPmtAmt(self):
		del self._OthrPmtAmt
		self._OthrPmtAmt = base_types.UninitialisedField(self, 'OthrPmtAmt', ActiveOrHistoricCurrencyAnd19DecimalAmount, True)

	@property
	def PostvVal(self):
		return self._PostvVal

	@PostvVal.setter
	def PostvVal(self, value):
		self._PostvVal = value if value is not None else base_types.UninitialisedField(self, 'PostvVal', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@PostvVal.deleter
	def PostvVal(self):
		del self._PostvVal
		self._PostvVal = base_types.UninitialisedField(self, 'PostvVal', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfTrds', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NegVal', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntnl', type=NotionalAmountLegs6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PostvVal', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))