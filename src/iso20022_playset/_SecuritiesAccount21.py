# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification5
from . import ActiveOrHistoricCurrencyCode
from . import BaseOneRate

class SecuritiesAccount21(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_BaseCcy", "_FXRate", "_RptgCcy", "_SubAcct"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', AccountIdentification5, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', AccountIdentification5, False)

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if value is not None else base_types.UninitialisedField(self, 'BaseCcy', ActiveOrHistoricCurrencyCode, False)

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = base_types.UninitialisedField(self, 'BaseCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def FXRate(self):
		return self._FXRate

	@FXRate.setter
	def FXRate(self, value):
		self._FXRate = value if value is not None else base_types.UninitialisedField(self, 'FXRate', BaseOneRate, False)

	@FXRate.deleter
	def FXRate(self):
		del self._FXRate
		self._FXRate = base_types.UninitialisedField(self, 'FXRate', BaseOneRate, False)

	@property
	def RptgCcy(self):
		return self._RptgCcy

	@RptgCcy.setter
	def RptgCcy(self, value):
		self._RptgCcy = value if value is not None else base_types.UninitialisedField(self, 'RptgCcy', ActiveOrHistoricCurrencyCode, False)

	@RptgCcy.deleter
	def RptgCcy(self):
		del self._RptgCcy
		self._RptgCcy = base_types.UninitialisedField(self, 'RptgCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def SubAcct(self):
		return self._SubAcct

	@SubAcct.setter
	def SubAcct(self, value):
		self._SubAcct = value if value is not None else base_types.UninitialisedField(self, 'SubAcct', AccountIdentification5, False)

	@SubAcct.deleter
	def SubAcct(self):
		del self._SubAcct
		self._SubAcct = base_types.UninitialisedField(self, 'SubAcct', AccountIdentification5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=AccountIdentification5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcct', type=AccountIdentification5, min=0, max=1, mutex_group=None, array=False),
	))