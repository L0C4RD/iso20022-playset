import base_types
import Max4AlphaNumericText
import RestrictedFINDecimalNumber
import Exact4AlphaNumericText

class ProprietaryQuantity9(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_QtyTp", "_Issr", "_SchmeNm"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def QtyTp(self):
		return self._QtyTp

	@QtyTp.setter
	def QtyTp(self, value):
		self._QtyTp = value if type(value) != auto else self.make_default("QtyTp")

	@QtyTp.deleter
	def QtyTp(self):
		del self._QtyTp
		self._QtyTp = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def SchmeNm(self):
		return self._SchmeNm

	@SchmeNm.setter
	def SchmeNm(self, value):
		self._SchmeNm = value if type(value) != auto else self.make_default("SchmeNm")

	@SchmeNm.deleter
	def SchmeNm(self):
		del self._SchmeNm
		self._SchmeNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=RestrictedFINDecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))

