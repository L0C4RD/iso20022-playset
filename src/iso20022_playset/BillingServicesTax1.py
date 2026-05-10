import base_types
import Max35Text
import DecimalNumber
import Max40Text
import AmountAndDirection34

class BillingServicesTax1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_PricgAmt", "_Rate", "_Nb", "_HstAmt"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def PricgAmt(self):
		return self._PricgAmt

	@PricgAmt.setter
	def PricgAmt(self, value):
		self._PricgAmt = value if type(value) != auto else self.make_default("PricgAmt")

	@PricgAmt.deleter
	def PricgAmt(self):
		del self._PricgAmt
		self._PricgAmt = None

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
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def HstAmt(self):
		return self._HstAmt

	@HstAmt.setter
	def HstAmt(self, value):
		self._HstAmt = value if type(value) != auto else self.make_default("HstAmt")

	@HstAmt.deleter
	def HstAmt(self):
		del self._HstAmt
		self._HstAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))

