import base_types
import AccountIdentification73Choice
import SupplementaryData1
import PartyIdentification120Choice
import Max8000Text
import CorporateActionGeneralInformation174
import CorporateActionCancellation3
import CorporateAction72

class CorporateActionCancellationAdviceV13(base_types._BaseFieldType):

	__slots__ = ["_PngAgt", "_SplmtryData", "_SlctnAgt", "_IssrAgt", "_Regar", "_InfAgt", "_AcctsDtls", "_CorpActnDtls", "_CorpActnGnlInf", "_PhysSctiesAgt", "_CxlAdvcGnlInf", "_RsellngAgt", "_DrpAgt", "_AddtlTxt", "_SubPngAgt"]
	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if type(value) != auto else self.make_default("PngAgt")

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SlctnAgt(self):
		return self._SlctnAgt

	@SlctnAgt.setter
	def SlctnAgt(self, value):
		self._SlctnAgt = value if type(value) != auto else self.make_default("SlctnAgt")

	@SlctnAgt.deleter
	def SlctnAgt(self):
		del self._SlctnAgt
		self._SlctnAgt = None

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if type(value) != auto else self.make_default("IssrAgt")

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = None

	@property
	def Regar(self):
		return self._Regar

	@Regar.setter
	def Regar(self, value):
		self._Regar = value if type(value) != auto else self.make_default("Regar")

	@Regar.deleter
	def Regar(self):
		del self._Regar
		self._Regar = None

	@property
	def InfAgt(self):
		return self._InfAgt

	@InfAgt.setter
	def InfAgt(self, value):
		self._InfAgt = value if type(value) != auto else self.make_default("InfAgt")

	@InfAgt.deleter
	def InfAgt(self):
		del self._InfAgt
		self._InfAgt = None

	@property
	def AcctsDtls(self):
		return self._AcctsDtls

	@AcctsDtls.setter
	def AcctsDtls(self, value):
		self._AcctsDtls = value if type(value) != auto else self.make_default("AcctsDtls")

	@AcctsDtls.deleter
	def AcctsDtls(self):
		del self._AcctsDtls
		self._AcctsDtls = None

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def PhysSctiesAgt(self):
		return self._PhysSctiesAgt

	@PhysSctiesAgt.setter
	def PhysSctiesAgt(self, value):
		self._PhysSctiesAgt = value if type(value) != auto else self.make_default("PhysSctiesAgt")

	@PhysSctiesAgt.deleter
	def PhysSctiesAgt(self):
		del self._PhysSctiesAgt
		self._PhysSctiesAgt = None

	@property
	def CxlAdvcGnlInf(self):
		return self._CxlAdvcGnlInf

	@CxlAdvcGnlInf.setter
	def CxlAdvcGnlInf(self, value):
		self._CxlAdvcGnlInf = value if type(value) != auto else self.make_default("CxlAdvcGnlInf")

	@CxlAdvcGnlInf.deleter
	def CxlAdvcGnlInf(self):
		del self._CxlAdvcGnlInf
		self._CxlAdvcGnlInf = None

	@property
	def RsellngAgt(self):
		return self._RsellngAgt

	@RsellngAgt.setter
	def RsellngAgt(self, value):
		self._RsellngAgt = value if type(value) != auto else self.make_default("RsellngAgt")

	@RsellngAgt.deleter
	def RsellngAgt(self):
		del self._RsellngAgt
		self._RsellngAgt = None

	@property
	def DrpAgt(self):
		return self._DrpAgt

	@DrpAgt.setter
	def DrpAgt(self, value):
		self._DrpAgt = value if type(value) != auto else self.make_default("DrpAgt")

	@DrpAgt.deleter
	def DrpAgt(self):
		del self._DrpAgt
		self._DrpAgt = None

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
	def SubPngAgt(self):
		return self._SubPngAgt

	@SubPngAgt.setter
	def SubPngAgt(self, value):
		self._SubPngAgt = value if type(value) != auto else self.make_default("SubPngAgt")

	@SubPngAgt.deleter
	def SubPngAgt(self):
		del self._SubPngAgt
		self._SubPngAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SlctnAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Regar', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfAgt', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctsDtls', type=AccountIdentification73Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation174, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysSctiesAgt', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlAdvcGnlInf', type=CorporateActionCancellation3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsellngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DrpAgt', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTxt', type=Max8000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubPngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
	))

