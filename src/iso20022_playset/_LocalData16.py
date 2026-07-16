# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import AdditionalInformation22
from . import CardholderName2
from . import ISOMax3ALanguageCode
from . import LocalAddress1
from . import Max35Text
from . import Max512Text

class LocalData16(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AddtlInf", "_CrdhldrNm", "_Lang", "_MldFrPstlCd", "_MlngAdr", "_MlngAdrUstrd", "_NcodgFrmt"]
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
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation22, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation22, True)

	@property
	def CrdhldrNm(self):
		return self._CrdhldrNm

	@CrdhldrNm.setter
	def CrdhldrNm(self, value):
		self._CrdhldrNm = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrNm', CardholderName2, False)

	@CrdhldrNm.deleter
	def CrdhldrNm(self):
		del self._CrdhldrNm
		self._CrdhldrNm = base_types.UninitialisedField(self, 'CrdhldrNm', CardholderName2, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@property
	def MldFrPstlCd(self):
		return self._MldFrPstlCd

	@MldFrPstlCd.setter
	def MldFrPstlCd(self, value):
		self._MldFrPstlCd = value if value is not None else base_types.UninitialisedField(self, 'MldFrPstlCd', Max35Text, False)

	@MldFrPstlCd.deleter
	def MldFrPstlCd(self):
		del self._MldFrPstlCd
		self._MldFrPstlCd = base_types.UninitialisedField(self, 'MldFrPstlCd', Max35Text, False)

	@property
	def MlngAdr(self):
		return self._MlngAdr

	@MlngAdr.setter
	def MlngAdr(self, value):
		self._MlngAdr = value if value is not None else base_types.UninitialisedField(self, 'MlngAdr', LocalAddress1, False)

	@MlngAdr.deleter
	def MlngAdr(self):
		del self._MlngAdr
		self._MlngAdr = base_types.UninitialisedField(self, 'MlngAdr', LocalAddress1, False)

	@property
	def MlngAdrUstrd(self):
		return self._MlngAdrUstrd

	@MlngAdrUstrd.setter
	def MlngAdrUstrd(self, value):
		self._MlngAdrUstrd = value if value is not None else base_types.UninitialisedField(self, 'MlngAdrUstrd', Max512Text, False)

	@MlngAdrUstrd.deleter
	def MlngAdrUstrd(self):
		del self._MlngAdrUstrd
		self._MlngAdrUstrd = base_types.UninitialisedField(self, 'MlngAdrUstrd', Max512Text, False)

	@property
	def NcodgFrmt(self):
		return self._NcodgFrmt

	@NcodgFrmt.setter
	def NcodgFrmt(self, value):
		self._NcodgFrmt = value if value is not None else base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	@NcodgFrmt.deleter
	def NcodgFrmt(self):
		del self._NcodgFrmt
		self._NcodgFrmt = base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrdhldrNm', type=CardholderName2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MldFrPstlCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngAdr', type=LocalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngAdrUstrd', type=Max512Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))