# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection72

class OtherAmounts36(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_ChrgsFees", "_CsmptnTax", "_ExctgBrkrAmt", "_LclBrkrComssn", "_LclTax", "_Othr", "_StmpDty", "_TradAmt", "_TxTax", "_WhldgTax"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection72, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection72, False)

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection72, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection72, False)

	@property
	def CsmptnTax(self):
		return self._CsmptnTax

	@CsmptnTax.setter
	def CsmptnTax(self, value):
		self._CsmptnTax = value if value is not None else base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection72, False)

	@CsmptnTax.deleter
	def CsmptnTax(self):
		del self._CsmptnTax
		self._CsmptnTax = base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection72, False)

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection72, False)

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection72, False)

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if value is not None else base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection72, False)

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection72, False)

	@property
	def LclTax(self):
		return self._LclTax

	@LclTax.setter
	def LclTax(self, value):
		self._LclTax = value if value is not None else base_types.UninitialisedField(self, 'LclTax', AmountAndDirection72, False)

	@LclTax.deleter
	def LclTax(self):
		del self._LclTax
		self._LclTax = base_types.UninitialisedField(self, 'LclTax', AmountAndDirection72, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', AmountAndDirection72, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', AmountAndDirection72, False)

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if value is not None else base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection72, False)

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection72, False)

	@property
	def TradAmt(self):
		return self._TradAmt

	@TradAmt.setter
	def TradAmt(self, value):
		self._TradAmt = value if value is not None else base_types.UninitialisedField(self, 'TradAmt', AmountAndDirection72, False)

	@TradAmt.deleter
	def TradAmt(self):
		del self._TradAmt
		self._TradAmt = base_types.UninitialisedField(self, 'TradAmt', AmountAndDirection72, False)

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if value is not None else base_types.UninitialisedField(self, 'TxTax', AmountAndDirection72, False)

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = base_types.UninitialisedField(self, 'TxTax', AmountAndDirection72, False)

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if value is not None else base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection72, False)

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection72, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradAmt', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection72, min=0, max=1, mutex_group=None, array=False),
	))