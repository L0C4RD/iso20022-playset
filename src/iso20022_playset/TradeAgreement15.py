import base_types
import Max35Text
import Max4Text
import Exact4AlphaNumericText
import YesNoIndicator
import MatchingSystemReference1Choice
import ISODate

class TradeAgreement15(base_types._BaseFieldType):

	__slots__ = ["_SttlmSsnIdr", "_CmonRef", "_AmdOrCclRsn", "_MtchgSysRef", "_OprScp", "_OprTp", "_PmtVrssPmtInd", "_TradDt", "_OrgtrRef", "_PdctTp"]
	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if type(value) != auto else self.make_default("SttlmSsnIdr")

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = None

	@property
	def CmonRef(self):
		return self._CmonRef

	@CmonRef.setter
	def CmonRef(self, value):
		self._CmonRef = value if type(value) != auto else self.make_default("CmonRef")

	@CmonRef.deleter
	def CmonRef(self):
		del self._CmonRef
		self._CmonRef = None

	@property
	def AmdOrCclRsn(self):
		return self._AmdOrCclRsn

	@AmdOrCclRsn.setter
	def AmdOrCclRsn(self, value):
		self._AmdOrCclRsn = value if type(value) != auto else self.make_default("AmdOrCclRsn")

	@AmdOrCclRsn.deleter
	def AmdOrCclRsn(self):
		del self._AmdOrCclRsn
		self._AmdOrCclRsn = None

	@property
	def MtchgSysRef(self):
		return self._MtchgSysRef

	@MtchgSysRef.setter
	def MtchgSysRef(self, value):
		self._MtchgSysRef = value if type(value) != auto else self.make_default("MtchgSysRef")

	@MtchgSysRef.deleter
	def MtchgSysRef(self):
		del self._MtchgSysRef
		self._MtchgSysRef = None

	@property
	def OprScp(self):
		return self._OprScp

	@OprScp.setter
	def OprScp(self, value):
		self._OprScp = value if type(value) != auto else self.make_default("OprScp")

	@OprScp.deleter
	def OprScp(self):
		del self._OprScp
		self._OprScp = None

	@property
	def OprTp(self):
		return self._OprTp

	@OprTp.setter
	def OprTp(self, value):
		self._OprTp = value if type(value) != auto else self.make_default("OprTp")

	@OprTp.deleter
	def OprTp(self):
		del self._OprTp
		self._OprTp = None

	@property
	def PmtVrssPmtInd(self):
		return self._PmtVrssPmtInd

	@PmtVrssPmtInd.setter
	def PmtVrssPmtInd(self, value):
		self._PmtVrssPmtInd = value if type(value) != auto else self.make_default("PmtVrssPmtInd")

	@PmtVrssPmtInd.deleter
	def PmtVrssPmtInd(self):
		del self._PmtVrssPmtInd
		self._PmtVrssPmtInd = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def OrgtrRef(self):
		return self._OrgtrRef

	@OrgtrRef.setter
	def OrgtrRef(self, value):
		self._OrgtrRef = value if type(value) != auto else self.make_default("OrgtrRef")

	@OrgtrRef.deleter
	def OrgtrRef(self):
		del self._OrgtrRef
		self._OrgtrRef = None

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if type(value) != auto else self.make_default("PdctTp")

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdOrCclRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysRef', type=MatchingSystemReference1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprScp', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTp', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtVrssPmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

