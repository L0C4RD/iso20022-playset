# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ATICAPartyType1Code
from . import Exact6AlphaNumericText
from . import ISO8583ActionCode
from . import ISO8583ResponseCode
from . import ISOMax3ACountryCode
from . import Max35Text

class ProcessingResult31(base_types._BaseFieldType):

	__slots__ = ["_ActnCd", "_ApprvlCd", "_NtlData", "_PrvtData", "_RspnCd", "_RspnRsn", "_RspnSrcCtry", "_RspnSrcId", "_RspnSrcNm", "_RspnSrcTp"]
	@property
	def ActnCd(self):
		return self._ActnCd

	@ActnCd.setter
	def ActnCd(self, value):
		self._ActnCd = value if value is not None else base_types.UninitialisedField(self, 'ActnCd', ISO8583ActionCode, False)

	@ActnCd.deleter
	def ActnCd(self):
		del self._ActnCd
		self._ActnCd = base_types.UninitialisedField(self, 'ActnCd', ISO8583ActionCode, False)

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

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
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if value is not None else base_types.UninitialisedField(self, 'RspnRsn', Max35Text, False)

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = base_types.UninitialisedField(self, 'RspnRsn', Max35Text, False)

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
	def RspnSrcNm(self):
		return self._RspnSrcNm

	@RspnSrcNm.setter
	def RspnSrcNm(self, value):
		self._RspnSrcNm = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcNm', Max35Text, False)

	@RspnSrcNm.deleter
	def RspnSrcNm(self):
		del self._RspnSrcNm
		self._RspnSrcNm = base_types.UninitialisedField(self, 'RspnSrcNm', Max35Text, False)

	@property
	def RspnSrcTp(self):
		return self._RspnSrcTp

	@RspnSrcTp.setter
	def RspnSrcTp(self, value):
		self._RspnSrcTp = value if value is not None else base_types.UninitialisedField(self, 'RspnSrcTp', ATICAPartyType1Code, False)

	@RspnSrcTp.deleter
	def RspnSrcTp(self):
		del self._RspnSrcTp
		self._RspnSrcTp = base_types.UninitialisedField(self, 'RspnSrcTp', ATICAPartyType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnCd', type=ISO8583ActionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApprvlCd', type=Exact6AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcTp', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
	))