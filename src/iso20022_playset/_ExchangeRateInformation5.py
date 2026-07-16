# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOne25Rate
from . import Endpoint1Code
from . import ExchangeRateAgreementType1Code
from . import ExchangeRateType2Code
from . import ISO3NumericCurrencyCode
from . import ISODate
from . import ISOTime
from . import Max35Text
from . import Max70Text
from . import TrueFalseIndicator

class ExchangeRateInformation5(base_types._BaseFieldType):

	__slots__ = ["_AgrmtTp", "_BaseCcyCd", "_CntrCcyCd", "_Dt", "_EndPt", "_Id", "_OthrAgrmtTp", "_OthrEndPt", "_OthrRateTp", "_Prvdr", "_Rate", "_RateLckApld", "_RateLckElgbl", "_RateLckReqd", "_RateTp", "_Tm"]
	@property
	def AgrmtTp(self):
		return self._AgrmtTp

	@AgrmtTp.setter
	def AgrmtTp(self, value):
		self._AgrmtTp = value if value is not None else base_types.UninitialisedField(self, 'AgrmtTp', ExchangeRateAgreementType1Code, False)

	@AgrmtTp.deleter
	def AgrmtTp(self):
		del self._AgrmtTp
		self._AgrmtTp = base_types.UninitialisedField(self, 'AgrmtTp', ExchangeRateAgreementType1Code, False)

	@property
	def BaseCcyCd(self):
		return self._BaseCcyCd

	@BaseCcyCd.setter
	def BaseCcyCd(self, value):
		self._BaseCcyCd = value if value is not None else base_types.UninitialisedField(self, 'BaseCcyCd', ISO3NumericCurrencyCode, False)

	@BaseCcyCd.deleter
	def BaseCcyCd(self):
		del self._BaseCcyCd
		self._BaseCcyCd = base_types.UninitialisedField(self, 'BaseCcyCd', ISO3NumericCurrencyCode, False)

	@property
	def CntrCcyCd(self):
		return self._CntrCcyCd

	@CntrCcyCd.setter
	def CntrCcyCd(self, value):
		self._CntrCcyCd = value if value is not None else base_types.UninitialisedField(self, 'CntrCcyCd', ISO3NumericCurrencyCode, False)

	@CntrCcyCd.deleter
	def CntrCcyCd(self):
		del self._CntrCcyCd
		self._CntrCcyCd = base_types.UninitialisedField(self, 'CntrCcyCd', ISO3NumericCurrencyCode, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def EndPt(self):
		return self._EndPt

	@EndPt.setter
	def EndPt(self, value):
		self._EndPt = value if value is not None else base_types.UninitialisedField(self, 'EndPt', Endpoint1Code, False)

	@EndPt.deleter
	def EndPt(self):
		del self._EndPt
		self._EndPt = base_types.UninitialisedField(self, 'EndPt', Endpoint1Code, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@property
	def OthrAgrmtTp(self):
		return self._OthrAgrmtTp

	@OthrAgrmtTp.setter
	def OthrAgrmtTp(self, value):
		self._OthrAgrmtTp = value if value is not None else base_types.UninitialisedField(self, 'OthrAgrmtTp', Max35Text, False)

	@OthrAgrmtTp.deleter
	def OthrAgrmtTp(self):
		del self._OthrAgrmtTp
		self._OthrAgrmtTp = base_types.UninitialisedField(self, 'OthrAgrmtTp', Max35Text, False)

	@property
	def OthrEndPt(self):
		return self._OthrEndPt

	@OthrEndPt.setter
	def OthrEndPt(self, value):
		self._OthrEndPt = value if value is not None else base_types.UninitialisedField(self, 'OthrEndPt', Max35Text, False)

	@OthrEndPt.deleter
	def OthrEndPt(self):
		del self._OthrEndPt
		self._OthrEndPt = base_types.UninitialisedField(self, 'OthrEndPt', Max35Text, False)

	@property
	def OthrRateTp(self):
		return self._OthrRateTp

	@OthrRateTp.setter
	def OthrRateTp(self, value):
		self._OthrRateTp = value if value is not None else base_types.UninitialisedField(self, 'OthrRateTp', Max35Text, False)

	@OthrRateTp.deleter
	def OthrRateTp(self):
		del self._OthrRateTp
		self._OthrRateTp = base_types.UninitialisedField(self, 'OthrRateTp', Max35Text, False)

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if value is not None else base_types.UninitialisedField(self, 'Prvdr', Max70Text, False)

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = base_types.UninitialisedField(self, 'Prvdr', Max70Text, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', BaseOne25Rate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', BaseOne25Rate, False)

	@property
	def RateLckApld(self):
		return self._RateLckApld

	@RateLckApld.setter
	def RateLckApld(self, value):
		self._RateLckApld = value if value is not None else base_types.UninitialisedField(self, 'RateLckApld', TrueFalseIndicator, False)

	@RateLckApld.deleter
	def RateLckApld(self):
		del self._RateLckApld
		self._RateLckApld = base_types.UninitialisedField(self, 'RateLckApld', TrueFalseIndicator, False)

	@property
	def RateLckElgbl(self):
		return self._RateLckElgbl

	@RateLckElgbl.setter
	def RateLckElgbl(self, value):
		self._RateLckElgbl = value if value is not None else base_types.UninitialisedField(self, 'RateLckElgbl', TrueFalseIndicator, False)

	@RateLckElgbl.deleter
	def RateLckElgbl(self):
		del self._RateLckElgbl
		self._RateLckElgbl = base_types.UninitialisedField(self, 'RateLckElgbl', TrueFalseIndicator, False)

	@property
	def RateLckReqd(self):
		return self._RateLckReqd

	@RateLckReqd.setter
	def RateLckReqd(self, value):
		self._RateLckReqd = value if value is not None else base_types.UninitialisedField(self, 'RateLckReqd', TrueFalseIndicator, False)

	@RateLckReqd.deleter
	def RateLckReqd(self):
		del self._RateLckReqd
		self._RateLckReqd = base_types.UninitialisedField(self, 'RateLckReqd', TrueFalseIndicator, False)

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', ExchangeRateType2Code, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', ExchangeRateType2Code, False)

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if value is not None else base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtTp', type=ExchangeRateAgreementType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcyCd', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrCcyCd', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndPt', type=Endpoint1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAgrmtTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrEndPt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRateTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateLckApld', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateLckElgbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateLckReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=ExchangeRateType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))