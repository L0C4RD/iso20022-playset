# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import CurrencyCode
from . import DocumentIdentification1
from . import ISODate
from . import InsuranceClauses1Code
from . import Max350Text
from . import Max35Text
from . import Max70Text
from . import PartyIdentification26
from . import PartyIdentification29Choice
from . import PostalAddress5
from . import SingleTransport3

class InsuranceDataSet1(base_types._BaseFieldType):

	__slots__ = ["_Assrd", "_ClmsPyblAt", "_ClmsPyblIn", "_DataSetId", "_FctvDt", "_InsrdAmt", "_InsrdGoodsDesc", "_InsrncClauses", "_InsrncConds", "_InsrncDocId", "_IsseDt", "_Issr", "_PlcOfIsse", "_Trnsprt"]
	@property
	def Assrd(self):
		return self._Assrd

	@Assrd.setter
	def Assrd(self, value):
		self._Assrd = value if value is not None else base_types.UninitialisedField(self, 'Assrd', PartyIdentification29Choice, False)

	@Assrd.deleter
	def Assrd(self):
		del self._Assrd
		self._Assrd = base_types.UninitialisedField(self, 'Assrd', PartyIdentification29Choice, False)

	@property
	def ClmsPyblAt(self):
		return self._ClmsPyblAt

	@ClmsPyblAt.setter
	def ClmsPyblAt(self, value):
		self._ClmsPyblAt = value if value is not None else base_types.UninitialisedField(self, 'ClmsPyblAt', PostalAddress5, False)

	@ClmsPyblAt.deleter
	def ClmsPyblAt(self):
		del self._ClmsPyblAt
		self._ClmsPyblAt = base_types.UninitialisedField(self, 'ClmsPyblAt', PostalAddress5, False)

	@property
	def ClmsPyblIn(self):
		return self._ClmsPyblIn

	@ClmsPyblIn.setter
	def ClmsPyblIn(self, value):
		self._ClmsPyblIn = value if value is not None else base_types.UninitialisedField(self, 'ClmsPyblIn', CurrencyCode, False)

	@ClmsPyblIn.deleter
	def ClmsPyblIn(self):
		del self._ClmsPyblIn
		self._ClmsPyblIn = base_types.UninitialisedField(self, 'ClmsPyblIn', CurrencyCode, False)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', ISODate, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', ISODate, False)

	@property
	def InsrdAmt(self):
		return self._InsrdAmt

	@InsrdAmt.setter
	def InsrdAmt(self, value):
		self._InsrdAmt = value if value is not None else base_types.UninitialisedField(self, 'InsrdAmt', CurrencyAndAmount, False)

	@InsrdAmt.deleter
	def InsrdAmt(self):
		del self._InsrdAmt
		self._InsrdAmt = base_types.UninitialisedField(self, 'InsrdAmt', CurrencyAndAmount, False)

	@property
	def InsrdGoodsDesc(self):
		return self._InsrdGoodsDesc

	@InsrdGoodsDesc.setter
	def InsrdGoodsDesc(self, value):
		self._InsrdGoodsDesc = value if value is not None else base_types.UninitialisedField(self, 'InsrdGoodsDesc', Max70Text, False)

	@InsrdGoodsDesc.deleter
	def InsrdGoodsDesc(self):
		del self._InsrdGoodsDesc
		self._InsrdGoodsDesc = base_types.UninitialisedField(self, 'InsrdGoodsDesc', Max70Text, False)

	@property
	def InsrncClauses(self):
		return self._InsrncClauses

	@InsrncClauses.setter
	def InsrncClauses(self, value):
		self._InsrncClauses = value if value is not None else base_types.UninitialisedField(self, 'InsrncClauses', InsuranceClauses1Code, True)

	@InsrncClauses.deleter
	def InsrncClauses(self):
		del self._InsrncClauses
		self._InsrncClauses = base_types.UninitialisedField(self, 'InsrncClauses', InsuranceClauses1Code, True)

	@property
	def InsrncConds(self):
		return self._InsrncConds

	@InsrncConds.setter
	def InsrncConds(self, value):
		self._InsrncConds = value if value is not None else base_types.UninitialisedField(self, 'InsrncConds', Max350Text, True)

	@InsrncConds.deleter
	def InsrncConds(self):
		del self._InsrncConds
		self._InsrncConds = base_types.UninitialisedField(self, 'InsrncConds', Max350Text, True)

	@property
	def InsrncDocId(self):
		return self._InsrncDocId

	@InsrncDocId.setter
	def InsrncDocId(self, value):
		self._InsrncDocId = value if value is not None else base_types.UninitialisedField(self, 'InsrncDocId', Max35Text, False)

	@InsrncDocId.deleter
	def InsrncDocId(self):
		del self._InsrncDocId
		self._InsrncDocId = base_types.UninitialisedField(self, 'InsrncDocId', Max35Text, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification26, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification26, False)

	@property
	def PlcOfIsse(self):
		return self._PlcOfIsse

	@PlcOfIsse.setter
	def PlcOfIsse(self, value):
		self._PlcOfIsse = value if value is not None else base_types.UninitialisedField(self, 'PlcOfIsse', PostalAddress5, False)

	@PlcOfIsse.deleter
	def PlcOfIsse(self):
		del self._PlcOfIsse
		self._PlcOfIsse = base_types.UninitialisedField(self, 'PlcOfIsse', PostalAddress5, False)

	@property
	def Trnsprt(self):
		return self._Trnsprt

	@Trnsprt.setter
	def Trnsprt(self, value):
		self._Trnsprt = value if value is not None else base_types.UninitialisedField(self, 'Trnsprt', SingleTransport3, False)

	@Trnsprt.deleter
	def Trnsprt(self):
		del self._Trnsprt
		self._Trnsprt = base_types.UninitialisedField(self, 'Trnsprt', SingleTransport3, False)

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