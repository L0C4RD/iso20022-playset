# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ISODate
from . import Max105Text
from . import Max35Text
from . import NotificationStatus3Code
from . import OriginalItemReference7
from . import UUIDv4Identifier

class OriginalItemAndStatus8(base_types._BaseFieldType):

	__slots__ = ["_AddtlStsInf", "_Amt", "_ItmSts", "_OrgnlEndToEndId", "_OrgnlItmId", "_OrgnlItmRef", "_OrgnlUETR", "_XpctdValDt"]
	@property
	def AddtlStsInf(self):
		return self._AddtlStsInf

	@AddtlStsInf.setter
	def AddtlStsInf(self, value):
		self._AddtlStsInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlStsInf', Max105Text, False)

	@AddtlStsInf.deleter
	def AddtlStsInf(self):
		del self._AddtlStsInf
		self._AddtlStsInf = base_types.UninitialisedField(self, 'AddtlStsInf', Max105Text, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def ItmSts(self):
		return self._ItmSts

	@ItmSts.setter
	def ItmSts(self, value):
		self._ItmSts = value if value is not None else base_types.UninitialisedField(self, 'ItmSts', NotificationStatus3Code, False)

	@ItmSts.deleter
	def ItmSts(self):
		del self._ItmSts
		self._ItmSts = base_types.UninitialisedField(self, 'ItmSts', NotificationStatus3Code, False)

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlEndToEndId', Max35Text, False)

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = base_types.UninitialisedField(self, 'OrgnlEndToEndId', Max35Text, False)

	@property
	def OrgnlItmId(self):
		return self._OrgnlItmId

	@OrgnlItmId.setter
	def OrgnlItmId(self, value):
		self._OrgnlItmId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlItmId', Max35Text, False)

	@OrgnlItmId.deleter
	def OrgnlItmId(self):
		del self._OrgnlItmId
		self._OrgnlItmId = base_types.UninitialisedField(self, 'OrgnlItmId', Max35Text, False)

	@property
	def OrgnlItmRef(self):
		return self._OrgnlItmRef

	@OrgnlItmRef.setter
	def OrgnlItmRef(self, value):
		self._OrgnlItmRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlItmRef', OriginalItemReference7, False)

	@OrgnlItmRef.deleter
	def OrgnlItmRef(self):
		del self._OrgnlItmRef
		self._OrgnlItmRef = base_types.UninitialisedField(self, 'OrgnlItmRef', OriginalItemReference7, False)

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if value is not None else base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	@property
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdValDt', ISODate, False)

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = base_types.UninitialisedField(self, 'XpctdValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsInf', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmSts', type=NotificationStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmRef', type=OriginalItemReference7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))