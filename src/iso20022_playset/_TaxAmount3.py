# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import PercentageRate
from . import TaxRecordDetails3

class TaxAmount3(base_types._BaseFieldType):

	__slots__ = ["_Dtls", "_Rate", "_TaxblBaseAmt", "_TtlAmt"]
	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if value is not None else base_types.UninitialisedField(self, 'Dtls', TaxRecordDetails3, True)

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = base_types.UninitialisedField(self, 'Dtls', TaxRecordDetails3, True)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def TaxblBaseAmt(self):
		return self._TaxblBaseAmt

	@TaxblBaseAmt.setter
	def TaxblBaseAmt(self, value):
		self._TaxblBaseAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxblBaseAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TaxblBaseAmt.deleter
	def TaxblBaseAmt(self):
		del self._TaxblBaseAmt
		self._TaxblBaseAmt = base_types.UninitialisedField(self, 'TaxblBaseAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dtls', type=TaxRecordDetails3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblBaseAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))