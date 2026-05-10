import base_types
import BaseOneRate
import ActiveOrHistoricCurrencyCode
import AccountIdentification5

class SecuritiesAccount21(base_types._BaseFieldType):

	__slots__ = ["_FXRate", "_SubAcct", "_Acct", "_RptgCcy", "_BaseCcy"]
	@property
	def FXRate(self):
		return self._FXRate

	@FXRate.setter
	def FXRate(self, value):
		self._FXRate = value if type(value) != auto else self.make_default("FXRate")

	@FXRate.deleter
	def FXRate(self):
		del self._FXRate
		self._FXRate = None

	@property
	def SubAcct(self):
		return self._SubAcct

	@SubAcct.setter
	def SubAcct(self, value):
		self._SubAcct = value if type(value) != auto else self.make_default("SubAcct")

	@SubAcct.deleter
	def SubAcct(self):
		del self._SubAcct
		self._SubAcct = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def RptgCcy(self):
		return self._RptgCcy

	@RptgCcy.setter
	def RptgCcy(self, value):
		self._RptgCcy = value if type(value) != auto else self.make_default("RptgCcy")

	@RptgCcy.deleter
	def RptgCcy(self):
		del self._RptgCcy
		self._RptgCcy = None

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if type(value) != auto else self.make_default("BaseCcy")

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FXRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcct', type=AccountIdentification5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=AccountIdentification5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

