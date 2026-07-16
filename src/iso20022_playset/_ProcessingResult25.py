# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Exact6AlphaNumericText
from . import ISO8583ResponseCode
from . import ISOMax3ACountryCode
from . import Max35Text
from . import PartyType26Code
from . import PartyType9Code

class ProcessingResult25(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ApprvlCd", "_RspnCd", "_RspnSrcAssgnr", "_RspnSrcCtry", "_RspnSrcId", "_RspnSrcOthrTp", "_RspnSrcShrtNm", "_RspnSrcTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalData1, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalData1, True)

	@property
	def ApprvlCd(self):
		return self._ApprvlCd

	@ApprvlCd.setter
	def ApprvlCd(self, value):
		self._ApprvlCd = value if value is not None else base_types.UninitialisedField(self, 'ApprvlCd', Exact6AlphaNumericText, False)

	@ApprvlCd.deleter
	def ApprvlCd(self):
		del self._ApprvlCd
		self._ApprvlCd = base_types.UninitialisedField(self, 'ApprvlCd', Exact6AlphaNumericText, False)

	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if value is not None else base_types.UninitialisedField(self, 'RspnCd', ISO8583ResponseCode, False)

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = base_types.UninitialisedField(self, 'RspnCd', ISO8583ResponseCode, False)

	@property
	def RspnSrcAssgnr(self):
		return self._RspnSrcAssgnr

	@RspnSrcAssgnr.setter
	def RspnSrcAssgnr(self, value):
		self._RspnSrcAssgnr = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcAssgnr', PartyType9Code, False)

	@RspnSrcAssgnr.deleter
	def RspnSrcAssgnr(self):
		del self._RspnSrcAssgnr
		self._RspnSrcAssgnr = base_types.UninitialisedField(self, 'RspnSrcAssgnr', PartyType9Code, False)

	@property
	def RspnSrcCtry(self):
		return self._RspnSrcCtry

	@RspnSrcCtry.setter
	def RspnSrcCtry(self, value):
		self._RspnSrcCtry = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcCtry', ISOMax3ACountryCode, False)

	@RspnSrcCtry.deleter
	def RspnSrcCtry(self):
		del self._RspnSrcCtry
		self._RspnSrcCtry = base_types.UninitialisedField(self, 'RspnSrcCtry', ISOMax3ACountryCode, False)

	@property
	def RspnSrcId(self):
		return self._RspnSrcId

	@RspnSrcId.setter
	def RspnSrcId(self, value):
		self._RspnSrcId = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcId', Max35Text, False)

	@RspnSrcId.deleter
	def RspnSrcId(self):
		del self._RspnSrcId
		self._RspnSrcId = base_types.UninitialisedField(self, 'RspnSrcId', Max35Text, False)

	@property
	def RspnSrcOthrTp(self):
		return self._RspnSrcOthrTp

	@RspnSrcOthrTp.setter
	def RspnSrcOthrTp(self, value):
		self._RspnSrcOthrTp = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcOthrTp', Max35Text, False)

	@RspnSrcOthrTp.deleter
	def RspnSrcOthrTp(self):
		del self._RspnSrcOthrTp
		self._RspnSrcOthrTp = base_types.UninitialisedField(self, 'RspnSrcOthrTp', Max35Text, False)

	@property
	def RspnSrcShrtNm(self):
		return self._RspnSrcShrtNm

	@RspnSrcShrtNm.setter
	def RspnSrcShrtNm(self, value):
		self._RspnSrcShrtNm = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcShrtNm', Max35Text, False)

	@RspnSrcShrtNm.deleter
	def RspnSrcShrtNm(self):
		del self._RspnSrcShrtNm
		self._RspnSrcShrtNm = base_types.UninitialisedField(self, 'RspnSrcShrtNm', Max35Text, False)

	@property
	def RspnSrcTp(self):
		return self._RspnSrcTp

	@RspnSrcTp.setter
	def RspnSrcTp(self, value):
		self._RspnSrcTp = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcTp', PartyType26Code, False)

	@RspnSrcTp.deleter
	def RspnSrcTp(self):
		del self._RspnSrcTp
		self._RspnSrcTp = base_types.UninitialisedField(self, 'RspnSrcTp', PartyType26Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApprvlCd', type=Exact6AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcAssgnr', type=PartyType9Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcOthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcTp', type=PartyType26Code, min=0, max=1, mutex_group=None, array=False),
	))