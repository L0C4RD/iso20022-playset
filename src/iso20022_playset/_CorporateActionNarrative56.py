from . import base_types
from ._UpdatedAdditionalInformation17 import UpdatedAdditionalInformation17

class CorporateActionNarrative56(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_BsktOrIndxInf", "_CertfctnBrkdwn", "_Dsclmr", "_InfConds", "_InfToCmplyWth", "_NrrtvVrsn", "_PrcgTxtForNxtIntrmy", "_PtyCtctNrrtv", "_RegnDtls", "_TaxtnConds"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if type(value) != base_types.auto else self.make_default("AddtlTxt")

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = None

	@property
	def BsktOrIndxInf(self):
		return self._BsktOrIndxInf

	@BsktOrIndxInf.setter
	def BsktOrIndxInf(self, value):
		self._BsktOrIndxInf = value if type(value) != base_types.auto else self.make_default("BsktOrIndxInf")

	@BsktOrIndxInf.deleter
	def BsktOrIndxInf(self):
		del self._BsktOrIndxInf
		self._BsktOrIndxInf = None

	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if type(value) != base_types.auto else self.make_default("CertfctnBrkdwn")

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = None

	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if type(value) != base_types.auto else self.make_default("Dsclmr")

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = None

	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if type(value) != base_types.auto else self.make_default("InfConds")

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = None

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if type(value) != base_types.auto else self.make_default("InfToCmplyWth")

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = None

	@property
	def NrrtvVrsn(self):
		return self._NrrtvVrsn

	@NrrtvVrsn.setter
	def NrrtvVrsn(self, value):
		self._NrrtvVrsn = value if type(value) != base_types.auto else self.make_default("NrrtvVrsn")

	@NrrtvVrsn.deleter
	def NrrtvVrsn(self):
		del self._NrrtvVrsn
		self._NrrtvVrsn = None

	@property
	def PrcgTxtForNxtIntrmy(self):
		return self._PrcgTxtForNxtIntrmy

	@PrcgTxtForNxtIntrmy.setter
	def PrcgTxtForNxtIntrmy(self, value):
		self._PrcgTxtForNxtIntrmy = value if type(value) != base_types.auto else self.make_default("PrcgTxtForNxtIntrmy")

	@PrcgTxtForNxtIntrmy.deleter
	def PrcgTxtForNxtIntrmy(self):
		del self._PrcgTxtForNxtIntrmy
		self._PrcgTxtForNxtIntrmy = None

	@property
	def PtyCtctNrrtv(self):
		return self._PtyCtctNrrtv

	@PtyCtctNrrtv.setter
	def PtyCtctNrrtv(self, value):
		self._PtyCtctNrrtv = value if type(value) != base_types.auto else self.make_default("PtyCtctNrrtv")

	@PtyCtctNrrtv.deleter
	def PtyCtctNrrtv(self):
		del self._PtyCtctNrrtv
		self._PtyCtctNrrtv = None

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if type(value) != base_types.auto else self.make_default("RegnDtls")

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = None

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if type(value) != base_types.auto else self.make_default("TaxtnConds")

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktOrIndxInf', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwn', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsclmr', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfConds', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfToCmplyWth', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrrtvVrsn', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgTxtForNxtIntrmy', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCtctNrrtv', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnConds', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
	))

