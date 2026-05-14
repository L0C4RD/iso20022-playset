# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralPortfolioCode5Choice import CollateralPortfolioCode5Choice
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DerivativeEventType3Code import DerivativeEventType3Code
from ._ISODateTime import ISODateTime
from ._MasterAgreement8 import MasterAgreement8
from ._Max140Text import Max140Text
from ._PartyIdentification248Choice import PartyIdentification248Choice
from ._TransactionOperationType10Code import TransactionOperationType10Code
from ._UniqueTransactionIdentifier2Choice import UniqueTransactionIdentifier2Choice

class TradeTransactionIdentification24(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_CollPrtflCd", "_DerivEvtTmStmp", "_DerivEvtTp", "_MstrAgrmt", "_OthrCtrPty", "_RptgTmStmp", "_TechRcrdId", "_UnqIdr"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != base_types.auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if type(value) != base_types.auto else self.make_default("CollPrtflCd")

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = None

	@property
	def DerivEvtTmStmp(self):
		return self._DerivEvtTmStmp

	@DerivEvtTmStmp.setter
	def DerivEvtTmStmp(self, value):
		self._DerivEvtTmStmp = value if type(value) != base_types.auto else self.make_default("DerivEvtTmStmp")

	@DerivEvtTmStmp.deleter
	def DerivEvtTmStmp(self):
		del self._DerivEvtTmStmp
		self._DerivEvtTmStmp = None

	@property
	def DerivEvtTp(self):
		return self._DerivEvtTp

	@DerivEvtTp.setter
	def DerivEvtTp(self, value):
		self._DerivEvtTp = value if type(value) != base_types.auto else self.make_default("DerivEvtTp")

	@DerivEvtTp.deleter
	def DerivEvtTp(self):
		del self._DerivEvtTp
		self._DerivEvtTp = None

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if type(value) != base_types.auto else self.make_default("MstrAgrmt")

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = None

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != base_types.auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	@property
	def RptgTmStmp(self):
		return self._RptgTmStmp

	@RptgTmStmp.setter
	def RptgTmStmp(self, value):
		self._RptgTmStmp = value if type(value) != base_types.auto else self.make_default("RptgTmStmp")

	@RptgTmStmp.deleter
	def RptgTmStmp(self):
		del self._RptgTmStmp
		self._RptgTmStmp = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def UnqIdr(self):
		return self._UnqIdr

	@UnqIdr.setter
	def UnqIdr(self, value):
		self._UnqIdr = value if type(value) != base_types.auto else self.make_default("UnqIdr")

	@UnqIdr.deleter
	def UnqIdr(self):
		del self._UnqIdr
		self._UnqIdr = None

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