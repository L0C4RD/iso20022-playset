# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection49
from . import CalculationMethod1Code
from . import CollateralTransactionAmountBreakdown2
from . import Frequency38Choice
from . import Max3NumericText

class CollateralAmount18(base_types._BaseFieldType):

	__slots__ = ["_Acrd", "_CmpndSmplAcrlClctn", "_IntrstPmtDely", "_PmtFrqcy", "_Termntn", "_Tx", "_TxAmtBrkdwn", "_ValSght"]
	@property
	def Acrd(self):
		return self._Acrd

	@Acrd.setter
	def Acrd(self, value):
		self._Acrd = value if value is not None else base_types.UninitialisedField(self, 'Acrd', AmountAndDirection49, False)

	@Acrd.deleter
	def Acrd(self):
		del self._Acrd
		self._Acrd = base_types.UninitialisedField(self, 'Acrd', AmountAndDirection49, False)

	@property
	def CmpndSmplAcrlClctn(self):
		return self._CmpndSmplAcrlClctn

	@CmpndSmplAcrlClctn.setter
	def CmpndSmplAcrlClctn(self, value):
		self._CmpndSmplAcrlClctn = value if value is not None else base_types.UninitialisedField(self, 'CmpndSmplAcrlClctn', CalculationMethod1Code, False)

	@CmpndSmplAcrlClctn.deleter
	def CmpndSmplAcrlClctn(self):
		del self._CmpndSmplAcrlClctn
		self._CmpndSmplAcrlClctn = base_types.UninitialisedField(self, 'CmpndSmplAcrlClctn', CalculationMethod1Code, False)

	@property
	def IntrstPmtDely(self):
		return self._IntrstPmtDely

	@IntrstPmtDely.setter
	def IntrstPmtDely(self, value):
		self._IntrstPmtDely = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtDely', Max3NumericText, False)

	@IntrstPmtDely.deleter
	def IntrstPmtDely(self):
		del self._IntrstPmtDely
		self._IntrstPmtDely = base_types.UninitialisedField(self, 'IntrstPmtDely', Max3NumericText, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', Frequency38Choice, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', Frequency38Choice, False)

	@property
	def Termntn(self):
		return self._Termntn

	@Termntn.setter
	def Termntn(self, value):
		self._Termntn = value if value is not None else base_types.UninitialisedField(self, 'Termntn', AmountAndDirection49, False)

	@Termntn.deleter
	def Termntn(self):
		del self._Termntn
		self._Termntn = base_types.UninitialisedField(self, 'Termntn', AmountAndDirection49, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', AmountAndDirection49, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', AmountAndDirection49, False)

	@property
	def TxAmtBrkdwn(self):
		return self._TxAmtBrkdwn

	@TxAmtBrkdwn.setter
	def TxAmtBrkdwn(self, value):
		self._TxAmtBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'TxAmtBrkdwn', CollateralTransactionAmountBreakdown2, True)

	@TxAmtBrkdwn.deleter
	def TxAmtBrkdwn(self):
		del self._TxAmtBrkdwn
		self._TxAmtBrkdwn = base_types.UninitialisedField(self, 'TxAmtBrkdwn', CollateralTransactionAmountBreakdown2, True)

	@property
	def ValSght(self):
		return self._ValSght

	@ValSght.setter
	def ValSght(self, value):
		self._ValSght = value if value is not None else base_types.UninitialisedField(self, 'ValSght', AmountAndDirection49, False)

	@ValSght.deleter
	def ValSght(self):
		del self._ValSght
		self._ValSght = base_types.UninitialisedField(self, 'ValSght', AmountAndDirection49, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acrd', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpndSmplAcrlClctn', type=CalculationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmtDely', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termntn', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmtBrkdwn', type=CollateralTransactionAmountBreakdown2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValSght', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
	))