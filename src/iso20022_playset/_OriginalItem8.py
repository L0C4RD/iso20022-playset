# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ISODate
from . import Max35Text
from . import OriginalItemReference7
from . import UUIDv4Identifier

class OriginalItem8(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_OrgnlEndToEndId", "_OrgnlItmId", "_OrgnlItmRef", "_UETR", "_XpctdValDt"]
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
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if value is not None else base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

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
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmRef', type=OriginalItemReference7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))