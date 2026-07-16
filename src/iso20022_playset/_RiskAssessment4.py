# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ATICAPartyType1Code
from . import ISO3NumericCountryCode
from . import Max35Text
from . import RecommendationAction2
from . import TrueFalseIndicator

class RiskAssessment4(base_types._BaseFieldType):

	__slots__ = ["_Cond", "_HghRskTx", "_NtlData", "_NttyCtry", "_NttyId", "_NttyTp", "_PrvtData", "_Rcmmndtn", "_Rslt", "_Rsn", "_Tp"]
	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if value is not None else base_types.UninitialisedField(self, 'Cond', ATICALaxProcessing, False)

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = base_types.UninitialisedField(self, 'Cond', ATICALaxProcessing, False)

	@property
	def HghRskTx(self):
		return self._HghRskTx

	@HghRskTx.setter
	def HghRskTx(self, value):
		self._HghRskTx = value if value is not None else base_types.UninitialisedField(self, 'HghRskTx', TrueFalseIndicator, False)

	@HghRskTx.deleter
	def HghRskTx(self):
		del self._HghRskTx
		self._HghRskTx = base_types.UninitialisedField(self, 'HghRskTx', TrueFalseIndicator, False)

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
	def NttyCtry(self):
		return self._NttyCtry

	@NttyCtry.setter
	def NttyCtry(self, value):
		self._NttyCtry = value if value is not None else base_types.UninitialisedField(self, 'NttyCtry', ISO3NumericCountryCode, False)

	@NttyCtry.deleter
	def NttyCtry(self):
		del self._NttyCtry
		self._NttyCtry = base_types.UninitialisedField(self, 'NttyCtry', ISO3NumericCountryCode, False)

	@property
	def NttyId(self):
		return self._NttyId

	@NttyId.setter
	def NttyId(self, value):
		self._NttyId = value if value is not None else base_types.UninitialisedField(self, 'NttyId', Max35Text, False)

	@NttyId.deleter
	def NttyId(self):
		del self._NttyId
		self._NttyId = base_types.UninitialisedField(self, 'NttyId', Max35Text, False)

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if value is not None else base_types.UninitialisedField(self, 'NttyTp', ATICAPartyType1Code, False)

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = base_types.UninitialisedField(self, 'NttyTp', ATICAPartyType1Code, False)

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
	def Rcmmndtn(self):
		return self._Rcmmndtn

	@Rcmmndtn.setter
	def Rcmmndtn(self, value):
		self._Rcmmndtn = value if value is not None else base_types.UninitialisedField(self, 'Rcmmndtn', RecommendationAction2, True)

	@Rcmmndtn.deleter
	def Rcmmndtn(self):
		del self._Rcmmndtn
		self._Rcmmndtn = base_types.UninitialisedField(self, 'Rcmmndtn', RecommendationAction2, True)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', Max35Text, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', Max35Text, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max35Text, True)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max35Text, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

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