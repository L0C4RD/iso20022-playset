# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BaseOne25Rate import BaseOne25Rate
from ._Endpoint2Code import Endpoint2Code
from ._ExchangeRateAgreementType2Code import ExchangeRateAgreementType2Code
from ._ExchangeRateType3Code import ExchangeRateType3Code
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ISODate import ISODate
from ._ISOTime import ISOTime
from ._Max70Text import Max70Text
from ._TrueFalseIndicator import TrueFalseIndicator

class CardExchangeRate1(base_types._BaseFieldType):

	__slots__ = ["_AgrmtTp", "_BaseCcyCd", "_CntrCcyCd", "_Dt", "_EndPt", "_Id", "_Prvdr", "_Rate", "_RateLckApld", "_RateLckElgbl", "_RateLckReqd", "_RateTp", "_Tm"]
	@property
	def AgrmtTp(self):
		return self._AgrmtTp

	@AgrmtTp.setter
	def AgrmtTp(self, value):
		self._AgrmtTp = value if type(value) != base_types.auto else self.make_default("AgrmtTp")

	@AgrmtTp.deleter
	def AgrmtTp(self):
		del self._AgrmtTp
		self._AgrmtTp = None

	@property
	def BaseCcyCd(self):
		return self._BaseCcyCd

	@BaseCcyCd.setter
	def BaseCcyCd(self, value):
		self._BaseCcyCd = value if type(value) != base_types.auto else self.make_default("BaseCcyCd")

	@BaseCcyCd.deleter
	def BaseCcyCd(self):
		del self._BaseCcyCd
		self._BaseCcyCd = None

	@property
	def CntrCcyCd(self):
		return self._CntrCcyCd

	@CntrCcyCd.setter
	def CntrCcyCd(self, value):
		self._CntrCcyCd = value if type(value) != base_types.auto else self.make_default("CntrCcyCd")

	@CntrCcyCd.deleter
	def CntrCcyCd(self):
		del self._CntrCcyCd
		self._CntrCcyCd = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def EndPt(self):
		return self._EndPt

	@EndPt.setter
	def EndPt(self, value):
		self._EndPt = value if type(value) != base_types.auto else self.make_default("EndPt")

	@EndPt.deleter
	def EndPt(self):
		del self._EndPt
		self._EndPt = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != base_types.auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def RateLckApld(self):
		return self._RateLckApld

	@RateLckApld.setter
	def RateLckApld(self, value):
		self._RateLckApld = value if type(value) != base_types.auto else self.make_default("RateLckApld")

	@RateLckApld.deleter
	def RateLckApld(self):
		del self._RateLckApld
		self._RateLckApld = None

	@property
	def RateLckElgbl(self):
		return self._RateLckElgbl

	@RateLckElgbl.setter
	def RateLckElgbl(self, value):
		self._RateLckElgbl = value if type(value) != base_types.auto else self.make_default("RateLckElgbl")

	@RateLckElgbl.deleter
	def RateLckElgbl(self):
		del self._RateLckElgbl
		self._RateLckElgbl = None

	@property
	def RateLckReqd(self):
		return self._RateLckReqd

	@RateLckReqd.setter
	def RateLckReqd(self, value):
		self._RateLckReqd = value if type(value) != base_types.auto else self.make_default("RateLckReqd")

	@RateLckReqd.deleter
	def RateLckReqd(self):
		del self._RateLckReqd
		self._RateLckReqd = None

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtTp', type=ExchangeRateAgreementType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcyCd', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrCcyCd', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndPt', type=Endpoint2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateLckApld', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateLckElgbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateLckReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=ExchangeRateType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))