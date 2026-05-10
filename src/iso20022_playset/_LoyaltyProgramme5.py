from . import base_types
from ._Address2 import Address2
from ._CardholderName3 import CardholderName3
from ._ISODate import ISODate
from ._LoyaltyValueType1Code import LoyaltyValueType1Code
from ._Max10NumericText import Max10NumericText
from ._Max35Text import Max35Text
from ._TrueFalseIndicator import TrueFalseIndicator

class LoyaltyProgramme5(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_Elgblty", "_Issr", "_MmbAdr", "_MmbId", "_MmbNm", "_MmbSts", "_OthrValTp", "_Val", "_ValToCdt", "_ValToDbt", "_ValTp", "_XprtnDt"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def Elgblty(self):
		return self._Elgblty

	@Elgblty.setter
	def Elgblty(self, value):
		self._Elgblty = value if type(value) != base_types.auto else self.make_default("Elgblty")

	@Elgblty.deleter
	def Elgblty(self):
		del self._Elgblty
		self._Elgblty = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def MmbAdr(self):
		return self._MmbAdr

	@MmbAdr.setter
	def MmbAdr(self, value):
		self._MmbAdr = value if type(value) != base_types.auto else self.make_default("MmbAdr")

	@MmbAdr.deleter
	def MmbAdr(self):
		del self._MmbAdr
		self._MmbAdr = None

	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if type(value) != base_types.auto else self.make_default("MmbId")

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = None

	@property
	def MmbNm(self):
		return self._MmbNm

	@MmbNm.setter
	def MmbNm(self, value):
		self._MmbNm = value if type(value) != base_types.auto else self.make_default("MmbNm")

	@MmbNm.deleter
	def MmbNm(self):
		del self._MmbNm
		self._MmbNm = None

	@property
	def MmbSts(self):
		return self._MmbSts

	@MmbSts.setter
	def MmbSts(self, value):
		self._MmbSts = value if type(value) != base_types.auto else self.make_default("MmbSts")

	@MmbSts.deleter
	def MmbSts(self):
		del self._MmbSts
		self._MmbSts = None

	@property
	def OthrValTp(self):
		return self._OthrValTp

	@OthrValTp.setter
	def OthrValTp(self, value):
		self._OthrValTp = value if type(value) != base_types.auto else self.make_default("OthrValTp")

	@OthrValTp.deleter
	def OthrValTp(self):
		del self._OthrValTp
		self._OthrValTp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def ValToCdt(self):
		return self._ValToCdt

	@ValToCdt.setter
	def ValToCdt(self, value):
		self._ValToCdt = value if type(value) != base_types.auto else self.make_default("ValToCdt")

	@ValToCdt.deleter
	def ValToCdt(self):
		del self._ValToCdt
		self._ValToCdt = None

	@property
	def ValToDbt(self):
		return self._ValToDbt

	@ValToDbt.setter
	def ValToDbt(self, value):
		self._ValToDbt = value if type(value) != base_types.auto else self.make_default("ValToDbt")

	@ValToDbt.deleter
	def ValToDbt(self):
		del self._ValToDbt
		self._ValToDbt = None

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if type(value) != base_types.auto else self.make_default("ValTp")

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = None

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if type(value) != base_types.auto else self.make_default("XprtnDt")

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Elgblty', type=TrueFalseIndicator, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbNm', type=CardholderName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbSts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrValTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValToCdt', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValToDbt', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValTp', type=LoyaltyValueType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

