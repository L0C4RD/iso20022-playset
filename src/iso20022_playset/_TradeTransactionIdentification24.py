# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralPortfolioCode5Choice
from . import DateAndDateTime2Choice
from . import DerivativeEventType3Code
from . import ISODateTime
from . import MasterAgreement8
from . import Max140Text
from . import PartyIdentification248Choice
from . import TransactionOperationType10Code
from . import UniqueTransactionIdentifier2Choice

class TradeTransactionIdentification24(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_CollPrtflCd", "_DerivEvtTmStmp", "_DerivEvtTp", "_MstrAgrmt", "_OthrCtrPty", "_RptgTmStmp", "_TechRcrdId", "_UnqIdr"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType10Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType10Code, False)

	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if value is not None else base_types.UninitialisedField(self, 'CollPrtflCd', CollateralPortfolioCode5Choice, False)

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = base_types.UninitialisedField(self, 'CollPrtflCd', CollateralPortfolioCode5Choice, False)

	@property
	def DerivEvtTmStmp(self):
		return self._DerivEvtTmStmp

	@DerivEvtTmStmp.setter
	def DerivEvtTmStmp(self, value):
		self._DerivEvtTmStmp = value if value is not None else base_types.UninitialisedField(self, 'DerivEvtTmStmp', DateAndDateTime2Choice, False)

	@DerivEvtTmStmp.deleter
	def DerivEvtTmStmp(self):
		del self._DerivEvtTmStmp
		self._DerivEvtTmStmp = base_types.UninitialisedField(self, 'DerivEvtTmStmp', DateAndDateTime2Choice, False)

	@property
	def DerivEvtTp(self):
		return self._DerivEvtTp

	@DerivEvtTp.setter
	def DerivEvtTp(self, value):
		self._DerivEvtTp = value if value is not None else base_types.UninitialisedField(self, 'DerivEvtTp', DerivativeEventType3Code, False)

	@DerivEvtTp.deleter
	def DerivEvtTp(self):
		del self._DerivEvtTp
		self._DerivEvtTp = base_types.UninitialisedField(self, 'DerivEvtTp', DerivativeEventType3Code, False)

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement8, False)

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement8, False)

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', PartyIdentification248Choice, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', PartyIdentification248Choice, False)

	@property
	def RptgTmStmp(self):
		return self._RptgTmStmp

	@RptgTmStmp.setter
	def RptgTmStmp(self, value):
		self._RptgTmStmp = value if value is not None else base_types.UninitialisedField(self, 'RptgTmStmp', ISODateTime, False)

	@RptgTmStmp.deleter
	def RptgTmStmp(self):
		del self._RptgTmStmp
		self._RptgTmStmp = base_types.UninitialisedField(self, 'RptgTmStmp', ISODateTime, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@property
	def UnqIdr(self):
		return self._UnqIdr

	@UnqIdr.setter
	def UnqIdr(self, value):
		self._UnqIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqIdr', UniqueTransactionIdentifier2Choice, False)

	@UnqIdr.deleter
	def UnqIdr(self):
		del self._UnqIdr
		self._UnqIdr = base_types.UninitialisedField(self, 'UnqIdr', UniqueTransactionIdentifier2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflCd', type=CollateralPortfolioCode5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivEvtTmStmp', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivEvtTp', type=DerivativeEventType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=PartyIdentification248Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqIdr', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
	))