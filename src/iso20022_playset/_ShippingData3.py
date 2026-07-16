# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ISODateTime
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max40Text
from . import Max6NumericText
from . import Max70Text
from . import ShippingPackage3
from . import Tax41
from . import TrueFalseIndicator

class ShippingData3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_IncntivAmt", "_Insrnc", "_InsrncAmt", "_InvcCreDtTm", "_InvcNb", "_MiscExpnss", "_NbOfPackgs", "_NetAmt", "_Packg", "_SummryCmmdtyId", "_SvcDscrptrCd", "_Tax"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def IncntivAmt(self):
		return self._IncntivAmt

	@IncntivAmt.setter
	def IncntivAmt(self, value):
		self._IncntivAmt = value if value is not None else base_types.UninitialisedField(self, 'IncntivAmt', ImpliedCurrencyAndAmount, False)

	@IncntivAmt.deleter
	def IncntivAmt(self):
		del self._IncntivAmt
		self._IncntivAmt = base_types.UninitialisedField(self, 'IncntivAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if value is not None else base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@property
	def InvcCreDtTm(self):
		return self._InvcCreDtTm

	@InvcCreDtTm.setter
	def InvcCreDtTm(self, value):
		self._InvcCreDtTm = value if value is not None else base_types.UninitialisedField(self, 'InvcCreDtTm', ISODateTime, False)

	@InvcCreDtTm.deleter
	def InvcCreDtTm(self):
		del self._InvcCreDtTm
		self._InvcCreDtTm = base_types.UninitialisedField(self, 'InvcCreDtTm', ISODateTime, False)

	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if value is not None else base_types.UninitialisedField(self, 'InvcNb', Max70Text, False)

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = base_types.UninitialisedField(self, 'InvcNb', Max70Text, False)

	@property
	def MiscExpnss(self):
		return self._MiscExpnss

	@MiscExpnss.setter
	def MiscExpnss(self, value):
		self._MiscExpnss = value if value is not None else base_types.UninitialisedField(self, 'MiscExpnss', ImpliedCurrencyAndAmount, False)

	@MiscExpnss.deleter
	def MiscExpnss(self):
		del self._MiscExpnss
		self._MiscExpnss = base_types.UninitialisedField(self, 'MiscExpnss', ImpliedCurrencyAndAmount, False)

	@property
	def NbOfPackgs(self):
		return self._NbOfPackgs

	@NbOfPackgs.setter
	def NbOfPackgs(self, value):
		self._NbOfPackgs = value if value is not None else base_types.UninitialisedField(self, 'NbOfPackgs', Max6NumericText, False)

	@NbOfPackgs.deleter
	def NbOfPackgs(self):
		del self._NbOfPackgs
		self._NbOfPackgs = base_types.UninitialisedField(self, 'NbOfPackgs', Max6NumericText, False)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', ImpliedCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if value is not None else base_types.UninitialisedField(self, 'Packg', ShippingPackage3, True)

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = base_types.UninitialisedField(self, 'Packg', ShippingPackage3, True)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def SvcDscrptrCd(self):
		return self._SvcDscrptrCd

	@SvcDscrptrCd.setter
	def SvcDscrptrCd(self, value):
		self._SvcDscrptrCd = value if value is not None else base_types.UninitialisedField(self, 'SvcDscrptrCd', Max40Text, False)

	@SvcDscrptrCd.deleter
	def SvcDscrptrCd(self):
		del self._SvcDscrptrCd
		self._SvcDscrptrCd = base_types.UninitialisedField(self, 'SvcDscrptrCd', Max40Text, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax41, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncntivAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MiscExpnss', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfPackgs', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Packg', type=ShippingPackage3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcDscrptrCd', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
	))