# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import CardholderName3
from . import ISODate
from . import LoyaltyValueType1Code
from . import Max10NumericText
from . import Max35Text
from . import TrueFalseIndicator

class LoyaltyProgramme5(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_Elgblty", "_Issr", "_MmbAdr", "_MmbId", "_MmbNm", "_MmbSts", "_OthrValTp", "_Val", "_ValToCdt", "_ValToDbt", "_ValTp", "_XprtnDt"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', Max10NumericText, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', Max10NumericText, False)

	@property
	def Elgblty(self):
		return self._Elgblty

	@Elgblty.setter
	def Elgblty(self, value):
		self._Elgblty = value if value is not None else base_types.UninitialisedField(self, 'Elgblty', TrueFalseIndicator, True)

	@Elgblty.deleter
	def Elgblty(self):
		del self._Elgblty
		self._Elgblty = base_types.UninitialisedField(self, 'Elgblty', TrueFalseIndicator, True)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', Max35Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', Max35Text, False)

	@property
	def MmbAdr(self):
		return self._MmbAdr

	@MmbAdr.setter
	def MmbAdr(self, value):
		self._MmbAdr = value if value is not None else base_types.UninitialisedField(self, 'MmbAdr', Address2, False)

	@MmbAdr.deleter
	def MmbAdr(self):
		del self._MmbAdr
		self._MmbAdr = base_types.UninitialisedField(self, 'MmbAdr', Address2, False)

	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if value is not None else base_types.UninitialisedField(self, 'MmbId', Max35Text, False)

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = base_types.UninitialisedField(self, 'MmbId', Max35Text, False)

	@property
	def MmbNm(self):
		return self._MmbNm

	@MmbNm.setter
	def MmbNm(self, value):
		self._MmbNm = value if value is not None else base_types.UninitialisedField(self, 'MmbNm', CardholderName3, False)

	@MmbNm.deleter
	def MmbNm(self):
		del self._MmbNm
		self._MmbNm = base_types.UninitialisedField(self, 'MmbNm', CardholderName3, False)

	@property
	def MmbSts(self):
		return self._MmbSts

	@MmbSts.setter
	def MmbSts(self, value):
		self._MmbSts = value if value is not None else base_types.UninitialisedField(self, 'MmbSts', Max35Text, False)

	@MmbSts.deleter
	def MmbSts(self):
		del self._MmbSts
		self._MmbSts = base_types.UninitialisedField(self, 'MmbSts', Max35Text, False)

	@property
	def OthrValTp(self):
		return self._OthrValTp

	@OthrValTp.setter
	def OthrValTp(self, value):
		self._OthrValTp = value if value is not None else base_types.UninitialisedField(self, 'OthrValTp', Max35Text, False)

	@OthrValTp.deleter
	def OthrValTp(self):
		del self._OthrValTp
		self._OthrValTp = base_types.UninitialisedField(self, 'OthrValTp', Max35Text, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max10NumericText, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max10NumericText, False)

	@property
	def ValToCdt(self):
		return self._ValToCdt

	@ValToCdt.setter
	def ValToCdt(self, value):
		self._ValToCdt = value if value is not None else base_types.UninitialisedField(self, 'ValToCdt', Max10NumericText, False)

	@ValToCdt.deleter
	def ValToCdt(self):
		del self._ValToCdt
		self._ValToCdt = base_types.UninitialisedField(self, 'ValToCdt', Max10NumericText, False)

	@property
	def ValToDbt(self):
		return self._ValToDbt

	@ValToDbt.setter
	def ValToDbt(self, value):
		self._ValToDbt = value if value is not None else base_types.UninitialisedField(self, 'ValToDbt', Max10NumericText, False)

	@ValToDbt.deleter
	def ValToDbt(self):
		del self._ValToDbt
		self._ValToDbt = base_types.UninitialisedField(self, 'ValToDbt', Max10NumericText, False)

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if value is not None else base_types.UninitialisedField(self, 'ValTp', LoyaltyValueType1Code, False)

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = base_types.UninitialisedField(self, 'ValTp', LoyaltyValueType1Code, False)

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if value is not None else base_types.UninitialisedField(self, 'XprtnDt', ISODate, False)

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = base_types.UninitialisedField(self, 'XprtnDt', ISODate, False)

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