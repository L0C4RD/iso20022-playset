# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection55
from . import CorporateActionEventType101Choice
from . import DateAndDateTime2Choice
from . import FinancialInstrumentQuantity36Choice
from . import GenericIdentification39
from . import ISODateTime
from . import References75Choice
from . import RestrictedFINXMax350Text
from . import SecuritiesBalanceType8Choice
from . import SupplementaryData1

class IntraPositionMovementDetails20(base_types._BaseFieldType):

	__slots__ = ["_AckdStsTmStmp", "_AvlblDt", "_BalTo", "_CollMntrAmt", "_CorpActnEvtTp", "_Id", "_InstrPrcgAddtlDtls", "_PrevslySttldQty", "_RmngToBeSttldQty", "_SctiesSubBalId", "_SplmtryData", "_SttldQty", "_SttlmDt"]
	@property
	def AckdStsTmStmp(self):
		return self._AckdStsTmStmp

	@AckdStsTmStmp.setter
	def AckdStsTmStmp(self, value):
		self._AckdStsTmStmp = value if value is not None else base_types.UninitialisedField(self, 'AckdStsTmStmp', ISODateTime, False)

	@AckdStsTmStmp.deleter
	def AckdStsTmStmp(self):
		del self._AckdStsTmStmp
		self._AckdStsTmStmp = base_types.UninitialisedField(self, 'AckdStsTmStmp', ISODateTime, False)

	@property
	def AvlblDt(self):
		return self._AvlblDt

	@AvlblDt.setter
	def AvlblDt(self, value):
		self._AvlblDt = value if value is not None else base_types.UninitialisedField(self, 'AvlblDt', DateAndDateTime2Choice, False)

	@AvlblDt.deleter
	def AvlblDt(self):
		del self._AvlblDt
		self._AvlblDt = base_types.UninitialisedField(self, 'AvlblDt', DateAndDateTime2Choice, False)

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if value is not None else base_types.UninitialisedField(self, 'BalTo', SecuritiesBalanceType8Choice, False)

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = base_types.UninitialisedField(self, 'BalTo', SecuritiesBalanceType8Choice, False)

	@property
	def CollMntrAmt(self):
		return self._CollMntrAmt

	@CollMntrAmt.setter
	def CollMntrAmt(self, value):
		self._CollMntrAmt = value if value is not None else base_types.UninitialisedField(self, 'CollMntrAmt', AmountAndDirection55, False)

	@CollMntrAmt.deleter
	def CollMntrAmt(self):
		del self._CollMntrAmt
		self._CollMntrAmt = base_types.UninitialisedField(self, 'CollMntrAmt', AmountAndDirection55, False)

	@property
	def CorpActnEvtTp(self):
		return self._CorpActnEvtTp

	@CorpActnEvtTp.setter
	def CorpActnEvtTp(self, value):
		self._CorpActnEvtTp = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtTp', CorporateActionEventType101Choice, False)

	@CorpActnEvtTp.deleter
	def CorpActnEvtTp(self):
		del self._CorpActnEvtTp
		self._CorpActnEvtTp = base_types.UninitialisedField(self, 'CorpActnEvtTp', CorporateActionEventType101Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', References75Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', References75Choice, False)

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', RestrictedFINXMax350Text, False)

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', RestrictedFINXMax350Text, False)

	@property
	def PrevslySttldQty(self):
		return self._PrevslySttldQty

	@PrevslySttldQty.setter
	def PrevslySttldQty(self, value):
		self._PrevslySttldQty = value if value is not None else base_types.UninitialisedField(self, 'PrevslySttldQty', FinancialInstrumentQuantity36Choice, False)

	@PrevslySttldQty.deleter
	def PrevslySttldQty(self):
		del self._PrevslySttldQty
		self._PrevslySttldQty = base_types.UninitialisedField(self, 'PrevslySttldQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def RmngToBeSttldQty(self):
		return self._RmngToBeSttldQty

	@RmngToBeSttldQty.setter
	def RmngToBeSttldQty(self, value):
		self._RmngToBeSttldQty = value if value is not None else base_types.UninitialisedField(self, 'RmngToBeSttldQty', FinancialInstrumentQuantity36Choice, False)

	@RmngToBeSttldQty.deleter
	def RmngToBeSttldQty(self):
		del self._RmngToBeSttldQty
		self._RmngToBeSttldQty = base_types.UninitialisedField(self, 'RmngToBeSttldQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def SctiesSubBalId(self):
		return self._SctiesSubBalId

	@SctiesSubBalId.setter
	def SctiesSubBalId(self, value):
		self._SctiesSubBalId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSubBalId', GenericIdentification39, False)

	@SctiesSubBalId.deleter
	def SctiesSubBalId(self):
		del self._SctiesSubBalId
		self._SctiesSubBalId = base_types.UninitialisedField(self, 'SctiesSubBalId', GenericIdentification39, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if value is not None else base_types.UninitialisedField(self, 'SttldQty', FinancialInstrumentQuantity36Choice, False)

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = base_types.UninitialisedField(self, 'SttldQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', DateAndDateTime2Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=SecuritiesBalanceType8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMntrAmt', type=AmountAndDirection55, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtTp', type=CorporateActionEventType101Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=References75Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalId', type=GenericIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttldQty', type=FinancialInstrumentQuantity36Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))