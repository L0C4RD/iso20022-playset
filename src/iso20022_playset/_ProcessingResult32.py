# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ATICAPartyType1Code import ATICAPartyType1Code
from ._ISO8583ActionCode import ISO8583ActionCode
from ._ISO8583ResponseCode import ISO8583ResponseCode
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._Max35Text import Max35Text

class ProcessingResult32(base_types._BaseFieldType):

	__slots__ = ["_ActnCd", "_NtlData", "_PrvtData", "_RspnCd", "_RspnRsn", "_RspnSrcCtry", "_RspnSrcId", "_RspnSrcNm", "_RspnSrcTp"]
	@property
	def ActnCd(self):
		return self._ActnCd

	@ActnCd.setter
	def ActnCd(self, value):
		self._ActnCd = value if type(value) != base_types.auto else self.make_default("ActnCd")

	@ActnCd.deleter
	def ActnCd(self):
		del self._ActnCd
		self._ActnCd = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if type(value) != base_types.auto else self.make_default("RspnCd")

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = None

	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if type(value) != base_types.auto else self.make_default("RspnRsn")

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = None

	@property
	def RspnSrcCtry(self):
		return self._RspnSrcCtry

	@RspnSrcCtry.setter
	def RspnSrcCtry(self, value):
		self._RspnSrcCtry = value if type(value) != base_types.auto else self.make_default("RspnSrcCtry")

	@RspnSrcCtry.deleter
	def RspnSrcCtry(self):
		del self._RspnSrcCtry
		self._RspnSrcCtry = None

	@property
	def RspnSrcId(self):
		return self._RspnSrcId

	@RspnSrcId.setter
	def RspnSrcId(self, value):
		self._RspnSrcId = value if type(value) != base_types.auto else self.make_default("RspnSrcId")

	@RspnSrcId.deleter
	def RspnSrcId(self):
		del self._RspnSrcId
		self._RspnSrcId = None

	@property
	def RspnSrcNm(self):
		return self._RspnSrcNm

	@RspnSrcNm.setter
	def RspnSrcNm(self, value):
		self._RspnSrcNm = value if type(value) != base_types.auto else self.make_default("RspnSrcNm")

	@RspnSrcNm.deleter
	def RspnSrcNm(self):
		del self._RspnSrcNm
		self._RspnSrcNm = None

	@property
	def RspnSrcTp(self):
		return self._RspnSrcTp

	@RspnSrcTp.setter
	def RspnSrcTp(self, value):
		self._RspnSrcTp = value if type(value) != base_types.auto else self.make_default("RspnSrcTp")

	@RspnSrcTp.deleter
	def RspnSrcTp(self):
		del self._RspnSrcTp
		self._RspnSrcTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnCd', type=ISO8583ActionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcTp', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
	))