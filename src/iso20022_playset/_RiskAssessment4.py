# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ATICAPartyType1Code import ATICAPartyType1Code
from ._ISO3NumericCountryCode import ISO3NumericCountryCode
from ._Max35Text import Max35Text
from ._RecommendationAction2 import RecommendationAction2
from ._TrueFalseIndicator import TrueFalseIndicator

class RiskAssessment4(base_types._BaseFieldType):

	__slots__ = ["_Cond", "_HghRskTx", "_NtlData", "_NttyCtry", "_NttyId", "_NttyTp", "_PrvtData", "_Rcmmndtn", "_Rslt", "_Rsn", "_Tp"]
	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if type(value) != base_types.auto else self.make_default("Cond")

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = None

	@property
	def HghRskTx(self):
		return self._HghRskTx

	@HghRskTx.setter
	def HghRskTx(self, value):
		self._HghRskTx = value if type(value) != base_types.auto else self.make_default("HghRskTx")

	@HghRskTx.deleter
	def HghRskTx(self):
		del self._HghRskTx
		self._HghRskTx = None

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
	def NttyCtry(self):
		return self._NttyCtry

	@NttyCtry.setter
	def NttyCtry(self, value):
		self._NttyCtry = value if type(value) != base_types.auto else self.make_default("NttyCtry")

	@NttyCtry.deleter
	def NttyCtry(self):
		del self._NttyCtry
		self._NttyCtry = None

	@property
	def NttyId(self):
		return self._NttyId

	@NttyId.setter
	def NttyId(self, value):
		self._NttyId = value if type(value) != base_types.auto else self.make_default("NttyId")

	@NttyId.deleter
	def NttyId(self):
		del self._NttyId
		self._NttyId = None

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if type(value) != base_types.auto else self.make_default("NttyTp")

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = None

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
	def Rcmmndtn(self):
		return self._Rcmmndtn

	@Rcmmndtn.setter
	def Rcmmndtn(self, value):
		self._Rcmmndtn = value if type(value) != base_types.auto else self.make_default("Rcmmndtn")

	@Rcmmndtn.deleter
	def Rcmmndtn(self):
		del self._Rcmmndtn
		self._Rcmmndtn = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cond', type=ATICALaxProcessing, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghRskTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NttyCtry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyTp', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcmmndtn', type=RecommendationAction2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rslt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))