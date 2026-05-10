import base_types
import ImpliedCurrencyAndAmount
import BaseOneRate
import Exact3NumericText
import ActiveCurrencyCode

class CurrencyConversion5(base_types._BaseFieldType):

	__slots__ = ["_TrgtCcyNmrc", "_Rate", "_ClctdAmt", "_TrgtCcy", "_SrcCcyNmrc", "_SrcCcy"]
	@property
	def TrgtCcyNmrc(self):
		return self._TrgtCcyNmrc

	@TrgtCcyNmrc.setter
	def TrgtCcyNmrc(self, value):
		self._TrgtCcyNmrc = value if type(value) != auto else self.make_default("TrgtCcyNmrc")

	@TrgtCcyNmrc.deleter
	def TrgtCcyNmrc(self):
		del self._TrgtCcyNmrc
		self._TrgtCcyNmrc = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def ClctdAmt(self):
		return self._ClctdAmt

	@ClctdAmt.setter
	def ClctdAmt(self, value):
		self._ClctdAmt = value if type(value) != auto else self.make_default("ClctdAmt")

	@ClctdAmt.deleter
	def ClctdAmt(self):
		del self._ClctdAmt
		self._ClctdAmt = None

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if type(value) != auto else self.make_default("TrgtCcy")

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = None

	@property
	def SrcCcyNmrc(self):
		return self._SrcCcyNmrc

	@SrcCcyNmrc.setter
	def SrcCcyNmrc(self, value):
		self._SrcCcyNmrc = value if type(value) != auto else self.make_default("SrcCcyNmrc")

	@SrcCcyNmrc.deleter
	def SrcCcyNmrc(self):
		del self._SrcCcyNmrc
		self._SrcCcyNmrc = None

	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if type(value) != auto else self.make_default("SrcCcy")

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrgtCcyNmrc', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctdAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcyNmrc', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

