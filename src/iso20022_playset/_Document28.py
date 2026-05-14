from . import base_types
from ._ClassificationType4 import ClassificationType4
from ._CountryCode import CountryCode
from ._Document26 import Document26
from ._GenericIdentification190 import GenericIdentification190
from ._ISODateTime import ISODateTime
from ._Max140Text import Max140Text
from ._PartyIdentification260Choice import PartyIdentification260Choice
from ._Period4Choice import Period4Choice
from ._PositiveNumber import PositiveNumber
from ._SecurityIdentification49 import SecurityIdentification49
from ._SupplementaryDataEnvelope1 import SupplementaryDataEnvelope1
from ._TransactionOperationType13Code import TransactionOperationType13Code
from ._TrueFalseIndicator import TrueFalseIndicator

class Document28(base_types._BaseFieldType):

	__slots__ = ["_DataRcrd", "_DocRef", "_HomeCtry", "_HstCtry", "_HstrclData", "_PblctnPrd", "_PrsnlData", "_RgltryDataTp", "_RltdNtty", "_RltdPdctIdr", "_RltdPrd", "_RltdRgltryData", "_SubmissnDtTm", "_SubmissnTp", "_TechRcrdIdr", "_Vlntry", "_Vrsn"]
	@property
	def DataRcrd(self):
		return self._DataRcrd

	@DataRcrd.setter
	def DataRcrd(self, value):
		self._DataRcrd = value if type(value) != base_types.auto else self.make_default("DataRcrd")

	@DataRcrd.deleter
	def DataRcrd(self):
		del self._DataRcrd
		self._DataRcrd = None

	@property
	def DocRef(self):
		return self._DocRef

	@DocRef.setter
	def DocRef(self, value):
		self._DocRef = value if type(value) != base_types.auto else self.make_default("DocRef")

	@DocRef.deleter
	def DocRef(self):
		del self._DocRef
		self._DocRef = None

	@property
	def HomeCtry(self):
		return self._HomeCtry

	@HomeCtry.setter
	def HomeCtry(self, value):
		self._HomeCtry = value if type(value) != base_types.auto else self.make_default("HomeCtry")

	@HomeCtry.deleter
	def HomeCtry(self):
		del self._HomeCtry
		self._HomeCtry = None

	@property
	def HstCtry(self):
		return self._HstCtry

	@HstCtry.setter
	def HstCtry(self, value):
		self._HstCtry = value if type(value) != base_types.auto else self.make_default("HstCtry")

	@HstCtry.deleter
	def HstCtry(self):
		del self._HstCtry
		self._HstCtry = None

	@property
	def HstrclData(self):
		return self._HstrclData

	@HstrclData.setter
	def HstrclData(self, value):
		self._HstrclData = value if type(value) != base_types.auto else self.make_default("HstrclData")

	@HstrclData.deleter
	def HstrclData(self):
		del self._HstrclData
		self._HstrclData = None

	@property
	def PblctnPrd(self):
		return self._PblctnPrd

	@PblctnPrd.setter
	def PblctnPrd(self, value):
		self._PblctnPrd = value if type(value) != base_types.auto else self.make_default("PblctnPrd")

	@PblctnPrd.deleter
	def PblctnPrd(self):
		del self._PblctnPrd
		self._PblctnPrd = None

	@property
	def PrsnlData(self):
		return self._PrsnlData

	@PrsnlData.setter
	def PrsnlData(self, value):
		self._PrsnlData = value if type(value) != base_types.auto else self.make_default("PrsnlData")

	@PrsnlData.deleter
	def PrsnlData(self):
		del self._PrsnlData
		self._PrsnlData = None

	@property
	def RgltryDataTp(self):
		return self._RgltryDataTp

	@RgltryDataTp.setter
	def RgltryDataTp(self, value):
		self._RgltryDataTp = value if type(value) != base_types.auto else self.make_default("RgltryDataTp")

	@RgltryDataTp.deleter
	def RgltryDataTp(self):
		del self._RgltryDataTp
		self._RgltryDataTp = None

	@property
	def RltdNtty(self):
		return self._RltdNtty

	@RltdNtty.setter
	def RltdNtty(self, value):
		self._RltdNtty = value if type(value) != base_types.auto else self.make_default("RltdNtty")

	@RltdNtty.deleter
	def RltdNtty(self):
		del self._RltdNtty
		self._RltdNtty = None

	@property
	def RltdPdctIdr(self):
		return self._RltdPdctIdr

	@RltdPdctIdr.setter
	def RltdPdctIdr(self, value):
		self._RltdPdctIdr = value if type(value) != base_types.auto else self.make_default("RltdPdctIdr")

	@RltdPdctIdr.deleter
	def RltdPdctIdr(self):
		del self._RltdPdctIdr
		self._RltdPdctIdr = None

	@property
	def RltdPrd(self):
		return self._RltdPrd

	@RltdPrd.setter
	def RltdPrd(self, value):
		self._RltdPrd = value if type(value) != base_types.auto else self.make_default("RltdPrd")

	@RltdPrd.deleter
	def RltdPrd(self):
		del self._RltdPrd
		self._RltdPrd = None

	@property
	def RltdRgltryData(self):
		return self._RltdRgltryData

	@RltdRgltryData.setter
	def RltdRgltryData(self, value):
		self._RltdRgltryData = value if type(value) != base_types.auto else self.make_default("RltdRgltryData")

	@RltdRgltryData.deleter
	def RltdRgltryData(self):
		del self._RltdRgltryData
		self._RltdRgltryData = None

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if type(value) != base_types.auto else self.make_default("SubmissnDtTm")

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = None

	@property
	def SubmissnTp(self):
		return self._SubmissnTp

	@SubmissnTp.setter
	def SubmissnTp(self, value):
		self._SubmissnTp = value if type(value) != base_types.auto else self.make_default("SubmissnTp")

	@SubmissnTp.deleter
	def SubmissnTp(self):
		del self._SubmissnTp
		self._SubmissnTp = None

	@property
	def TechRcrdIdr(self):
		return self._TechRcrdIdr

	@TechRcrdIdr.setter
	def TechRcrdIdr(self, value):
		self._TechRcrdIdr = value if type(value) != base_types.auto else self.make_default("TechRcrdIdr")

	@TechRcrdIdr.deleter
	def TechRcrdIdr(self):
		del self._TechRcrdIdr
		self._TechRcrdIdr = None

	@property
	def Vlntry(self):
		return self._Vlntry

	@Vlntry.setter
	def Vlntry(self, value):
		self._Vlntry = value if type(value) != base_types.auto else self.make_default("Vlntry")

	@Vlntry.deleter
	def Vlntry(self):
		del self._Vlntry
		self._Vlntry = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataRcrd', type=SupplementaryDataEnvelope1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocRef', type=Document26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HomeCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstrclData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblctnPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnlData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryDataTp', type=ClassificationType4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdNtty', type=PartyIdentification260Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPdctIdr', type=SecurityIdentification49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRgltryData', type=GenericIdentification190, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnTp', type=TransactionOperationType13Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdIdr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vlntry', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))

