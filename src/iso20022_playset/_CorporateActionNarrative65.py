# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UpdatedAdditionalInformation26
from . import UpdatedURLlnformation7

class CorporateActionNarrative65(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_BsktOrIndxInf", "_CertfctnBrkdwn", "_Dsclmr", "_InfConds", "_InfToCmplyWth", "_NrrtvVrsn", "_PrcgTxtForNxtIntrmy", "_PtyCtctNrrtv", "_RegnDtls", "_TaxtnConds", "_URLAdr"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxt', UpdatedAdditionalInformation26, True)

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = base_types.UninitialisedField(self, 'AddtlTxt', UpdatedAdditionalInformation26, True)

	@property
	def BsktOrIndxInf(self):
		return self._BsktOrIndxInf

	@BsktOrIndxInf.setter
	def BsktOrIndxInf(self, value):
		self._BsktOrIndxInf = value if value is not None else base_types.UninitialisedField(self, 'BsktOrIndxInf', UpdatedAdditionalInformation26, True)

	@BsktOrIndxInf.deleter
	def BsktOrIndxInf(self):
		del self._BsktOrIndxInf
		self._BsktOrIndxInf = base_types.UninitialisedField(self, 'BsktOrIndxInf', UpdatedAdditionalInformation26, True)

	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwn', UpdatedAdditionalInformation26, True)

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = base_types.UninitialisedField(self, 'CertfctnBrkdwn', UpdatedAdditionalInformation26, True)

	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if value is not None else base_types.UninitialisedField(self, 'Dsclmr', UpdatedAdditionalInformation26, True)

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = base_types.UninitialisedField(self, 'Dsclmr', UpdatedAdditionalInformation26, True)

	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if value is not None else base_types.UninitialisedField(self, 'InfConds', UpdatedAdditionalInformation26, True)

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = base_types.UninitialisedField(self, 'InfConds', UpdatedAdditionalInformation26, True)

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if value is not None else base_types.UninitialisedField(self, 'InfToCmplyWth', UpdatedAdditionalInformation26, True)

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = base_types.UninitialisedField(self, 'InfToCmplyWth', UpdatedAdditionalInformation26, True)

	@property
	def NrrtvVrsn(self):
		return self._NrrtvVrsn

	@NrrtvVrsn.setter
	def NrrtvVrsn(self, value):
		self._NrrtvVrsn = value if value is not None else base_types.UninitialisedField(self, 'NrrtvVrsn', UpdatedAdditionalInformation26, True)

	@NrrtvVrsn.deleter
	def NrrtvVrsn(self):
		del self._NrrtvVrsn
		self._NrrtvVrsn = base_types.UninitialisedField(self, 'NrrtvVrsn', UpdatedAdditionalInformation26, True)

	@property
	def PrcgTxtForNxtIntrmy(self):
		return self._PrcgTxtForNxtIntrmy

	@PrcgTxtForNxtIntrmy.setter
	def PrcgTxtForNxtIntrmy(self, value):
		self._PrcgTxtForNxtIntrmy = value if value is not None else base_types.UninitialisedField(self, 'PrcgTxtForNxtIntrmy', UpdatedAdditionalInformation26, True)

	@PrcgTxtForNxtIntrmy.deleter
	def PrcgTxtForNxtIntrmy(self):
		del self._PrcgTxtForNxtIntrmy
		self._PrcgTxtForNxtIntrmy = base_types.UninitialisedField(self, 'PrcgTxtForNxtIntrmy', UpdatedAdditionalInformation26, True)

	@property
	def PtyCtctNrrtv(self):
		return self._PtyCtctNrrtv

	@PtyCtctNrrtv.setter
	def PtyCtctNrrtv(self, value):
		self._PtyCtctNrrtv = value if value is not None else base_types.UninitialisedField(self, 'PtyCtctNrrtv', UpdatedAdditionalInformation26, True)

	@PtyCtctNrrtv.deleter
	def PtyCtctNrrtv(self):
		del self._PtyCtctNrrtv
		self._PtyCtctNrrtv = base_types.UninitialisedField(self, 'PtyCtctNrrtv', UpdatedAdditionalInformation26, True)

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if value is not None else base_types.UninitialisedField(self, 'RegnDtls', UpdatedAdditionalInformation26, True)

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = base_types.UninitialisedField(self, 'RegnDtls', UpdatedAdditionalInformation26, True)

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if value is not None else base_types.UninitialisedField(self, 'TaxtnConds', UpdatedAdditionalInformation26, True)

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = base_types.UninitialisedField(self, 'TaxtnConds', UpdatedAdditionalInformation26, True)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', UpdatedURLlnformation7, True)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', UpdatedURLlnformation7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BsktOrIndxInf', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnBrkdwn', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dsclmr', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfConds', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfToCmplyWth', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrrtvVrsn', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgTxtForNxtIntrmy', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyCtctNrrtv', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnDtls', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxtnConds', type=UpdatedAdditionalInformation26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='URLAdr', type=UpdatedURLlnformation7, min=0, max=None, mutex_group=None, array=True),
	))