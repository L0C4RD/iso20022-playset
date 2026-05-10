from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .CorporateActionGeneralInformation191 import CorporateActionGeneralInformation191
from .CorporateAction76 import CorporateAction76
from .AccountIdentification75Choice import AccountIdentification75Choice
from .PartyIdentification137Choice import PartyIdentification137Choice
from .DocumentIdentification37 import DocumentIdentification37

class CorporateActionMovementPreliminaryAdviceCancellationAdvice002V13(base_types._BaseFieldType):

	__slots__ = ["_RsellngAgt", "_SplmtryData", "_CorpActnDtls", "_AcctDtls", "_DrpAgt", "_MvmntPrlimryAdvcId", "_PngAgt", "_SlctnAgt", "_InfAgt", "_CorpActnGnlInf", "_IssrAgt", "_SubPngAgt", "_PhysSctiesAgt", "_Regar"]
	@property
	def RsellngAgt(self):
		return self._RsellngAgt

	@RsellngAgt.setter
	def RsellngAgt(self, value):
		self._RsellngAgt = value if type(value) != base_types.auto else self.make_default("RsellngAgt")

	@RsellngAgt.deleter
	def RsellngAgt(self):
		del self._RsellngAgt
		self._RsellngAgt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != base_types.auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def DrpAgt(self):
		return self._DrpAgt

	@DrpAgt.setter
	def DrpAgt(self, value):
		self._DrpAgt = value if type(value) != base_types.auto else self.make_default("DrpAgt")

	@DrpAgt.deleter
	def DrpAgt(self):
		del self._DrpAgt
		self._DrpAgt = None

	@property
	def MvmntPrlimryAdvcId(self):
		return self._MvmntPrlimryAdvcId

	@MvmntPrlimryAdvcId.setter
	def MvmntPrlimryAdvcId(self, value):
		self._MvmntPrlimryAdvcId = value if type(value) != base_types.auto else self.make_default("MvmntPrlimryAdvcId")

	@MvmntPrlimryAdvcId.deleter
	def MvmntPrlimryAdvcId(self):
		del self._MvmntPrlimryAdvcId
		self._MvmntPrlimryAdvcId = None

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if type(value) != base_types.auto else self.make_default("PngAgt")

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = None

	@property
	def SlctnAgt(self):
		return self._SlctnAgt

	@SlctnAgt.setter
	def SlctnAgt(self, value):
		self._SlctnAgt = value if type(value) != base_types.auto else self.make_default("SlctnAgt")

	@SlctnAgt.deleter
	def SlctnAgt(self):
		del self._SlctnAgt
		self._SlctnAgt = None

	@property
	def InfAgt(self):
		return self._InfAgt

	@InfAgt.setter
	def InfAgt(self, value):
		self._InfAgt = value if type(value) != base_types.auto else self.make_default("InfAgt")

	@InfAgt.deleter
	def InfAgt(self):
		del self._InfAgt
		self._InfAgt = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if type(value) != base_types.auto else self.make_default("IssrAgt")

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = None

	@property
	def SubPngAgt(self):
		return self._SubPngAgt

	@SubPngAgt.setter
	def SubPngAgt(self, value):
		self._SubPngAgt = value if type(value) != base_types.auto else self.make_default("SubPngAgt")

	@SubPngAgt.deleter
	def SubPngAgt(self):
		del self._SubPngAgt
		self._SubPngAgt = None

	@property
	def PhysSctiesAgt(self):
		return self._PhysSctiesAgt

	@PhysSctiesAgt.setter
	def PhysSctiesAgt(self, value):
		self._PhysSctiesAgt = value if type(value) != base_types.auto else self.make_default("PhysSctiesAgt")

	@PhysSctiesAgt.deleter
	def PhysSctiesAgt(self):
		del self._PhysSctiesAgt
		self._PhysSctiesAgt = None

	@property
	def Regar(self):
		return self._Regar

	@Regar.setter
	def Regar(self, value):
		self._Regar = value if type(value) != base_types.auto else self.make_default("Regar")

	@Regar.deleter
	def Regar(self):
		del self._Regar
		self._Regar = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsellngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction76, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification75Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrpAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntPrlimryAdvcId', type=DocumentIdentification37, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SlctnAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation191, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubPngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PhysSctiesAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regar', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
	))

