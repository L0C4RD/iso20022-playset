# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import CurrencyReference3
from . import Max4Text
from . import Max500Text
from . import PercentageRate

class SettlementSubTotalCalculatedTax2(base_types._BaseFieldType):

	__slots__ = ["_BsisAmt", "_ClctdAmt", "_ClctdRate", "_TaxCcyXchg", "_TpCd", "_XmptnRsnCd", "_XmptnRsnTxt"]
	@property
	def BsisAmt(self):
		return self._BsisAmt

	@BsisAmt.setter
	def BsisAmt(self, value):
		self._BsisAmt = value if value is not None else base_types.UninitialisedField(self, 'BsisAmt', CurrencyAndAmount, True)

	@BsisAmt.deleter
	def BsisAmt(self):
		del self._BsisAmt
		self._BsisAmt = base_types.UninitialisedField(self, 'BsisAmt', CurrencyAndAmount, True)

	@property
	def ClctdAmt(self):
		return self._ClctdAmt

	@ClctdAmt.setter
	def ClctdAmt(self, value):
		self._ClctdAmt = value if value is not None else base_types.UninitialisedField(self, 'ClctdAmt', CurrencyAndAmount, True)

	@ClctdAmt.deleter
	def ClctdAmt(self):
		del self._ClctdAmt
		self._ClctdAmt = base_types.UninitialisedField(self, 'ClctdAmt', CurrencyAndAmount, True)

	@property
	def ClctdRate(self):
		return self._ClctdRate

	@ClctdRate.setter
	def ClctdRate(self, value):
		self._ClctdRate = value if value is not None else base_types.UninitialisedField(self, 'ClctdRate', PercentageRate, False)

	@ClctdRate.deleter
	def ClctdRate(self):
		del self._ClctdRate
		self._ClctdRate = base_types.UninitialisedField(self, 'ClctdRate', PercentageRate, False)

	@property
	def TaxCcyXchg(self):
		return self._TaxCcyXchg

	@TaxCcyXchg.setter
	def TaxCcyXchg(self, value):
		self._TaxCcyXchg = value if value is not None else base_types.UninitialisedField(self, 'TaxCcyXchg', CurrencyReference3, False)

	@TaxCcyXchg.deleter
	def TaxCcyXchg(self):
		del self._TaxCcyXchg
		self._TaxCcyXchg = base_types.UninitialisedField(self, 'TaxCcyXchg', CurrencyReference3, False)

	@property
	def TpCd(self):
		return self._TpCd

	@TpCd.setter
	def TpCd(self, value):
		self._TpCd = value if value is not None else base_types.UninitialisedField(self, 'TpCd', Max4Text, False)

	@TpCd.deleter
	def TpCd(self):
		del self._TpCd
		self._TpCd = base_types.UninitialisedField(self, 'TpCd', Max4Text, False)

	@property
	def XmptnRsnCd(self):
		return self._XmptnRsnCd

	@XmptnRsnCd.setter
	def XmptnRsnCd(self, value):
		self._XmptnRsnCd = value if value is not None else base_types.UninitialisedField(self, 'XmptnRsnCd', Max4Text, False)

	@XmptnRsnCd.deleter
	def XmptnRsnCd(self):
		del self._XmptnRsnCd
		self._XmptnRsnCd = base_types.UninitialisedField(self, 'XmptnRsnCd', Max4Text, False)

	@property
	def XmptnRsnTxt(self):
		return self._XmptnRsnTxt

	@XmptnRsnTxt.setter
	def XmptnRsnTxt(self, value):
		self._XmptnRsnTxt = value if value is not None else base_types.UninitialisedField(self, 'XmptnRsnTxt', Max500Text, False)

	@XmptnRsnTxt.deleter
	def XmptnRsnTxt(self):
		del self._XmptnRsnTxt
		self._XmptnRsnTxt = base_types.UninitialisedField(self, 'XmptnRsnTxt', Max500Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisAmt', type=CurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctdAmt', type=CurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCcyXchg', type=CurrencyReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsnCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsnTxt', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
	))