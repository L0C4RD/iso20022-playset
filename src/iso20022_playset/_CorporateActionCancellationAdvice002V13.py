# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification74Choice
from . import CorporateAction74
from . import CorporateActionCancellation4
from . import CorporateActionGeneralInformation184
from . import PartyIdentification137Choice
from . import RestrictedFINZMax8000Text
from . import SupplementaryData1

class CorporateActionCancellationAdvice002V13(base_types._BaseFieldType):

	__slots__ = ["_AcctsDtls", "_AddtlTxt", "_CorpActnDtls", "_CorpActnGnlInf", "_CxlAdvcGnlInf", "_DrpAgt", "_InfAgt", "_IssrAgt", "_PhysSctiesAgt", "_PngAgt", "_Regar", "_RsellngAgt", "_SlctnAgt", "_SplmtryData", "_SubPngAgt"]
	@property
	def AcctsDtls(self):
		return self._AcctsDtls

	@AcctsDtls.setter
	def AcctsDtls(self, value):
		self._AcctsDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctsDtls', AccountIdentification74Choice, False)

	@AcctsDtls.deleter
	def AcctsDtls(self):
		del self._AcctsDtls
		self._AcctsDtls = base_types.UninitialisedField(self, 'AcctsDtls', AccountIdentification74Choice, False)

	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxt', RestrictedFINZMax8000Text, True)

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = base_types.UninitialisedField(self, 'AddtlTxt', RestrictedFINZMax8000Text, True)

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction74, False)

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction74, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation184, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation184, False)

	@property
	def CxlAdvcGnlInf(self):
		return self._CxlAdvcGnlInf

	@CxlAdvcGnlInf.setter
	def CxlAdvcGnlInf(self, value):
		self._CxlAdvcGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CxlAdvcGnlInf', CorporateActionCancellation4, False)

	@CxlAdvcGnlInf.deleter
	def CxlAdvcGnlInf(self):
		del self._CxlAdvcGnlInf
		self._CxlAdvcGnlInf = base_types.UninitialisedField(self, 'CxlAdvcGnlInf', CorporateActionCancellation4, False)

	@property
	def DrpAgt(self):
		return self._DrpAgt

	@DrpAgt.setter
	def DrpAgt(self, value):
		self._DrpAgt = value if value is not None else base_types.UninitialisedField(self, 'DrpAgt', PartyIdentification137Choice, False)

	@DrpAgt.deleter
	def DrpAgt(self):
		del self._DrpAgt
		self._DrpAgt = base_types.UninitialisedField(self, 'DrpAgt', PartyIdentification137Choice, False)

	@property
	def InfAgt(self):
		return self._InfAgt

	@InfAgt.setter
	def InfAgt(self, value):
		self._InfAgt = value if value is not None else base_types.UninitialisedField(self, 'InfAgt', PartyIdentification137Choice, False)

	@InfAgt.deleter
	def InfAgt(self):
		del self._InfAgt
		self._InfAgt = base_types.UninitialisedField(self, 'InfAgt', PartyIdentification137Choice, False)

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if value is not None else base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification137Choice, True)

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification137Choice, True)

	@property
	def PhysSctiesAgt(self):
		return self._PhysSctiesAgt

	@PhysSctiesAgt.setter
	def PhysSctiesAgt(self, value):
		self._PhysSctiesAgt = value if value is not None else base_types.UninitialisedField(self, 'PhysSctiesAgt', PartyIdentification137Choice, False)

	@PhysSctiesAgt.deleter
	def PhysSctiesAgt(self):
		del self._PhysSctiesAgt
		self._PhysSctiesAgt = base_types.UninitialisedField(self, 'PhysSctiesAgt', PartyIdentification137Choice, False)

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if value is not None else base_types.UninitialisedField(self, 'PngAgt', PartyIdentification137Choice, True)

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = base_types.UninitialisedField(self, 'PngAgt', PartyIdentification137Choice, True)

	@property
	def Regar(self):
		return self._Regar

	@Regar.setter
	def Regar(self, value):
		self._Regar = value if value is not None else base_types.UninitialisedField(self, 'Regar', PartyIdentification137Choice, False)

	@Regar.deleter
	def Regar(self):
		del self._Regar
		self._Regar = base_types.UninitialisedField(self, 'Regar', PartyIdentification137Choice, False)

	@property
	def RsellngAgt(self):
		return self._RsellngAgt

	@RsellngAgt.setter
	def RsellngAgt(self, value):
		self._RsellngAgt = value if value is not None else base_types.UninitialisedField(self, 'RsellngAgt', PartyIdentification137Choice, True)

	@RsellngAgt.deleter
	def RsellngAgt(self):
		del self._RsellngAgt
		self._RsellngAgt = base_types.UninitialisedField(self, 'RsellngAgt', PartyIdentification137Choice, True)

	@property
	def SlctnAgt(self):
		return self._SlctnAgt

	@SlctnAgt.setter
	def SlctnAgt(self, value):
		self._SlctnAgt = value if value is not None else base_types.UninitialisedField(self, 'SlctnAgt', PartyIdentification137Choice, True)

	@SlctnAgt.deleter
	def SlctnAgt(self):
		del self._SlctnAgt
		self._SlctnAgt = base_types.UninitialisedField(self, 'SlctnAgt', PartyIdentification137Choice, True)

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
	def SubPngAgt(self):
		return self._SubPngAgt

	@SubPngAgt.setter
	def SubPngAgt(self, value):
		self._SubPngAgt = value if value is not None else base_types.UninitialisedField(self, 'SubPngAgt', PartyIdentification137Choice, True)

	@SubPngAgt.deleter
	def SubPngAgt(self):
		del self._SubPngAgt
		self._SubPngAgt = base_types.UninitialisedField(self, 'SubPngAgt', PartyIdentification137Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctsDtls', type=AccountIdentification74Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTxt', type=RestrictedFINZMax8000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction74, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation184, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlAdvcGnlInf', type=CorporateActionCancellation4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrpAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PhysSctiesAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Regar', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsellngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SlctnAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubPngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
	))