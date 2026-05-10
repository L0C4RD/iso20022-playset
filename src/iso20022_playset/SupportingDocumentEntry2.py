from . import base_types
import DocumentGeneralInformation5
import DocumentEntryAmendment1
import Max35Text
import ShipmentAttribute2
import ActiveCurrencyAndAmount
import DocumentIdentification22
import Max500Text
import Exact4AlphaNumericUnderscoreText

class SupportingDocumentEntry2(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_TtlAmtInCtrctCcy", "_TtlAmtAftrShipmnt", "_AddtlInf", "_MtrtyData", "_OrgnlDoc", "_DocTp", "_NtryId", "_NtryAmdmntId", "_ShipmntAttrbts", "_TtlAmt", "_TtlAmtAftrShipmntInCtrctCcy"]
	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if type(value) != auto else self.make_default("Attchmnt")

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = None

	@property
	def TtlAmtInCtrctCcy(self):
		return self._TtlAmtInCtrctCcy

	@TtlAmtInCtrctCcy.setter
	def TtlAmtInCtrctCcy(self, value):
		self._TtlAmtInCtrctCcy = value if type(value) != auto else self.make_default("TtlAmtInCtrctCcy")

	@TtlAmtInCtrctCcy.deleter
	def TtlAmtInCtrctCcy(self):
		del self._TtlAmtInCtrctCcy
		self._TtlAmtInCtrctCcy = None

	@property
	def TtlAmtAftrShipmnt(self):
		return self._TtlAmtAftrShipmnt

	@TtlAmtAftrShipmnt.setter
	def TtlAmtAftrShipmnt(self, value):
		self._TtlAmtAftrShipmnt = value if type(value) != auto else self.make_default("TtlAmtAftrShipmnt")

	@TtlAmtAftrShipmnt.deleter
	def TtlAmtAftrShipmnt(self):
		del self._TtlAmtAftrShipmnt
		self._TtlAmtAftrShipmnt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def MtrtyData(self):
		return self._MtrtyData

	@MtrtyData.setter
	def MtrtyData(self, value):
		self._MtrtyData = value if type(value) != auto else self.make_default("MtrtyData")

	@MtrtyData.deleter
	def MtrtyData(self):
		del self._MtrtyData
		self._MtrtyData = None

	@property
	def OrgnlDoc(self):
		return self._OrgnlDoc

	@OrgnlDoc.setter
	def OrgnlDoc(self, value):
		self._OrgnlDoc = value if type(value) != auto else self.make_default("OrgnlDoc")

	@OrgnlDoc.deleter
	def OrgnlDoc(self):
		del self._OrgnlDoc
		self._OrgnlDoc = None

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if type(value) != auto else self.make_default("DocTp")

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = None

	@property
	def NtryId(self):
		return self._NtryId

	@NtryId.setter
	def NtryId(self, value):
		self._NtryId = value if type(value) != auto else self.make_default("NtryId")

	@NtryId.deleter
	def NtryId(self):
		del self._NtryId
		self._NtryId = None

	@property
	def NtryAmdmntId(self):
		return self._NtryAmdmntId

	@NtryAmdmntId.setter
	def NtryAmdmntId(self, value):
		self._NtryAmdmntId = value if type(value) != auto else self.make_default("NtryAmdmntId")

	@NtryAmdmntId.deleter
	def NtryAmdmntId(self):
		del self._NtryAmdmntId
		self._NtryAmdmntId = None

	@property
	def ShipmntAttrbts(self):
		return self._ShipmntAttrbts

	@ShipmntAttrbts.setter
	def ShipmntAttrbts(self, value):
		self._ShipmntAttrbts = value if type(value) != auto else self.make_default("ShipmntAttrbts")

	@ShipmntAttrbts.deleter
	def ShipmntAttrbts(self):
		del self._ShipmntAttrbts
		self._ShipmntAttrbts = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def TtlAmtAftrShipmntInCtrctCcy(self):
		return self._TtlAmtAftrShipmntInCtrctCcy

	@TtlAmtAftrShipmntInCtrctCcy.setter
	def TtlAmtAftrShipmntInCtrctCcy(self, value):
		self._TtlAmtAftrShipmntInCtrctCcy = value if type(value) != auto else self.make_default("TtlAmtAftrShipmntInCtrctCcy")

	@TtlAmtAftrShipmntInCtrctCcy.deleter
	def TtlAmtAftrShipmntInCtrctCcy(self):
		del self._TtlAmtAftrShipmntInCtrctCcy
		self._TtlAmtAftrShipmntInCtrctCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmtInCtrctCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtAftrShipmnt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDoc', type=DocumentIdentification22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocTp', type=Exact4AlphaNumericUnderscoreText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryAmdmntId', type=DocumentEntryAmendment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipmntAttrbts', type=ShipmentAttribute2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtAftrShipmntInCtrctCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

