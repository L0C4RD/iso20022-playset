from . import base_types
import UpdatedAdditionalInformation17
import UpdatedAdditionalInformation18

class CorporateActionNarrative57(base_types._BaseFieldType):

	__slots__ = ["_NrrtvVrsn", "_AddtlTxt", "_Dsclmr", "_InfToCmplyWth", "_InfConds", "_CertfctnBrkdwn", "_TaxtnConds", "_SctyRstrctn"]
	@property
	def NrrtvVrsn(self):
		return self._NrrtvVrsn

	@NrrtvVrsn.setter
	def NrrtvVrsn(self, value):
		self._NrrtvVrsn = value if type(value) != auto else self.make_default("NrrtvVrsn")

	@NrrtvVrsn.deleter
	def NrrtvVrsn(self):
		del self._NrrtvVrsn
		self._NrrtvVrsn = None

	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if type(value) != auto else self.make_default("AddtlTxt")

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = None

	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if type(value) != auto else self.make_default("Dsclmr")

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = None

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if type(value) != auto else self.make_default("InfToCmplyWth")

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = None

	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if type(value) != auto else self.make_default("InfConds")

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = None

	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if type(value) != auto else self.make_default("CertfctnBrkdwn")

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = None

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if type(value) != auto else self.make_default("TaxtnConds")

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = None

	@property
	def SctyRstrctn(self):
		return self._SctyRstrctn

	@SctyRstrctn.setter
	def SctyRstrctn(self, value):
		self._SctyRstrctn = value if type(value) != auto else self.make_default("SctyRstrctn")

	@SctyRstrctn.deleter
	def SctyRstrctn(self):
		del self._SctyRstrctn
		self._SctyRstrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NrrtvVrsn', type=UpdatedAdditionalInformation18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTxt', type=UpdatedAdditionalInformation18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsclmr', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfToCmplyWth', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfConds', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwn', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnConds', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyRstrctn', type=UpdatedAdditionalInformation17, min=0, max=1, mutex_group=None, array=False),
	))

