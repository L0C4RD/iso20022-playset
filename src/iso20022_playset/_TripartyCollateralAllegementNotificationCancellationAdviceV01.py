# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection49
from . import CollateralParties8
from . import CollateralRole1Code
from . import CollateralTransactionType1Choice
from . import DateAndDateTime2Choice
from . import ExposureType23Choice
from . import GenericIdentification1
from . import SupplementaryData1
from . import TransactionIdentifications44

class TripartyCollateralAllegementNotificationCancellationAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_CollPties", "_CollSd", "_CollTxTp", "_ElgbltySetPrfl", "_ReqdExctnDt", "_SplmtryData", "_TxAmt", "_TxInstrId", "_XpsrTp"]
	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if value is not None else base_types.UninitialisedField(self, 'CollPties', CollateralParties8, False)

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = base_types.UninitialisedField(self, 'CollPties', CollateralParties8, False)

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if value is not None else base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@property
	def CollTxTp(self):
		return self._CollTxTp

	@CollTxTp.setter
	def CollTxTp(self, value):
		self._CollTxTp = value if value is not None else base_types.UninitialisedField(self, 'CollTxTp', CollateralTransactionType1Choice, False)

	@CollTxTp.deleter
	def CollTxTp(self):
		del self._CollTxTp
		self._CollTxTp = base_types.UninitialisedField(self, 'CollTxTp', CollateralTransactionType1Choice, False)

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if value is not None else base_types.UninitialisedField(self, 'TxAmt', AmountAndDirection49, False)

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = base_types.UninitialisedField(self, 'TxAmt', AmountAndDirection49, False)

	@property
	def TxInstrId(self):
		return self._TxInstrId

	@TxInstrId.setter
	def TxInstrId(self, value):
		self._TxInstrId = value if value is not None else base_types.UninitialisedField(self, 'TxInstrId', TransactionIdentifications44, False)

	@TxInstrId.deleter
	def TxInstrId(self):
		del self._TxInstrId
		self._TxInstrId = base_types.UninitialisedField(self, 'TxInstrId', TransactionIdentifications44, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPties', type=CollateralParties8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTxTp', type=CollateralTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmt', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInstrId', type=TransactionIdentifications44, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))