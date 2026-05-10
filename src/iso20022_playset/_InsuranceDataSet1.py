from . import base_types
from ._CurrencyAndAmount import CurrencyAndAmount
from ._CurrencyCode import CurrencyCode
from ._DocumentIdentification1 import DocumentIdentification1
from ._ISODate import ISODate
from ._InsuranceClauses1Code import InsuranceClauses1Code
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._PartyIdentification26 import PartyIdentification26
from ._PartyIdentification29Choice import PartyIdentification29Choice
from ._PostalAddress5 import PostalAddress5
from ._SingleTransport3 import SingleTransport3

class InsuranceDataSet1(base_types._BaseFieldType):

	__slots__ = ["_Assrd", "_ClmsPyblAt", "_ClmsPyblIn", "_DataSetId", "_FctvDt", "_InsrdAmt", "_InsrdGoodsDesc", "_InsrncClauses", "_InsrncConds", "_InsrncDocId", "_IsseDt", "_Issr", "_PlcOfIsse", "_Trnsprt"]
	@property
	def Assrd(self):
		return self._Assrd

	@Assrd.setter
	def Assrd(self, value):
		self._Assrd = value if type(value) != base_types.auto else self.make_default("Assrd")

	@Assrd.deleter
	def Assrd(self):
		del self._Assrd
		self._Assrd = None

	@property
	def ClmsPyblAt(self):
		return self._ClmsPyblAt

	@ClmsPyblAt.setter
	def ClmsPyblAt(self, value):
		self._ClmsPyblAt = value if type(value) != base_types.auto else self.make_default("ClmsPyblAt")

	@ClmsPyblAt.deleter
	def ClmsPyblAt(self):
		del self._ClmsPyblAt
		self._ClmsPyblAt = None

	@property
	def ClmsPyblIn(self):
		return self._ClmsPyblIn

	@ClmsPyblIn.setter
	def ClmsPyblIn(self, value):
		self._ClmsPyblIn = value if type(value) != base_types.auto else self.make_default("ClmsPyblIn")

	@ClmsPyblIn.deleter
	def ClmsPyblIn(self):
		del self._ClmsPyblIn
		self._ClmsPyblIn = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != base_types.auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != base_types.auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	@property
	def InsrdAmt(self):
		return self._InsrdAmt

	@InsrdAmt.setter
	def InsrdAmt(self, value):
		self._InsrdAmt = value if type(value) != base_types.auto else self.make_default("InsrdAmt")

	@InsrdAmt.deleter
	def InsrdAmt(self):
		del self._InsrdAmt
		self._InsrdAmt = None

	@property
	def InsrdGoodsDesc(self):
		return self._InsrdGoodsDesc

	@InsrdGoodsDesc.setter
	def InsrdGoodsDesc(self, value):
		self._InsrdGoodsDesc = value if type(value) != base_types.auto else self.make_default("InsrdGoodsDesc")

	@InsrdGoodsDesc.deleter
	def InsrdGoodsDesc(self):
		del self._InsrdGoodsDesc
		self._InsrdGoodsDesc = None

	@property
	def InsrncClauses(self):
		return self._InsrncClauses

	@InsrncClauses.setter
	def InsrncClauses(self, value):
		self._InsrncClauses = value if type(value) != base_types.auto else self.make_default("InsrncClauses")

	@InsrncClauses.deleter
	def InsrncClauses(self):
		del self._InsrncClauses
		self._InsrncClauses = None

	@property
	def InsrncConds(self):
		return self._InsrncConds

	@InsrncConds.setter
	def InsrncConds(self, value):
		self._InsrncConds = value if type(value) != base_types.auto else self.make_default("InsrncConds")

	@InsrncConds.deleter
	def InsrncConds(self):
		del self._InsrncConds
		self._InsrncConds = None

	@property
	def InsrncDocId(self):
		return self._InsrncDocId

	@InsrncDocId.setter
	def InsrncDocId(self, value):
		self._InsrncDocId = value if type(value) != base_types.auto else self.make_default("InsrncDocId")

	@InsrncDocId.deleter
	def InsrncDocId(self):
		del self._InsrncDocId
		self._InsrncDocId = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def PlcOfIsse(self):
		return self._PlcOfIsse

	@PlcOfIsse.setter
	def PlcOfIsse(self, value):
		self._PlcOfIsse = value if type(value) != base_types.auto else self.make_default("PlcOfIsse")

	@PlcOfIsse.deleter
	def PlcOfIsse(self):
		del self._PlcOfIsse
		self._PlcOfIsse = None

	@property
	def Trnsprt(self):
		return self._Trnsprt

	@Trnsprt.setter
	def Trnsprt(self, value):
		self._Trnsprt = value if type(value) != base_types.auto else self.make_default("Trnsprt")

	@Trnsprt.deleter
	def Trnsprt(self):
		del self._Trnsprt
		self._Trnsprt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assrd', type=PartyIdentification29Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmsPyblAt', type=PostalAddress5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmsPyblIn', type=CurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrdAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrdGoodsDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncClauses', type=InsuranceClauses1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InsrncConds', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InsrncDocId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfIsse', type=PostalAddress5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trnsprt', type=SingleTransport3, min=0, max=1, mutex_group=None, array=False),
	))

