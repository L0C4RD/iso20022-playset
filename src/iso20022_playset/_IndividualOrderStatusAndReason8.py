from . import base_types
from .InvestmentAccount58 import InvestmentAccount58
from .Max35Text import Max35Text
from .CancellationStatus22Choice import CancellationStatus22Choice
from .PartyIdentification113 import PartyIdentification113
from .FinancialInstrument57 import FinancialInstrument57

class IndividualOrderStatusAndReason8(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmDtls", "_OrdrRef", "_StsInitr", "_CxlRef", "_InvstmtAcctDtls", "_MstrRef", "_CxlSts", "_ClntRef"]
	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != base_types.auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if type(value) != base_types.auto else self.make_default("StsInitr")

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = None

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if type(value) != base_types.auto else self.make_default("CxlRef")

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != base_types.auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if type(value) != base_types.auto else self.make_default("CxlSts")

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument57, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlSts', type=CancellationStatus22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

