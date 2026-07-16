# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DocumentEntryAmendment1
from . import DocumentGeneralInformation5
from . import DocumentIdentification22
from . import Exact4AlphaNumericUnderscoreText
from . import Max35Text
from . import Max500Text
from . import ShipmentAttribute2

class SupportingDocumentEntry2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Attchmnt", "_DocTp", "_MtrtyData", "_NtryAmdmntId", "_NtryId", "_OrgnlDoc", "_ShipmntAttrbts", "_TtlAmt", "_TtlAmtAftrShipmnt", "_TtlAmtAftrShipmntInCtrctCcy", "_TtlAmtInCtrctCcy"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if value is not None else base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if value is not None else base_types.UninitialisedField(self, 'DocTp', Exact4AlphaNumericUnderscoreText, False)

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = base_types.UninitialisedField(self, 'DocTp', Exact4AlphaNumericUnderscoreText, False)

	@property
	def MtrtyData(self):
		return self._MtrtyData

	@MtrtyData.setter
	def MtrtyData(self, value):
		self._MtrtyData = value if value is not None else base_types.UninitialisedField(self, 'MtrtyData', Max35Text, False)

	@MtrtyData.deleter
	def MtrtyData(self):
		del self._MtrtyData
		self._MtrtyData = base_types.UninitialisedField(self, 'MtrtyData', Max35Text, False)

	@property
	def NtryAmdmntId(self):
		return self._NtryAmdmntId

	@NtryAmdmntId.setter
	def NtryAmdmntId(self, value):
		self._NtryAmdmntId = value if value is not None else base_types.UninitialisedField(self, 'NtryAmdmntId', DocumentEntryAmendment1, False)

	@NtryAmdmntId.deleter
	def NtryAmdmntId(self):
		del self._NtryAmdmntId
		self._NtryAmdmntId = base_types.UninitialisedField(self, 'NtryAmdmntId', DocumentEntryAmendment1, False)

	@property
	def NtryId(self):
		return self._NtryId

	@NtryId.setter
	def NtryId(self, value):
		self._NtryId = value if value is not None else base_types.UninitialisedField(self, 'NtryId', Max35Text, False)

	@NtryId.deleter
	def NtryId(self):
		del self._NtryId
		self._NtryId = base_types.UninitialisedField(self, 'NtryId', Max35Text, False)

	@property
	def OrgnlDoc(self):
		return self._OrgnlDoc

	@OrgnlDoc.setter
	def OrgnlDoc(self, value):
		self._OrgnlDoc = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDoc', DocumentIdentification22, False)

	@OrgnlDoc.deleter
	def OrgnlDoc(self):
		del self._OrgnlDoc
		self._OrgnlDoc = base_types.UninitialisedField(self, 'OrgnlDoc', DocumentIdentification22, False)

	@property
	def ShipmntAttrbts(self):
		return self._ShipmntAttrbts

	@ShipmntAttrbts.setter
	def ShipmntAttrbts(self, value):
		self._ShipmntAttrbts = value if value is not None else base_types.UninitialisedField(self, 'ShipmntAttrbts', ShipmentAttribute2, False)

	@ShipmntAttrbts.deleter
	def ShipmntAttrbts(self):
		del self._ShipmntAttrbts
		self._ShipmntAttrbts = base_types.UninitialisedField(self, 'ShipmntAttrbts', ShipmentAttribute2, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ActiveCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ActiveCurrencyAndAmount, False)

	@property
	def TtlAmtAftrShipmnt(self):
		return self._TtlAmtAftrShipmnt

	@TtlAmtAftrShipmnt.setter
	def TtlAmtAftrShipmnt(self, value):
		self._TtlAmtAftrShipmnt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtAftrShipmnt', ActiveCurrencyAndAmount, False)

	@TtlAmtAftrShipmnt.deleter
	def TtlAmtAftrShipmnt(self):
		del self._TtlAmtAftrShipmnt
		self._TtlAmtAftrShipmnt = base_types.UninitialisedField(self, 'TtlAmtAftrShipmnt', ActiveCurrencyAndAmount, False)

	@property
	def TtlAmtAftrShipmntInCtrctCcy(self):
		return self._TtlAmtAftrShipmntInCtrctCcy

	@TtlAmtAftrShipmntInCtrctCcy.setter
	def TtlAmtAftrShipmntInCtrctCcy(self, value):
		self._TtlAmtAftrShipmntInCtrctCcy = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtAftrShipmntInCtrctCcy', ActiveCurrencyAndAmount, False)

	@TtlAmtAftrShipmntInCtrctCcy.deleter
	def TtlAmtAftrShipmntInCtrctCcy(self):
		del self._TtlAmtAftrShipmntInCtrctCcy
		self._TtlAmtAftrShipmntInCtrctCcy = base_types.UninitialisedField(self, 'TtlAmtAftrShipmntInCtrctCcy', ActiveCurrencyAndAmount, False)

	@property
	def TtlAmtInCtrctCcy(self):
		return self._TtlAmtInCtrctCcy

	@TtlAmtInCtrctCcy.setter
	def TtlAmtInCtrctCcy(self, value):
		self._TtlAmtInCtrctCcy = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtInCtrctCcy', ActiveCurrencyAndAmount, False)

	@TtlAmtInCtrctCcy.deleter
	def TtlAmtInCtrctCcy(self):
		del self._TtlAmtInCtrctCcy
		self._TtlAmtInCtrctCcy = base_types.UninitialisedField(self, 'TtlAmtInCtrctCcy', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DocTp', type=Exact4AlphaNumericUnderscoreText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryAmdmntId', type=DocumentEntryAmendment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDoc', type=DocumentIdentification22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipmntAttrbts', type=ShipmentAttribute2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtAftrShipmnt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtAftrShipmntInCtrctCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtInCtrctCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))