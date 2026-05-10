from . import base_types
from .AmountAndDirection47 import AmountAndDirection47

class OtherAmounts32(base_types._BaseFieldType):

	__slots__ = ["_ChrgsFees", "_ExctgBrkrAmt", "_Othr", "_CsmptnTax", "_TradAmt", "_AcrdIntrstAmt", "_TxTax", "_WhldgTax", "_StmpDty", "_LclTax", "_LclBrkrComssn"]
	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if type(value) != base_types.auto else self.make_default("ChrgsFees")

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = None

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if type(value) != base_types.auto else self.make_default("ExctgBrkrAmt")

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def CsmptnTax(self):
		return self._CsmptnTax

	@CsmptnTax.setter
	def CsmptnTax(self, value):
		self._CsmptnTax = value if type(value) != base_types.auto else self.make_default("CsmptnTax")

	@CsmptnTax.deleter
	def CsmptnTax(self):
		del self._CsmptnTax
		self._CsmptnTax = None

	@property
	def TradAmt(self):
		return self._TradAmt

	@TradAmt.setter
	def TradAmt(self, value):
		self._TradAmt = value if type(value) != base_types.auto else self.make_default("TradAmt")

	@TradAmt.deleter
	def TradAmt(self):
		del self._TradAmt
		self._TradAmt = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != base_types.auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if type(value) != base_types.auto else self.make_default("TxTax")

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = None

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if type(value) != base_types.auto else self.make_default("WhldgTax")

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = None

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if type(value) != base_types.auto else self.make_default("StmpDty")

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = None

	@property
	def LclTax(self):
		return self._LclTax

	@LclTax.setter
	def LclTax(self, value):
		self._LclTax = value if type(value) != base_types.auto else self.make_default("LclTax")

	@LclTax.deleter
	def LclTax(self):
		del self._LclTax
		self._LclTax = None

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if type(value) != base_types.auto else self.make_default("LclBrkrComssn")

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradAmt', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection47, min=0, max=1, mutex_group=None, array=False),
	))

