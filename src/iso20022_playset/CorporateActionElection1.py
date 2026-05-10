import base_types
import Exact3NumericText
import UnitOrFaceAmount1Choice
import CorporateActionOption1FormatChoice

class CorporateActionElection1(base_types._BaseFieldType):

	__slots__ = ["_OrgnlInstdQty", "_RmngQty", "_OptnTp", "_OptnNb"]
	@property
	def OrgnlInstdQty(self):
		return self._OrgnlInstdQty

	@OrgnlInstdQty.setter
	def OrgnlInstdQty(self, value):
		self._OrgnlInstdQty = value if type(value) != auto else self.make_default("OrgnlInstdQty")

	@OrgnlInstdQty.deleter
	def OrgnlInstdQty(self):
		del self._OrgnlInstdQty
		self._OrgnlInstdQty = None

	@property
	def RmngQty(self):
		return self._RmngQty

	@RmngQty.setter
	def RmngQty(self, value):
		self._RmngQty = value if type(value) != auto else self.make_default("RmngQty")

	@RmngQty.deleter
	def RmngQty(self):
		del self._RmngQty
		self._RmngQty = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlInstdQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
	))

