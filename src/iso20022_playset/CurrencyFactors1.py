import base_types
import CurrencyCode
import ImpliedCurrencyAndAmount
import PercentageRate
import AgreedRate2

class CurrencyFactors1(base_types._BaseFieldType):

	__slots__ = ["_ShrtPosLmt", "_Ccy", "_Rate", "_VoltlyMrgn", "_MinPayInAmt"]
	@property
	def ShrtPosLmt(self):
		return self._ShrtPosLmt

	@ShrtPosLmt.setter
	def ShrtPosLmt(self, value):
		self._ShrtPosLmt = value if type(value) != auto else self.make_default("ShrtPosLmt")

	@ShrtPosLmt.deleter
	def ShrtPosLmt(self):
		del self._ShrtPosLmt
		self._ShrtPosLmt = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

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
	def VoltlyMrgn(self):
		return self._VoltlyMrgn

	@VoltlyMrgn.setter
	def VoltlyMrgn(self, value):
		self._VoltlyMrgn = value if type(value) != auto else self.make_default("VoltlyMrgn")

	@VoltlyMrgn.deleter
	def VoltlyMrgn(self):
		del self._VoltlyMrgn
		self._VoltlyMrgn = None

	@property
	def MinPayInAmt(self):
		return self._MinPayInAmt

	@MinPayInAmt.setter
	def MinPayInAmt(self, value):
		self._MinPayInAmt = value if type(value) != auto else self.make_default("MinPayInAmt")

	@MinPayInAmt.deleter
	def MinPayInAmt(self):
		del self._MinPayInAmt
		self._MinPayInAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtPosLmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=CurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=AgreedRate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoltlyMrgn', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPayInAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

